#!/usr/bin/env python3
"""
Weekly GSC report for decodifica.net.

Refreshes OAuth access token, queries Search Analytics for the last N days
(current vs previous period for deltas), formats a Markdown summary and
sends it to Telegram.

Required env vars (set as GitHub Actions secrets):
  GSC_REFRESH_TOKEN  - Long-lived refresh token from OAuth flow
  GSC_CLIENT_ID      - OAuth Client ID (same project as the refresh token)
  GSC_CLIENT_SECRET  - OAuth Client Secret
  GSC_SITE_URL       - Site URL in GSC format: "sc-domain:decodifica.net" or "https://decodifica.net/"
  TELEGRAM_BOT_TOKEN - Bot token from @BotFather
  TELEGRAM_CHAT_ID   - Target chat ID (Jordi: 555872211)
  DAYS_BACK          - (optional) days to look back, default 7
"""
from __future__ import annotations
import os
import sys
import json
import requests
from datetime import date, timedelta
from typing import Any

GSC_TOKEN_URL = "https://oauth2.googleapis.com/token"
GSC_SITES_URL = "https://www.googleapis.com/webmasters/v3/sites"
GSC_ANALYTICS_URL = (
    "https://www.googleapis.com/webmasters/v3/sites/{site}/searchAnalytics/query"
)
TG_API = "https://api.telegram.org/bot{token}/{method}"


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


def query_analytics(
    token: str, site: str, start: date, end: date, dimensions: list[str], row_limit: int = 25
) -> list[dict[str, Any]]:
    r = requests.post(
        GSC_ANALYTICS_URL.format(site=site),
        params={"access_token": token},
        json={
            "startDate": start.isoformat(),
            "endDate": end.isoformat(),
            "dimensions": dimensions,
            "rowLimit": row_limit,
        },
        timeout=30,
    )
    r.raise_for_status()
    return r.json().get("rows", []) or []


def aggregate(rows: list[dict[str, Any]]) -> dict[str, float]:
    return {
        "clicks": sum(r["clicks"] for r in rows),
        "impressions": sum(r["impressions"] for r in rows),
        "position_sum": sum(r["position"] * r["impressions"] for r in rows),
    }


def fmt_pct(curr: float, prev: float) -> str:
    if prev == 0:
        return "nuevo" if curr > 0 else "—"
    delta = (curr - prev) / prev * 100
    arrow = "↑" if delta > 0 else ("↓" if delta < 0 else "·")
    return f"{arrow} {abs(delta):.0f}%"


def build_report(days: int) -> str:
    token = get_access_token()
    site = os.environ.get("GSC_SITE_URL", "sc-domain:decodifica.net")

    today = date.today()
    end_curr = today - timedelta(days=3)  # GSC data has 2-3 day lag
    start_curr = end_curr - timedelta(days=days - 1)
    end_prev = start_curr - timedelta(days=1)
    start_prev = end_prev - timedelta(days=days - 1)

    print(f"Current period: {start_curr} -> {end_curr}", file=sys.stderr)
    print(f"Previous period: {start_prev} -> {end_prev}", file=sys.stderr)
    print(f"Site: {site}", file=sys.stderr)

    # Site-level totals
    curr_total_rows = query_analytics(token, site, start_curr, end_curr, ["date"], row_limit=days)
    prev_total_rows = query_analytics(token, site, start_prev, end_prev, ["date"], row_limit=days)
    curr = aggregate(curr_total_rows)
    prev = aggregate(prev_total_rows)

    # Top queries
    curr_queries = query_analytics(token, site, start_curr, end_curr, ["query"], row_limit=5)
    # Top pages
    curr_pages = query_analytics(token, site, start_curr, end_curr, ["page"], row_limit=5)

    avg_pos_curr = curr["position_sum"] / curr["impressions"] if curr["impressions"] else 0
    avg_pos_prev = prev["position_sum"] / prev["impressions"] if prev["impressions"] else 0
    ctr_curr = (curr["clicks"] / curr["impressions"] * 100) if curr["impressions"] else 0
    ctr_prev = (prev["clicks"] / prev["impressions"] * 100) if prev["impressions"] else 0

    lines = [
        f"*GSC weekly report — decodifica.net*",
        f"_{start_curr} → {end_curr} (vs {start_prev} → {end_prev})_",
        "",
        f"*Clicks:* {int(curr['clicks'])} ({fmt_pct(curr['clicks'], prev['clicks'])})",
        f"*Impressions:* {int(curr['impressions'])} ({fmt_pct(curr['impressions'], prev['impressions'])})",
        f"*CTR:* {ctr_curr:.1f}% (antes {ctr_prev:.1f}%)",
        f"*Avg pos:* {avg_pos_curr:.1f} (antes {avg_pos_prev:.1f})",
        "",
        "*Top 5 queries:*",
    ]
    if curr_queries:
        for r in curr_queries[:5]:
            lines.append(f"  - `{r['keys'][0]}` — {r['clicks']} clicks, pos {r['position']:.1f}")
    else:
        lines.append("  _(sin datos todavía)_")

    lines += ["", "*Top 5 pages:*"]
    if curr_pages:
        for r in curr_pages[:5]:
            lines.append(f"  - `{r['keys'][0]}` — {r['clicks']} clicks, {r['impressions']} impr")
    else:
        lines.append("  _(sin datos todavía)_")

    return "\n".join(lines)


def send_telegram(text: str) -> None:
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    r = requests.post(
        TG_API.format(token=token, method="sendMessage"),
        json={
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "Markdown",
            "disable_web_page_preview": True,
        },
        timeout=30,
    )
    r.raise_for_status()
    print(f"Telegram: {r.json()}", file=sys.stderr)


def main() -> int:
    days = int(os.environ.get("DAYS_BACK", "7"))
    try:
        report = build_report(days)
    except requests.HTTPError as e:
        # Save the error to a file so the workflow step can upload it
        with open("gsc-report.txt", "w", encoding="utf-8") as f:
            f.write(f"GSC API error: {e}\nResponse: {e.response.text if e.response else ''}")
        print(f"GSC API error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        with open("gsc-report.txt", "w", encoding="utf-8") as f:
            f.write(f"Error building report: {e!r}")
        print(f"Error: {e!r}", file=sys.stderr)
        return 1

    # Always save the report (debug artifact)
    with open("gsc-report.txt", "w", encoding="utf-8") as f:
        f.write(report)
    print(report, file=sys.stderr)

    # Only send to Telegram if there's actual data OR if it's the first run
    has_data = "_(sin datos todavía)_" not in report
    if has_data or os.environ.get("FORCE_SEND", "").lower() in ("1", "true"):
        try:
            send_telegram(report)
        except Exception as e:
            print(f"Telegram send failed (report saved): {e!r}", file=sys.stderr)
            return 2
    else:
        print("Skipping Telegram send: no data yet (first run or very new site)", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
