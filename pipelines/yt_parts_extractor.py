import os
import sys
import json
import time
import subprocess
import re
from pathlib import Path
from typing import List, Dict, Any, Optional

# Importowanie bibliotek Google GenAI (zakładając obecność w środowisku)
try:
    from google import genai
    from google.genai import types as genai_types
except ImportError:
    print("BŁĄD: Brak biblioteki google-genai. Zainstaluj: pip install google-genai")
    sys.exit(1)

class YTPartsExtractor:
    def __init__(self, api_keys: List[str]):
        self.api_keys = api_keys
        self.current_key_idx = 0
        self.clients = [genai.Client(api_key=k) for k in api_keys]
        
        # Modele zgodnie z dyspozycją użytkownika - Faza 1 i 2 na Gemma 4
        self.MODEL_ANALYSIS = "gemma-4-31b" 
        self.MODEL_VERIFICATION = "gemma-4-31b" 
        
    def get_client(self):
        client = self.clients[self.current_key_idx]
        self.current_key_idx = (self.current_key_idx + 1) % len(self.clients)
        return client

    def analyze_video_context(self, video_path: str, youtube_url: str):
        """
        Faza 1: Gemini analizuje cały film, audio i transkrypcję.
        Szuka urządzeń, części i momentów ich wystąpienia.
        """
        client = self.get_client()
        
        print(f"🚀 Przesyłam wideo do File API: {video_path}")
        video_file = client.files.upload(path=video_path)
        
        # Czekanie na przetworzenie wideo przez Google
        while video_file.state.name == "PROCESSING":
            time.sleep(5)
            video_file = client.files.get(name=video_file.name)
            
        if video_file.state.name == "FAILED":
            raise Exception("Błąd przetwarzania wideo przez Google File API.")

        system_instruction = """
        Jesteś ekspertem inżynierii odwrotnej i serwisantem AGD/RTV. 
        Twoim zadaniem jest analiza filmu z naprawy w celu zidentyfikowania konkretnych części zamiennych.
        
        ZASADY ANTY-HALUCYNACYJNE:
        1. Podawaj numery części TYLKO jeśli widnieją na naklejkach, grawerach lub są wyraźnie wypowiedziane w kontekście pokazywanego elementu.
        2. Musisz podać DOKŁADNY CZAS (timestamp w sekundach), w którym dana część lub jej numer jest najlepiej widoczna.
        3. Jeśli nie jesteś pewien numeru - oznacz go jako "UNCERTAIN".
        4. Rozróżniaj model całego urządzenia od numeru konkretnej części.
        
        FORMAT WYJŚCIOWY (JSON):
        {
          "device_model": "Dokładny model urządzenia",
          "detected_parts": [
            {
              "part_name": "Nazwa części (np. pompa odpływowa)",
              "part_number": "Numer seryjny/katalogowy",
              "timestamp_seconds": 124,
              "confidence": 0.0-1.0,
              "context_note": "Dlaczego uważasz, że to ta część?"
            }
          ]
        }
        """
        
        prompt = f"Przeanalizuj ten film z YouTube ({youtube_url}). Skup się na identyfikacji części. Podaj precyzyjne czasy dla każdej znalezionej części."
        
        print("🧠 Analiza multimodalna w toku...")
        response = client.models.generate_content(
            model=self.MODEL_ANALYSIS,
            contents=[
                genai_types.Content(role="user", parts=[
                    genai_types.Part.from_uri(file_uri=video_file.uri, mime_type=video_file.mime_type),
                    genai_types.Part.from_text(text=prompt)
                ])
            ],
            config=genai_types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.1, # Niska temperatura dla precyzji
                response_mime_type="application/json"
            )
        )
        
        return json.loads(response.text)

    def verify_with_frame(self, video_path: str, timestamp: int, expected_part_number: str):
        """
        Faza 2: Wycięcie klatki i weryfikacja przez inny model (Gemma).
        """
        frame_path = f"temp_frame_{timestamp}.jpg"
        print(f"📸 Wycinam klatkę z sekundy {timestamp}...")
        
        # Wycinanie klatki za pomocą ffmpeg
        subprocess.run([
            "ffmpeg", "-y", "-ss", str(timestamp), "-i", video_path,
            "-vframes", "1", "-q:v", "2", frame_path
        ], capture_output=True)
        
        if not os.path.exists(frame_path):
            return False, "Nie udało się wyciąć klatki"

        client = self.get_client()
        
        with open(frame_path, "rb") as f:
            img_data = f.read()

        prompt = f"Spójrz na to zdjęcie z serwisu urządzenia. Czy widzisz na nim wyraźnie napis/numer: '{expected_part_number}'? Odpowiedz TYLKO JSON: {{\"verified\": true/false, \"observed_text\": \"co widzisz\", \"confidence\": 0.9}}"
        
        # Używamy Gemmy lub innego modelu do cross-checku
        response = client.models.generate_content(
            model=self.MODEL_VERIFICATION,
            contents=[
                genai_types.Part.from_bytes(data=img_data, mime_type="image/jpeg"),
                genai_types.Part.from_text(text=prompt)
            ],
            config=genai_types.GenerateContentConfig(temperature=0.0)
        )
        
        os.remove(frame_path) # Sprzątanie
        try:
            return json.loads(response.text), None
        except:
            return {"verified": False, "observed_text": response.text}, "Błąd parsowania weryfikacji"

    def process_url(self, youtube_url: str):
        # 1. Pobieranie wideo (uproszczone - wymaga yt-dlp)
        video_filename = "temp_yt_video.mp4"
        print(f"📥 Pobieram wideo z {youtube_url}...")
        subprocess.run(["yt-dlp", "-f", "bestvideo[height<=720]+bestaudio/best[ext=mp4]", "-o", video_filename, youtube_url])
        
        try:
            # 2. Analiza kontekstowa
            analysis = self.analyze_video_context(video_filename, youtube_url)
            print(f"✅ Analiza wstępna zakończona. Znaleziono {len(analysis.get('detected_parts', []))} części.")
            
            final_results = []
            for part in analysis.get("detected_parts", []):
                # 3. Podwójna weryfikacja na klatce
                if part["part_number"] != "UNCERTAIN":
                    ver, err = self.verify_with_frame(video_filename, part["timestamp_seconds"], part["part_number"])
                    part["verification"] = ver
                    if ver.get("verified"):
                        print(f"⭐ CZĘŚĆ POTWIERDZONA: {part['part_number']}")
                    else:
                        print(f"⚠️ CZĘŚĆ NIEPOTWIERDZONA: {part['part_number']} (Widziano: {ver.get('observed_text')})")
                
                part["yt_link_with_time"] = f"{youtube_url}&t={part['timestamp_seconds']}s"
                final_results.append(part)
                
            return {
                "url": youtube_url,
                "device": analysis.get("device_model"),
                "results": final_results
            }
            
        finally:
            if os.path.exists(video_filename):
                os.remove(video_filename)

if __name__ == "__main__":
    # Przykład użycia
    keys = [os.environ.get("GEMINI_API_KEY")] # W środowisku produkcyjnym lista kluczy
    extractor = YTPartsExtractor(keys)
    res = extractor.process_url("https://www.youtube.com/watch?v=DODAJ_LINK_TUTAJ")
    print(json.dumps(res, indent=2))
