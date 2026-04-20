import { knowledgeBundle } from "./generated_knowledge_bundle.js";
import { normalizeForSearch, tokenize, parsePositiveInteger, parseNumber, normalizeWhitespace, toIsoNow, repoBlobUrl, buildPromptPayload } from "./base_utils.js";
import { sanitizeTelegramReply, getMainMenuKeyboard } from "./telegram_utils.js";
import { callProviderWithFallback } from "./ai_providers.js";

const ISSUE_DECISIONS = new Set(["accept", "reject_spam", "reject_abuse", "reject_too_short", "reject_off_topic"]);

function selectRelevantSections(query, limit = 4) {
  const queryTokens = tokenize(query);
  const sections = knowledgeBundle.sections || [];
  return sections
    .map((section) => ({
      ...section,
      score: scoreOverlap(queryTokens, `${section.title} ${section.content}`) + (section.source_path.includes("ARCHITEKTURA_ONBOARDINGU") ? 1 : 0),
    }))
    .sort((left, right) => right.score - left.score || left.title.localeCompare(right.title, "pl"))
    .filter((section, index) => section.score > 0 || index < limit)
    .slice(0, limit);
}

function scoreOverlap(queryTokens, text) {
  const textTokens = new Set(tokenize(text));
  let score = 0;
  for (const token of queryTokens) {
    if (textTokens.has(token)) score += 1;
  }
  return score;
}

function formatKnowledgeContext(sections) {
  return sections.map((section) => `### ${section.title}\nŹródło: ${section.source_path}\n${section.content}`).join("\n\n");
}

function buildHistoryContext(history) {
  if (!history.length) return "Brak wcześniejszej historii rozmowy.";
  return history.map((item) => `${item.role === "user" ? "Użytkownik" : "Asystent"}: ${item.message_text}`).join("\n");
}

function buildCommonKnowledgeIntro(query, history) {
  const sections = selectRelevantSections(query, 4);
  const docsList = (knowledgeBundle.documents || [])
    .filter((doc) => doc.path.startsWith("PROJEKTY/") || doc.path.startsWith("docs/") || doc.path === "README.md")
    .map((doc) => `- ${doc.title} (${doc.path})`)
    .join("\n");

  return [
    "### PUBLICZNA WIEDZA Z REPOZYTORIUM",
    `Baza adresów: ${knowledgeBundle.github_base_url}`,
    "### SPIS DOSTĘPNYCH DOKUMENTÓW I PROJEKTÓW:",
    docsList, "", formatKnowledgeContext(sections), "", "### HISTORIA ROZMOWY", buildHistoryContext(history)
  ].join("\n");
}

export async function generateChatReply(env, message, history = [], options = {}) {
  const response = await callProviderWithFallback(env, buildPromptPayload(
    "Jesteś asystentem AI Straży Przyszłości. Odpowiadaj po polsku.",
    [buildCommonKnowledgeIntro(message.text, history), "", "### PYTANIE UŻYTKOWNIKA", message.text].join("\n"),
    env, { maxTokens: 900, temperature: 0.35 }
  ), options);

  return {
    reply_text: sanitizeTelegramReply(response.text, env),
    reply_markup: getMainMenuKeyboard(),
    provider_name: response.provider_name, model_name: response.model_name,
  };
}

export async function moderateIssueCandidate(env, classification, message, history = [], options = {}) {
  const userPrompt = [
    buildCommonKnowledgeIntro(classification.content, history.slice(-4)), "",
    "### WIADOMOŚĆ DO OCENY", `Typ: ${classification.label}`, `Treść: ${classification.content}`, "",
    "Zwróć wyłącznie JSON z polami decision, reason_code, reason_text."
  ].join("\n");

  const response = await callProviderWithFallback(env, buildPromptPayload(
    "Tryb: moderacja zgłoszenia. Decision: accept, reject_spam, reject_abuse, reject_too_short, reject_off_topic.",
    userPrompt, env, { maxTokens: 300, temperature: 0.1 }
  ), options);

  const parsed = JSON.parse(response.text); // Simplified, should use extractJsonObject
  return {
    decision: parsed.decision || "accept",
    reason_code: parsed.reason_code || "ok",
    reason_text: parsed.reason_text || "Zaakceptowano.",
    provider_name: response.provider_name, model_name: response.model_name,
    chat_id: message.chat_id, user_id: message.user_id, message_id: message.message_id,
    issue_kind: classification.kind, original_text: classification.content,
  };
}

export async function draftIssueBody(env, classification, history = [], options = {}) {
  const response = await callProviderWithFallback(env, buildPromptPayload(
    "Tryb: redakcja treści GitHub Issue. Zwróć JSON z polami edited_description i additional_context.",
    [buildCommonKnowledgeIntro(classification.content, history.slice(-4)), "", "### ZGŁOSZENIE", `Typ: ${classification.label}`, `Treść: ${classification.content}`].join("\n"),
    env, { maxTokens: 500, temperature: 0.4 }
  ), options);

  const parsed = JSON.parse(response.text);
  return {
    edited_description: parsed.edited_description || classification.content,
    additional_context: parsed.additional_context || "",
    provider_name: response.provider_name, model_name: response.model_name,
  };
}
