-- Migration: 0007_telegram_sessions_add_name.sql
-- Description: Add active_device_name to sessions for handling unknown devices

ALTER TABLE telegram_user_sessions ADD COLUMN active_device_name TEXT;
