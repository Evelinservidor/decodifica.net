import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from buttondown_send_weekly import extract_preheader, open_checklist_items, reader_body, write_summary


class WeeklyNewsletterTests(unittest.TestCase):
    def test_reader_body_excludes_operational_sections(self):
        text = "Hola\n\n## Fuentes revisadas\n- fuente\n\n## Checklist antes de enviar\n- [x] listo"
        self.assertEqual(reader_body(text), "Hola")

    def test_open_checklist_items_only_returns_pending(self):
        text = "- [x] resuelto\n- [ ] falta enlace\n"
        self.assertEqual(open_checklist_items(text), ["falta enlace"])

    def test_preheader_must_be_checked(self):
        self.assertEqual(extract_preheader("- [x] Preheader usado: Resumen util"), "Resumen util")
        self.assertIsNone(extract_preheader("- [ ] Preheader sugerido: Pendiente"))

    def test_summary_is_sanitized_and_matches_control_tower_contract(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "weekly.json"
            write_summary(
                path,
                ok=True,
                status="sent",
                execute=True,
                sent=True,
                audience=1,
                failures=[],
            )
            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(payload["schema_version"], "decodifica-newsletter-weekly-1.0")
            self.assertTrue(payload["sent"])
            self.assertFalse(payload["contains_personal_data"])
            self.assertNotIn("subject", payload)
            self.assertNotIn("body", payload)


if __name__ == "__main__":
    unittest.main()
