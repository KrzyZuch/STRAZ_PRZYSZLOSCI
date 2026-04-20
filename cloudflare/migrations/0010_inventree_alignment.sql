-- Migration: 0010_inventree_alignment.sql
-- Description: Align database schema with InvenTree and Ki-nTree specifications for ecoEDA compatibility

-- Add InvenTree specific fields to recycled_parts
ALTER TABLE recycled_parts ADD COLUMN ipn TEXT; -- Internal Part Number for InvenTree
ALTER TABLE recycled_parts ADD COLUMN category TEXT; -- Mapped to InvenTree Category (e.g., Capacitor, Resistor)
ALTER TABLE recycled_parts ADD COLUMN parameters TEXT; -- JSON string for dynamic InvenTree PartParameters
ALTER TABLE recycled_parts ADD COLUMN datasheet_file_id TEXT; -- Link to locally downloaded/cached PDF in Telegram
ALTER TABLE recycled_parts ADD COLUMN kicad_reference TEXT; -- Reference designator prefix for Ki-nTree (e.g., U, R, C)
ALTER TABLE recycled_parts ADD COLUMN stock_location TEXT; -- Specific sub-location within the donor device

-- Re-create the FTS5 virtual table to index the new metadata fields
DROP TABLE IF EXISTS recycled_devices_fts;
CREATE VIRTUAL TABLE recycled_devices_fts USING fts5(
    model, 
    brand, 
    description, 
    parts_list,
    tokenize="unicode61 remove_diacritics 1"
);

-- Re-populate the FTS5 table
INSERT INTO recycled_devices_fts(rowid, model, brand, description, parts_list)
SELECT 
    d.id, 
    d.model, 
    d.brand, 
    d.description,
    GROUP_CONCAT(p.part_name || ' ' || COALESCE(p.ipn, '') || ' ' || COALESCE(p.category, '') || ' ' || COALESCE(p.parameters, ''), ', ') as parts_list
FROM recycled_devices d
LEFT JOIN recycled_parts p ON d.id = p.device_id
GROUP BY d.id;
