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
export function buildCommandReply(cmd) { return `Komenda: ${cmd}`; }
