-- Migration: 0009_fts5_recycled_devices.sql
-- Description: Create FTS5 virtual table for recycled_devices and recycled_device_aliases to optimize search.

-- 1. Create the virtual table
CREATE VIRTUAL TABLE IF NOT EXISTS recycled_devices_fts USING fts5(
    model,
    brand,
    alias,
    content='recycled_devices',
    content_rowid='id'
);

-- 2. Populate the virtual table from existing data
-- Note: This is tricky with content_rowid if aliases are in a separate table.
-- We might want a dedicated FTS table that we manage manually with triggers.

-- Actually, let's use a simpler FTS table without content='recycled_devices' 
-- if we want to index aliases too, or manage it manually.

DROP TABLE IF EXISTS recycled_devices_fts;
CREATE VIRTUAL TABLE recycled_devices_fts USING fts5(
    device_id UNINDEXED,
    model,
    brand,
    alias
);

-- Initial population
INSERT INTO recycled_devices_fts (device_id, model, brand, alias)
SELECT 
    d.id, 
    d.model, 
    COALESCE(d.brand, ''), 
    COALESCE(GROUP_CONCAT(a.alias, ' '), '')
FROM recycled_devices d
LEFT JOIN recycled_device_aliases a ON a.device_id = d.id
GROUP BY d.id;

-- 3. Triggers to keep FTS in sync

-- Trigger for new devices
CREATE TRIGGER IF NOT EXISTS recycled_devices_ai AFTER INSERT ON recycled_devices BEGIN
  INSERT INTO recycled_devices_fts (device_id, model, brand, alias)
  VALUES (new.id, new.model, COALESCE(new.brand, ''), '');
END;

-- Trigger for device updates
CREATE TRIGGER IF NOT EXISTS recycled_devices_au AFTER UPDATE ON recycled_devices BEGIN
  UPDATE recycled_devices_fts 
  SET model = new.model, brand = COALESCE(new.brand, '')
  WHERE device_id = new.id;
END;

-- Trigger for device deletion
CREATE TRIGGER IF NOT EXISTS recycled_devices_ad AFTER DELETE ON recycled_devices BEGIN
  DELETE FROM recycled_devices_fts WHERE device_id = old.id;
END;

-- Trigger for new aliases
CREATE TRIGGER IF NOT EXISTS recycled_device_aliases_ai AFTER INSERT ON recycled_device_aliases BEGIN
  UPDATE recycled_devices_fts 
  SET alias = (
    SELECT COALESCE(GROUP_CONCAT(alias, ' '), '') 
    FROM recycled_device_aliases 
    WHERE device_id = new.device_id
  )
  WHERE device_id = new.device_id;
END;

-- Trigger for alias updates
CREATE TRIGGER IF NOT EXISTS recycled_device_aliases_au AFTER UPDATE ON recycled_device_aliases BEGIN
  UPDATE recycled_devices_fts 
  SET alias = (
    SELECT COALESCE(GROUP_CONCAT(alias, ' '), '') 
    FROM recycled_device_aliases 
    WHERE device_id = new.device_id
  )
  WHERE device_id = new.device_id;
END;

-- Trigger for alias deletions
CREATE TRIGGER IF NOT EXISTS recycled_device_aliases_ad AFTER DELETE ON recycled_device_aliases BEGIN
  UPDATE recycled_devices_fts 
  SET alias = (
    SELECT COALESCE(GROUP_CONCAT(alias, ' '), '') 
    FROM recycled_device_aliases 
    WHERE device_id = old.device_id
  )
  WHERE device_id = old.device_id;
END;
