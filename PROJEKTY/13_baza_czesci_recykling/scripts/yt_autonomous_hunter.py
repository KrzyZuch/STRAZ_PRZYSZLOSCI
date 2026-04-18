#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import time
import argparse
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from yt_parts_extractor import YTPartsExtractor

# Konfiguracja ścieżek
BASE_DIR = Path("/home/krzysiek/Dokumenty/INFO_GROUP/STRAZ_POLSKIEGO_Ai/PROJEKTY/13_baza_czesci_recykling/autonomous_test")
RESULTS_FILE = BASE_DIR / "results" / "test_db.jsonl"
HISTORY_FILE = BASE_DIR / "processed_videos.json"
LOG_DIR = BASE_DIR / "logs"

# Słowa kluczowe do polowania (PL i EN)
KEYWORDS = [
    "naprawa pralki", "wymiana łożysk pralka", "serwis AGD", "rozbiórka laptopa",
    "repair washing machine", "laptop teardown", "disassembly smartphone", "fixing electronics",
    "wymiana matrycy", "naprawa zasilacza", "płyta główna naprawa", "motherboard repair"
]

class YTHunter:
    def __init__(self, yt_api_key: str, gemini_api_keys: list):
        self.yt_api_key = yt_api_key
        self.extractor = YTPartsExtractor(gemini_api_keys)
        self.history = self.load_history()

    def load_history(self):
        if HISTORY_FILE.exists():
            with open(HISTORY_FILE, "r") as f:
                return set(json.load(f))
        return set()

    def save_history(self):
        with open(HISTORY_FILE, "w") as f:
            json.dump(list(self.history), f)

    def search_videos(self, query: str, max_results=5):
        print(f"🔍 Szukam: {query}")
        params = {
            "part": "snippet",
            "q": query,
            "type": "video",
            "maxResults": max_results,
            "key": self.yt_api_key,
            "relevanceLanguage": "pl" if any(c in query.lower() for c in "ąćęłńóśźż") else "en"
        }
        url = f"https://www.googleapis.com/youtube/v3/search?{urlencode(params)}"
        req = Request(url, headers={"Accept": "application/json"})
        
        try:
            with urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data.get("items", [])
        except Exception as e:
            print(f"❌ Błąd wyszukiwania YouTube: {e}")
            return []

    def hunt(self):
        for kw in KEYWORDS:
            videos = self.search_videos(kw)
            for v in videos:
                vid_id = v["id"]["videoId"]
                if vid_id in self.history:
                    print(f"⏭️ Pomijam (już w bazie): {vid_id}")
                    continue
                
                yt_url = f"https://www.youtube.com/watch?v={vid_id}"
                print(f"🎯 Atakuję film: {v['snippet']['title']} ({yt_url})")
                
                try:
                    # Przetwarzanie przez Gemma 4
                    result = self.extractor.process_url(yt_url)
                    
                    if result and result.get("results"):
                        self.save_result(result)
                        print(f"✨ Sukces! Wyciągnięto {len(result['results'])} części.")
                    
                    self.history.add(vid_id)
                    self.save_history()
                    
                except Exception as e:
                    print(f"⚠️ Błąd podczas przetwarzania {vid_id}: {e}")
                
                # Pauza między filmami, żeby nie przegrzać API/systemu
                time.sleep(10)

    def save_result(self, result):
        with open(RESULTS_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(result, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    # Automatyczne pobieranie kluczy (uproszczone dla testu)
    # W produkcji należy użyć pełnej logiki z youtube_top_music_pl_v3.py
    YT_KEY = os.environ.get("YOUTUBE_API_KEY")
    GEMINI_KEYS = [os.environ.get("GEMINI_API_KEY")]
    
    if not YT_KEY or not GEMINI_KEYS[0]:
        print("❌ Brak kluczy API (YOUTUBE_API_KEY / GEMINI_API_KEY)!")
        exit(1)

    hunter = YTHunter(YT_KEY, GEMINI_KEYS)
    print("🚦 Start Autonomicznego Łowcy Części (Test Mode)...")
    hunter.hunt()
