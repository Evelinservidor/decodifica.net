#!/usr/bin/env python3
from __future__ import annotations

import ssl
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import MagicMock, patch

from web_health_check import (
    built_page_route,
    collect_built_discovery_resources,
    collect_built_internal_paths,
    discovery_resource_content_ok,
    fetch_url,
    load_public_env,
    normalize_internal_path,
)


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

    def test_collects_advertised_and_required_discovery_resources(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo = Path(temp_dir)
            dist = repo / "dist"
            page = dist / "index.html"
            page.parent.mkdir(parents=True)
            page.write_text(
                '<link rel="alternate" type="application/rss+xml" href="/feed.xml">'
                '<link rel="icon" href="/favicon.svg">',
                encoding="utf-8",
            )

            resources = collect_built_discovery_resources(repo, "https://decodifica.net")
            keys = {(item["path"], item["kind"]) for item in resources}
            self.assertIn(("/feed.xml", "rss"), keys)
            self.assertIn(("/rss.xml", "rss"), keys)
            self.assertIn(("/favicon.svg", "icon"), keys)
            self.assertIn(("/favicon.ico", "icon"), keys)

    def test_validates_discovery_resource_content_types(self) -> None:
        self.assertTrue(discovery_resource_content_ok("rss", "application/rss+xml"))
        self.assertTrue(discovery_resource_content_ok("icon", "image/x-icon"))
        self.assertFalse(discovery_resource_content_ok("rss", "text/html"))

class WebHealthFetchTests(unittest.TestCase):
    @staticmethod
    def successful_response() -> MagicMock:
        response = MagicMock()
        response.status = 200
        response.read.return_value = b"<html>ok</html>"
        response.headers.get_content_type.return_value = "text/html"
        response.headers.get_content_charset.return_value = "utf-8"
        response.__enter__.return_value = response
        return response

    def test_retries_transient_tls_error_then_recovers(self) -> None:
        transient = urllib.error.URLError(ssl.SSLError("temporary TLS decode error"))
        with (
            patch("web_health_check.urllib.request.urlopen", side_effect=[transient, self.successful_response()]) as urlopen,
            patch("web_health_check.time.sleep") as sleep,
        ):
            result = fetch_url("https://decodifica.net/login", attempts=3, retry_backoff_seconds=0.01)

        self.assertTrue(result["ok"])
        self.assertEqual(result["attempts"], 2)
        self.assertEqual(urlopen.call_count, 2)
        sleep.assert_called_once_with(0.01)

    def test_reports_failure_after_transient_attempts_are_exhausted(self) -> None:
        transient = urllib.error.URLError("temporary network failure")
        with (
            patch("web_health_check.urllib.request.urlopen", side_effect=transient) as urlopen,
            patch("web_health_check.time.sleep") as sleep,
        ):
            result = fetch_url("https://decodifica.net/login", attempts=3, retry_backoff_seconds=0.01)

        self.assertFalse(result["ok"])
        self.assertEqual(result["attempts"], 3)
        self.assertEqual(urlopen.call_count, 3)
        self.assertEqual(sleep.call_count, 2)

    def test_does_not_retry_permanent_http_error(self) -> None:
        permanent = urllib.error.HTTPError(
            "https://decodifica.net/missing",
            404,
            "Not Found",
            hdrs=None,
            fp=None,
        )
        with (
            patch("web_health_check.urllib.request.urlopen", side_effect=permanent) as urlopen,
            patch("web_health_check.time.sleep") as sleep,
        ):
            result = fetch_url("https://decodifica.net/missing", attempts=3)

        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], 404)
        self.assertEqual(result["attempts"], 1)
        self.assertEqual(urlopen.call_count, 1)
        sleep.assert_not_called()


if __name__ == "__main__":
    unittest.main()
