// Main Entry Point for Bot AI Logic
import { knowledgeBundle } from "./generated_knowledge_bundle.js";

// Re-exports from base utils
export * from "./base_utils.js";

// Re-exports from modules
export * from "./ai_providers.js";
export * from "./sessions.js";
export * from "./recycled_catalog.js";
export * from "./onboarding.js";
export * from "./vision.js";
export * from "./datasheet.js";
export * from "./ai_logic.js";
export * from "./history.js";

// Runtime schema enforcement functions are now NO-OPs or removed.
export async function ensureRecycledKnowledgeSchema(db) { /* Handled by migrations */ }
export async function ensureTelegramAiSchema(db) { /* Handled by migrations */ }
export async function ensureTelegramThrottleSchema(db) { /* Handled by migrations */ }

// High-level intent routing
export function routeTelegramIntent(message) {
  const text = (message?.text || message?.caption || "").trim();
  if (text.startsWith("/")) return { intent: "command", command: text.slice(1).split(" ")[0].toLowerCase() };
  if (text.toLowerCase().includes("pomysl") || text.toLowerCase().includes("uwaga")) return { intent: "issue", classification: { kind: "idea", content: text, label: "pomysł" } };
  return { intent: "chat" };
}

export function buildIssueTitle(classification) { return classification.content.slice(0, 50); }
export function buildIssueBody(message, classification, draft) { return draft.edited_description; }
export function buildIssueModerationReply(mod) { return mod.decision === "accept" ? null : "Zgłoszenie odrzucone."; }
export function buildIssueThrottleReply(sec) { return `Zbyt szybko! Czekaj ${sec}s.`; }
export function buildChatThrottleReply(sec) { return `Zbyt szybko! Czekaj ${sec}s.`; }
export function buildCommandReply(command) {
  if (command === "start") {
    return [
      "Inicjatywa Straż Przyszłości – Intelekt wyprzedza Kapitał! 🇵🇱",
      "",
      "Jestem Twoim terminalem do budowy Narodowych Sił Intelektualnych. Pomogę Ci odnaleźć się w repozytorium, dopasować zadania do Twoich pasji oraz przekazać Twoje pomysły do zespołu.",
      "",
      "Mogę działać w czterech trybach:",
      "🤖 Asystent: Zadaj dowolne pytanie o inicjatywę i dokumenty.",
      "🧭 Onboarding: Opisz swoje kompetencje, a wskażę Ci ścieżkę.",
      "🚀 Zgłoszenia: Wyślij wiadomość z prefiksem \"Pomysl:\" lub \"Uwaga:\", aby utworzyć Issue na GitHubie.",
      "♻️ Recykling: Wyślij model lub zdjęcie PCB, a sprawdzę bazę reuse.",
      "📄 Datasheet: Wyślij PDF lub nazwę części, aby pobrać dokumentację i zadać pytanie AI (RAG).",
      "🎨 Rezystory: Wyślij zdjęcie rezystora, a odczytam jego wartość (paski/SMD).",
      "",
      "Komendy: /help, /reset",
    ].join("\n");
  }

  if (command === "help") {
    return [
      "Jak używać bota:",
      "- opisz, czym się zajmujesz, a dopasuję Ci ścieżkę i zadania",
      "- zadaj zwykłe pytanie o inicjatywę, repo albo dokumenty",
      '- wyślij "Pomysl: ..." albo "Uwaga: ...", jeśli chcesz utworzyć zgłoszenie do GitHub Issues',
      "",
      "Jak zgłaszać modele i części (recykling / e-waste):",
      "- najprościej: wyślij sam model, np. \"Sonoff Basic R2\" albo \"HP LaserJet P1102\"",
      "- part number / oznaczenie układu: wyślij sam token, np. \"ATmega328P\", \"ESP8266EX\", \"TPS62160\"",
      "- możesz dopisać kontekst w 1 linijce, np. \"Model: <...> / PCB: <...>\" albo \"Part: <...>\"",
      "- zdjęcia: wyślij zdjęcie etykiety znamionowej (model/PN/SN) albo zbliżenie PCB z nadrukami; w opisie zdjęcia dopisz jeśli możesz model i/lub oznaczenia układów",
    ].join("\n");
  }

  return `Komenda: ${command}`;
}
