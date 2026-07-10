#!/usr/bin/env python3
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from web_health_check import built_page_route, collect_built_internal_paths, load_public_env, normalize_internal_path


class WebHealthLinkTests(unittest.TestCase):
    def test_loads_only_public_env_from_utf8_bom_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo = Path(temp_dir)
            (repo / ".env.local").write_text(
                "# Public values\nPUBLIC_SITE_URL=https://decodifica.net\nPRIVATE_TOKEN=do-not-load\n",
                encoding="utf-8-sig",
            )

            self.assertEqual(load_public_env(repo), {"PUBLIC_SITE_URL": "https://decodifica.net"})

    def test_normalizes_internal_links_and_drops_query_and_fragment(self) -> None:
        self.assertEqual(
            normalize_internal_path(
                "/lead-magnets/workflows-ia-dia-a-dia.pdf?download=1#page=1",
                "https://decodifica.net/recursos/",
                "https://decodifica.net",
            ),
            "/lead-magnets/workflows-ia-dia-a-dia.pdf",
        )

    def test_ignores_external_and_non_http_links(self) -> None:
        self.assertIsNone(
            normalize_internal_path(
                "https://buttondown.com/decodifica",
                "https://decodifica.net/",
                "https://decodifica.net",
            )
        )
        self.assertIsNone(normalize_internal_path("mailto:hola@decodifica.net", "https://decodifica.net/", "https://decodifica.net"))
        self.assertIsNone(normalize_internal_path("#newsletter", "https://decodifica.net/", "https://decodifica.net"))

    def test_maps_built_html_routes(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            dist = Path(temp_dir)
            self.assertEqual(built_page_route(dist / "index.html", dist), "/")
            self.assertEqual(built_page_route(dist / "recursos" / "index.html", dist), "/recursos/")

    def test_collects_root_relative_absolute_and_relative_links(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo = Path(temp_dir)
            dist = repo / "dist"
            page = dist / "recursos" / "index.html"
            page.parent.mkdir(parents=True)
            page.write_text(
                """
                <a href="/lead-magnets/workflows.pdf?download=1">PDF</a>
                <a href="../newsletter/">Newsletter</a>
                <a href="https://www.decodifica.net/herramientas/#top">Herramientas</a>
                <a href="https://example.com/external">External</a>
                """,
                encoding="utf-8",
            )

            self.assertEqual(
                collect_built_internal_paths(repo, "https://decodifica.net"),
                [
                    "/herramientas/",
                    "/lead-magnets/workflows.pdf",
                    "/newsletter/",
                ],
            )


if __name__ == "__main__":
    unittest.main()
