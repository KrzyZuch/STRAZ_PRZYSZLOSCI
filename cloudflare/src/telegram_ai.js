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
export function stripIssuePrefix(messageText) {
  if (typeof messageText !== "string") return null;
  const trimmed = messageText.trim();
  if (!trimmed) return null;

  const matchers = [
    { kind: "idea", label: "pomysł", pattern: /^\s*(zapisz\s+pomysl|zapisz\s+pomysł|dopisz\s+pomysl|dopisz\s+pomysł|pomysl|pomysł)\s*[:\s]\s*/iu },
    { kind: "feedback", label: "uwaga", pattern: /^\s*(zapisz\s+uwage|zapisz\s+uwagę|dopisz\s+uwage|dopisz\s+uwagę|uwaga|uwagę|zastrzezenie|zastrzeżenie)\s*[:\s]\s*/iu },
  ];

  for (const matcher of matchers) {
    if (matcher.pattern.test(trimmed)) {
      const content = trimmed.replace(matcher.pattern, "").trim();
      if (!content) return null;
      return { kind: matcher.kind, label: matcher.label, content, original_text: trimmed };
    }
  }
  return null;
}

export function isCommand(text) {
  const match = String(text || "").trim().match(/^\/([a-z_]+)\b/i);
  return match ? match[1].toLowerCase() : null;
}

export function hasTelegramFile(message) {
  return Boolean(message && typeof message === "object" && message.file_id);
}

export function looksLikeStructuredCatalogToken(token) {
  const trimmed = String(token || "").replace(/^[^\p{Letter}\p{Number}]+|[^\p{Letter}\p{Number}]+$/gu, "");
  if (trimmed.length < 4 || trimmed.length > 40) return false;
  const hasLetter = /\p{Letter}/u.test(trimmed);
  const hasDigit = /\d/u.test(trimmed);
  const hasSeparator = /[-_/]/.test(trimmed);
  return hasLetter && (hasDigit || hasSeparator);
}

export function isDeviceLookupQuery(text) {
  const rawText = String(text || "").trim();
  if (!rawText) return false;

  const normalized = normalizeForSearch(rawText);
  const lookupHints = [
    "jakie czesci", "jakie części", "co jest w", "co siedzi w",
    "jaki uklad", "jaki układ", "jaki chip", "numer seryjny",
    "serial", "part number", "numer czesci", "numer części",
    "oznaczenie ukladu", "oznaczenie układu", "dawca", "donor", "model",
  ];
  if (lookupHints.some((phrase) => normalized.includes(normalizeForSearch(phrase)))) return true;

  const tokens = rawText.split(/\s+/).filter(Boolean);
  if (tokens.length <= 6 && tokens.some(looksLikeStructuredCatalogToken)) return true;

  return false;
}

export function routeTelegramIntent(message) {
  const messageText = getMessageText(message);
  const command = isCommand(messageText);
  if (command) return { intent: "command", command };

  if (hasTelegramFile(message)) {
    if (message.mime_type === "application/pdf") return { intent: "datasheet_analysis" };
    const text = (message.text || message.caption || "").toLowerCase();
    if (text.includes("rezystor") || text.includes("resistor")) return { intent: "resistor_reader" };
    return { intent: "device_media" };
  }

  const classification = stripIssuePrefix(messageText);
  if (classification) return { intent: "issue", classification };

  if (isOnboardingQuery(messageText)) return { intent: "onboarding" };

  if (isDeviceLookupQuery(messageText)) return { intent: "device_lookup" };

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
