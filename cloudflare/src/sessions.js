import { toIsoNow } from "./base_utils.js";

export async function upsertUserSession(env, chat_id, user_id, session_type, device_id, device_name = null) {
  const db = env.DB;
  const now = toIsoNow();
  await db.prepare(
    `
    INSERT INTO telegram_user_sessions (chat_id, user_id, session_type, active_device_id, active_device_name, status, created_at, updated_at)
    VALUES (?, ?, ?, ?, ?, 'active', ?, ?)
    ON CONFLICT(chat_id, user_id, session_type) DO UPDATE SET
      active_device_id = EXCLUDED.active_device_id,
      active_device_name = EXCLUDED.active_device_name,
      status = 'active',
      updated_at = EXCLUDED.updated_at
    `
  ).bind(chat_id, user_id, session_type, device_id, device_name, now, now).run();
}

export async function getUserSession(env, chat_id, user_id, session_type) {
  const db = env.DB;
  return await db.prepare(
    `SELECT * FROM telegram_user_sessions 
     WHERE chat_id = ? AND user_id = ? AND session_type = ? AND status = 'active'
     AND updated_at > datetime('now', '-1 hour')`
  ).bind(chat_id, user_id, session_type).first();
}

export async function closeUserSession(env, chat_id, user_id, session_type) {
  const db = env.DB;
  const now = toIsoNow();
  await db.prepare(
    `UPDATE telegram_user_sessions SET status = 'closed', updated_at = ? WHERE chat_id = ? AND user_id = ? AND session_type = ?`
  ).bind(now, chat_id, user_id, session_type).run();
}

export async function closeAllUserSessions(env, chat_id, user_id) {
  const db = env.DB;
  const now = toIsoNow();
  await db.prepare(
    `UPDATE telegram_user_sessions SET status = 'closed', updated_at = ? WHERE chat_id = ? AND user_id = ?`
  ).bind(now, chat_id, user_id).run();
}
