import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from pipelines.sync_recycled_queue import (
    Submission,
    apply_queue_to_devices,
    infer_brand_model,
    load_jsonl,
    parse_json_payload_from_wrangler,
)


class SyncRecycledQueueTests(unittest.TestCase):
    def test_parse_json_payload_from_wrangler_with_noise(self) -> None:
        output = """
npm warn Unknown env config "devdir". This will stop working.

 ⛅️ wrangler 4.69.0
[
  {
    "results": [
      {
        "id": 7,
        "query_text": "Sonoff Basic"
      }
    ],
    "success": true
  }
]
"""
        payload = parse_json_payload_from_wrangler(output)
        self.assertIsInstance(payload, list)
        self.assertEqual(payload[0]["results"][0]["id"], 7)

    def test_infer_brand_model_prefers_recognized_and_payload(self) -> None:
        submission = Submission(
            id=101,
            query_text="router wr740n",
            recognized_brand="TP-Link",
            recognized_model="TL-WR740N",
            attachment_file_id="",
            attachment_mime_type="",
            raw_payload_json={"brand": "Ignored", "model": "Ignored"},
            created_at="",
        )
        brand, model = infer_brand_model(submission)
        self.assertEqual(brand, "TP-Link")
        self.assertEqual(model, "TL-WR740N")

    def test_apply_queue_to_devices_adds_only_non_duplicates(self) -> None:
        with TemporaryDirectory() as temp_dir:
            devices_path = Path(temp_dir) / "devices.jsonl"
            devices_path.write_text(
                "\n".join(
                    [
                        json.dumps(
                            {
                                "device_slug": "sonoff-basic",
                                "brand": "Sonoff",
                                "model": "Basic",
                                "canonical_name": "Sonoff Basic",
                                "device_category": "smart_switch",
                                "description": "existing",
                                "known_aliases": [],
                                "serial_markers": [],
                                "donor_rank": 0.88,
                                "teardown_url": "",
                                "source_url": "",
                                "notes": "",
                            },
                            ensure_ascii=False,
                            separators=(",", ":"),
                        ),
                        ""
                    ]
                ),
                encoding="utf-8",
            )

            queued = [
                Submission(
                    id=1,
                    query_text="Sonoff Basic",
                    recognized_brand="Sonoff",
                    recognized_model="Basic",
                    attachment_file_id="",
                    attachment_mime_type="",
                    raw_payload_json={},
                    created_at="2026-04-15T00:00:00Z",
                ),
                Submission(
                    id=2,
                    query_text="HP LaserJet P1102",
                    recognized_brand="HP",
                    recognized_model="LaserJet P1102",
                    attachment_file_id="abc",
                    attachment_mime_type="image/jpeg",
                    raw_payload_json={"confidence": 0.77},
                    created_at="2026-04-15T00:01:00Z",
                ),
            ]

            new_devices, curated_ids, duplicate_ids = apply_queue_to_devices(
                queued,
                devices_path=devices_path,
            )

            self.assertEqual(len(new_devices), 1)
            self.assertEqual(curated_ids, [2])
            self.assertEqual(duplicate_ids, [1])

            devices = load_jsonl(devices_path)
            self.assertEqual(len(devices), 2)
            self.assertEqual(devices[-1]["brand"], "HP")
            self.assertEqual(devices[-1]["model"], "LaserJet P1102")
            self.assertEqual(devices[-1]["donor_rank"], 0.77)


if __name__ == "__main__":
    unittest.main()
