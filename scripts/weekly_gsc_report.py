#!/usr/bin/env python3
"""
Weekly GSC fetcher for decodifica.net + 4 blogspot sites.

Refreshes OAuth access token, queries Search Analytics for the last N days
(current period vs previous period for deltas), aggregates by query, page,
date and country. Saves raw + aggregated data as JSON to disk for downstream
analysis (the seo-data-analyst skill consumes it).

Required env vars (set as GitHub Actions secrets):
  GSC_REFRESH_TOKEN  - Long-lived refresh token from OAuth flow
  GSC_CLIENT_ID      - OAuth Client ID (same project as the refresh token)
  GSC_CLIENT_SECRET  - OAuth Client Secret
  GSC_SITE_URLS      - Comma-separated list of site URLs in GSC format
                       e.g. "sc-domain:decodifica.net,https://drulenterror.blogspot.com/"
  DAYS_BACK          - (optional) days to look back, default 7
  OUTPUT_DIR         - (optional) where to write the JSON/MD outputs
                       default: /tmp/gsc_weekly (CI) or ./data/gsc_weekly (local)
"""
from __future__ import annotations
import os
import sys
import json
import requests
from datetime import date, timedelta
from pathlib import Path
from typing import Any

GSC_TOKEN_URL = "https://oauth2.googleapis.com/token"
GSC_SITES_URL = "https://www.googleapis.com/webmasters/v3/sites"
GSC_ANALYTICS_URL = (
    "https://www.googleapis.com/webmasters/v3/sites/{site}/searchAnalytics/query"
)


def get_access_token() -> str:
    r = requests.post(
        GSC_TOKEN_URL,
        data={
            "client_id": os.environ["GSC_CLIENT_ID"],
            "client_secret": os.environ["GSC_CLIENT_SECRET"],
            "refresh_token": os.environ["GSC_REFRESH_TOKEN"],
            "grant_type": "refresh_token",
        },
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["access_token"]


def list_sites(token: str) -> list[dict[str, Any]]:
    r = requests.get(
        GSC_SITES_URL,
        params={"access_token": token},
        timeout=30,
    )
    r.raise_for_status()
    return r.json().get("siteEntry", [])


def query_analytics(
    token: str,
    site: str,
    start: date,
    end: date,
    dimensions: list[str],
    row_limit: int = 1000,
) -> list[dict[str, Any]]:
    """Query GSC for a single site + date range. Handles pagination (max 25k rows per call).

    GSC requires the siteUrl in the path to be URL-encoded:
      sc-domain:foo.com       -> sc-domain%3Afoo.com
      https://foo.com/        -> https%3A%2F%2Ffoo.com%2F
    Using requests' params= would put it in the query string; instead we
    manually URL-encode the path segment with urllib.parse.quote.
    """
    from urllib.parse import quote
    encoded_site = quote(site, safe="")
    url = f"https://www.googleapis.com/webmasters/v3/sites/{encoded_site}/searchAnalytics/query"

    rows: list[dict[str, Any]] = []
    start_row = 0
    while True:
        r = requests.post(
            url,
            params={"access_token": token},
            json={
                "startDate": start.isoformat(),
                "endDate": end.isoformat(),
                "dimensions": dimensions,
                "rowLimit": min(row_limit, 25000),
                "startRow": start_row,
            },
            timeout=60,
        )
        r.raise_for_status()
        batch = r.json().get("rows", []) or []
        rows.extend(batch)
        if len(batch) < 25000 or len(rows) >= row_limit:
            break
        start_row += len(batch)
    return rows


def aggregate(rows: list[dict[str, Any]]) -> dict[str, float]:
    return {
        "clicks": sum(r["clicks"] for r in rows),
        "impressions": sum(r["impressions"] for r in rows),
        "position_impressions_sum": sum(r["position"] * r["impressions"] for r in rows),
    }


def build_site_payload(token: str, site: str, days: int) -> dict[str, Any]:
    """Build the full data payload for a single site."""
    today = date.today()
    end_curr = today - timedelta(days=3)  # GSC data lag = 2-3 days
    start_curr = end_curr - timedelta(days=days - 1)
    end_prev = start_curr - timedelta(days=1)
    start_prev = end_prev - timedelta(days=days - 1)

    # Site-level totals (date dimension for daily granularity)
    curr_total = query_analytics(token, site, start_curr, end_curr, ["date"], row_limit=days)
    prev_total = query_analytics(token, site, start_prev, end_prev, ["date"], row_limit=days)
    curr = aggregate(curr_total)
    prev = aggregate(prev_total)

    # By query (the most actionable dimension)
    curr_queries = query_analytics(token, site, start_curr, end_curr, ["query"], row_limit=1000)
    prev_queries = query_analytics(token, site, start_prev, end_prev, ["query"], row_limit=1000)

    # By page
    curr_pages = query_analytics(token, site, start_curr, end_curr, ["page"], row_limit=500)
    prev_pages = query_analytics(token, site, start_prev, end_prev, ["page"], row_limit=500)

    # By country
    curr_countries = query_analytics(token, site, start_curr, end_curr, ["country"], row_limit=100)

    # By device
    curr_devices = query_analytics(token, site, start_curr, end_curr, ["device"], row_limit=10)

    return {
        "site": site,
        "period": {
            "current": {"start": start_curr.isoformat(), "end": end_curr.isoformat()},
            "previous": {"start": start_prev.isoformat(), "end": end_prev.isoformat()},
        },
        "totals": {
            "current": curr,
            "previous": prev,
            "ctr_current": (curr["clicks"] / curr["impressions"] * 100) if curr["impressions"] else 0,
            "ctr_previous": (prev["clicks"] / prev["impressions"] * 100) if prev["impressions"] else 0,
            "avg_position_current": (
                curr["position_impressions_sum"] / curr["impressions"] if curr["impressions"] else 0
            ),
            "avg_position_previous": (
                prev["position_impressions_sum"] / prev["impressions"] if prev["impressions"] else 0
            ),
        },
        "queries": {
            "current": [
                {
                    "query": r["keys"][0],
                    "clicks": r["clicks"],
                    "impressions": r["impressions"],
                    "ctr": r["ctr"],
                    "position": r["position"],
                }
                for r in curr_queries
            ],
            "previous": [
                {
                    "query": r["keys"][0],
                    "clicks": r["clicks"],
                    "impressions": r["impressions"],
                    "ctr": r["ctr"],
                    "position": r["position"],
                }
                for r in prev_queries
            ],
        },
        "pages": {
            "current": [
                {
                    "page": r["keys"][0],
                    "clicks": r["clicks"],
                    "impressions": r["impressions"],
                    "ctr": r["ctr"],
                    "position": r["position"],
                }
                for r in curr_pages
            ],
            "previous": [
                {
                    "page": r["keys"][0],
                    "clicks": r["clicks"],
                    "impressions": r["impressions"],
                    "ctr": r["ctr"],
                    "position": r["position"],
                }
                for r in prev_pages
            ],
        },
        "countries": [
            {
                "country": r["keys"][0],
                "clicks": r["clicks"],
                "impressions": r["impressions"],
            }
            for r in curr_countries
        ],
        "devices": [
            {
                "device": r["keys"][0],
                "clicks": r["clicks"],
                "impressions": r["impressions"],
            }
            for r in curr_devices
        ],
        "daily": [
            {
                "date": r["keys"][0],
                "clicks": r["clicks"],
                "impressions": r["impressions"],
                "position": r["position"],
            }
            for r in curr_total
        ],
    }


def main() -> int:
    days = int(os.environ.get("DAYS_BACK", "7"))
    sites_str = os.environ.get(
        "GSC_SITE_URLS",
        "sc-domain:decodifica.net,"
        "https://drulenterror.blogspot.com/,"
        "https://calm-mind-meditation-souns.blogspot.com/,"
        "https://pergaminosprohibidos.blogspot.com/,"
        "https://jc-automation-n8n.blogspot.com/",
    )

    def normalize(site: str) -> str:
        s = site.strip()
        if not s:
            return s
        if s.startswith("sc-domain:"):
            return s  # sc-domain:foo.com (no trailing slash)
        if s.startswith("http://") or s.startswith("https://"):
            return s if s.endswith("/") else s + "/"
        return s

    sites = [normalize(s) for s in sites_str.split(",") if s.strip()]

    output_dir = Path(
        os.environ.get(
            "OUTPUT_DIR",
            "/tmp/gsc_weekly" if os.environ.get("GITHUB_ACTIONS") else "./data/gsc_weekly",
        )
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    today_str = date.today().isoformat()

    print(f"Fetching GSC data for {len(sites)} sites, last {days} days", file=sys.stderr)
    print(f"Output dir: {output_dir}", file=sys.stderr)

    token = get_access_token()

    # Optional: verify all sites exist for the user
    available = {s["siteUrl"] for s in list_sites(token)}
    print(f"Sites available in GSC: {sorted(available)}", file=sys.stderr)

    results: dict[str, Any] = {
        "fetched_at": today_str,
        "days": days,
        "sites_requested": sites,
        "sites_available": sorted(available),
        "per_site": {},
    }

    for site in sites:
        if site not in available:
            print(f"SKIP {site}: not in GSC or no access", file=sys.stderr)
            results["per_site"][site] = {"error": "not_in_gsc_or_no_access"}
            continue
        try:
            print(f"Fetching {site}...", file=sys.stderr)
            payload = build_site_payload(token, site, days)
            results["per_site"][site] = payload
            total_curr = payload["totals"]["current"]
            total_prev = payload["totals"]["previous"]
            print(
                f"  clicks={total_curr['clicks']:.0f} (prev={total_prev['clicks']:.0f}) "
                f"impressions={total_curr['impressions']:.0f} "
                f"queries={len(payload['queries']['current'])} "
                f"pages={len(payload['pages']['current'])}",
                file=sys.stderr,
            )
        except Exception as e:
            print(f"  ERROR: {e!r}", file=sys.stderr)
            results["per_site"][site] = {"error": repr(e)}

    # Write the combined JSON
    output_json = output_dir / f"{today_str}_gsc_weekly.json"
    output_json.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {output_json}", file=sys.stderr)

    # Write a quick-look summary markdown (per-site totals + deltas)
    first_period = ""
    if sites:
        first = results["per_site"].get(sites[0], {})
        if "period" in first:
            curr_p = first["period"]["current"]
            prev_p = first["period"]["previous"]
            first_period = f"Current: {curr_p['start']} → {curr_p['end']}  |  Previous: {prev_p['start']} → {prev_p['end']}"

    md_lines = [
        f"# GSC Weekly Summary — {today_str}",
        "",
        f"_{first_period}_",
        f"Sites: {len(sites)} requested, {len([s for s,v in results['per_site'].items() if 'error' not in v])} fetched OK",
        "",
        "| Site | Clicks | Clicks Δ | Impressions | Impr Δ | CTR | Avg Pos |",
        "|---|---|---|---|---|---|---|",
    ]
    for site in sites:
        data = results["per_site"].get(site, {})
        if "error" in data:
            md_lines.append(f"| {site} | ERROR | — | — | — | — | — |")
            continue
        t = data["totals"]
        curr = t["current"]
        prev = t["previous"]
        clicks_delta = curr["clicks"] - prev["clicks"]
        imp_delta = curr["impressions"] - prev["impressions"]
        md_lines.append(
            f"| {site} | {curr['clicks']:.0f} | {clicks_delta:+.0f} | "
            f"{curr['impressions']:.0f} | {imp_delta:+.0f} | "
            f"{t['ctr_current']:.1f}% | {t['avg_position_current']:.1f} |"
        )
    md_text = "\n".join(md_lines)
    output_md = output_dir / f"{today_str}_gsc_summary.md"
    output_md.write_text(md_text, encoding="utf-8")
    print(f"Wrote {output_md}", file=sys.stderr)

    # Also write a "latest" symlink-like file for easy access
    latest_json = output_dir / "latest.json"
    latest_md = output_dir / "latest.md"
    latest_json.write_text(output_json.read_text(encoding="utf-8"), encoding="utf-8")
    latest_md.write_text(md_text, encoding="utf-8")

    return 0


if __name__ == "__main__":
    sys.exit(main())
