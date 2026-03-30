#!/usr/bin/env python3
"""
Morning Delivery Pipeline for Wealth System
Orchestrates 9AM content delivery via Telegram and Gmail.

Usage:
    python morning_delivery.py              # Generate and send today's morning content
    python morning_delivery.py --dry-run    # Preview without sending
    python morning_delivery.py --day 5      # Generate for specific day number
    python morning_delivery.py --date 2026-04-05  # Generate for specific date
    python morning_delivery.py --telegram-only     # Send only via Telegram
    python morning_delivery.py --email-only        # Send only via Gmail

Environment Variables:
    TELEGRAM_CHAT_ID   - Telegram chat ID for delivery
    GMAIL_RECIPIENT    - Email address for delivery
"""

import argparse
import json
import logging
import os
import subprocess
import sys
import time
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Optional

try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    print("ERROR: jinja2 is required. Install with: pip install jinja2", file=sys.stderr)
    sys.exit(1)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = BASE_DIR / "scripts"
CONTENT_DIR = BASE_DIR / "content"
GENERATED_DIR = CONTENT_DIR / "generated"
TEMPLATES_DIR = BASE_DIR / "templates"
DOMAIN_CONFIG_PATH = TEMPLATES_DIR / "domain_config.json"

REPO_ROOT = BASE_DIR.parent
TELEGRAM_SKILL = REPO_ROOT / "claude-config" / "skills" / "telegram" / "scripts" / "telegram.py"
GMAIL_SKILL = REPO_ROOT / "claude-config" / "skills" / "gmail" / "scripts" / "gmail.py"
CONTENT_GENERATOR = SCRIPTS_DIR / "content_generator.py"

START_DATE = date(2026, 3, 30)
TIMEZONE_NAME = "Australia/Canberra"

MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 5

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("morning_delivery")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def get_day_number(target_date: date) -> int:
    """Calculate day number (1-365) from the start date."""
    delta = (target_date - START_DATE).days + 1
    if delta < 1:
        logger.error("Date %s is before the start date %s", target_date, START_DATE)
        sys.exit(1)
    return delta


def get_week_number(day_number: int) -> int:
    """Get the week number (1-52) from the day number."""
    return ((day_number - 1) // 7) + 1


def load_json(path: Path) -> dict:
    """Load a JSON file."""
    if not path.exists():
        logger.error("File not found: %s", path)
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_domain_config() -> dict:
    """Load domain display configuration."""
    if DOMAIN_CONFIG_PATH.exists():
        return load_json(DOMAIN_CONFIG_PATH)
    return {}


# ---------------------------------------------------------------------------
# Content Generation / Loading
# ---------------------------------------------------------------------------


def generate_content(target_date: date, day_number: int) -> Optional[Path]:
    """Generate morning content using content_generator.py."""
    output_path = GENERATED_DIR / f"{target_date.isoformat()}-morning.json"

    if output_path.exists():
        logger.info("Morning content already exists: %s", output_path)
        return output_path

    logger.info("Generating morning content for day %d (%s)", day_number, target_date)
    cmd = [
        sys.executable, str(CONTENT_GENERATOR),
        "--day", str(day_number),
        "--session", "morning",
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode != 0:
            logger.error("Content generation failed: %s", result.stderr)
            return None
        logger.info("Content generated successfully")
    except subprocess.TimeoutExpired:
        logger.error("Content generation timed out")
        return None
    except Exception as exc:
        logger.error("Content generation error: %s", exc)
        return None

    if output_path.exists():
        return output_path

    logger.error("Expected output file not found: %s", output_path)
    return None


def load_content(target_date: date, day_number: int) -> Optional[dict]:
    """Load or generate morning content."""
    content_path = generate_content(target_date, day_number)
    if content_path is None:
        return None
    return load_json(content_path)


# ---------------------------------------------------------------------------
# Template Rendering
# ---------------------------------------------------------------------------


def get_template_vars(content: dict, domain_config: dict) -> dict:
    """Build template variables from content data."""
    domain = content.get("domain", "general")
    domain_info = domain_config.get(domain, {})

    # Prefer content-level display fields, fall back to domain_config
    domain_display = content.get("domain_display") or domain_info.get("display_name", domain.replace("_", " ").title())
    domain_emoji = content.get("domain_emoji") or domain_info.get("emoji", "")
    cultural_flag = content.get("cultural_flag") or domain_info.get("cultural_flags", {}).get("universal", "")

    business_apps = content.get("business_applications", {})

    return {
        "day_number": content.get("day_number", 0),
        "date_formatted": content.get("date", ""),
        "week_number": content.get("week", 1),
        "title": content.get("title", ""),
        "domain": domain,
        "domain_display": domain_display,
        "domain_emoji": domain_emoji,
        "complexity": content.get("complexity", "beginner"),
        "cultural_source": content.get("cultural_source", ""),
        "cultural_flag": cultural_flag,
        "content_body": content.get("content_body", ""),
        "exercise": content.get("exercise", ""),
        "business_cleaning": business_apps.get("cleaning", ""),
        "business_vibe_coding": business_apps.get("vibe_coding", ""),
        "business_agency": business_apps.get("agency", ""),
        "business_passive": business_apps.get("passive_income", ""),
        "quote": content.get("quote", ""),
        "quote_author": content.get("quote_author", ""),
        "source_name": content.get("source_name", ""),
    }


def render_telegram_message(content: dict, domain_config: dict) -> str:
    """Render morning content as Telegram Markdown message."""
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=False,
    )

    try:
        template = env.get_template("morning_telegram.md")
    except Exception as exc:
        logger.error("Failed to load morning Telegram template: %s", exc)
        return _fallback_telegram_format(content)

    template_vars = get_template_vars(content, domain_config)
    return template.render(**template_vars)


def render_email_html(content: dict, domain_config: dict) -> str:
    """Render morning content as HTML email."""
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=False,
    )

    try:
        template = env.get_template("email_daily.html")
    except Exception as exc:
        logger.error("Failed to load email template: %s", exc)
        return _fallback_email_format(content)

    template_vars = get_template_vars(content, domain_config)
    return template.render(**template_vars)


def _fallback_telegram_format(content: dict) -> str:
    """Fallback Telegram format if template fails."""
    day = content.get("day_number", "?")
    title = content.get("title", "Today's Lesson")
    body = content.get("content_body", "")
    quote = content.get("quote", "")
    author = content.get("quote_author", "")

    parts = [
        f"*Good morning, Paul.* Day {day} of your transformation.",
        "",
        f"*{title}*",
        "",
        body,
    ]
    if quote:
        parts.append("")
        parts.append(f'_"{quote}"_ -- {author}')

    return "\n".join(parts)


def _fallback_email_format(content: dict) -> str:
    """Fallback email format if template fails."""
    title = content.get("title", "Today's Lesson")
    body = content.get("content_body", "").replace("\n", "<br>")
    return f"<html><body><h1>{title}</h1><p>{body}</p></body></html>"


# ---------------------------------------------------------------------------
# Delivery: Telegram
# ---------------------------------------------------------------------------


def _get_bot_token() -> str:
    """Get bot token from env var or token file."""
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    if token:
        return token
    token_file = Path(os.path.expanduser("~/.claude/skills/telegram/token.json"))
    if token_file.exists():
        with open(token_file) as f:
            data = json.load(f)
        return data.get("bot_token", "")
    return ""


def _send_telegram_direct(message: str, chat_id: str, token: str) -> bool:
    """Send via Telegram Bot API directly (for GitHub Actions / CI)."""
    try:
        import httpx
        resp = httpx.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat_id, "text": message, "parse_mode": "Markdown"},
            timeout=15,
        )
        if resp.status_code == 200 and resp.json().get("ok"):
            return True
        logger.warning("Telegram API response: %s", resp.text[:200])
    except Exception as exc:
        logger.warning("Direct Telegram send failed: %s", exc)
    return False


def send_telegram(message: str, chat_id: str) -> bool:
    """Send message via Telegram with retry logic. Uses skill script or direct API."""
    token = _get_bot_token()
    use_direct = not TELEGRAM_SKILL.exists() or not TELEGRAM_SKILL.parent.exists()

    if not token and use_direct:
        logger.error("No bot token found and skill script unavailable")
        return False

    for attempt in range(1, MAX_RETRIES + 1):
        logger.info("Telegram send attempt %d/%d", attempt, MAX_RETRIES)

        if use_direct or token:
            if _send_telegram_direct(message, chat_id, token):
                logger.info("Telegram message sent successfully (direct API)")
                return True
        else:
            cmd = [
                sys.executable,
                str(TELEGRAM_SKILL),
                "send-message",
                chat_id,
                message,
                "--parse-mode", "Markdown",
            ]
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                if result.returncode == 0:
                    logger.info("Telegram message sent successfully (skill)")
                    return True
                logger.warning("Telegram send failed (exit %d): %s", result.returncode, result.stderr)
            except subprocess.TimeoutExpired:
                logger.warning("Telegram send timed out (attempt %d)", attempt)
            except Exception as exc:
                logger.warning("Telegram send error (attempt %d): %s", attempt, exc)

        if attempt < MAX_RETRIES:
            logger.info("Retrying in %d seconds...", RETRY_DELAY_SECONDS)
            time.sleep(RETRY_DELAY_SECONDS)

    logger.error("Telegram delivery failed after %d attempts", MAX_RETRIES)
    return False


# ---------------------------------------------------------------------------
# Delivery: Gmail
# ---------------------------------------------------------------------------


def send_gmail(html_body: str, subject: str, recipient: str) -> bool:
    """Send email via Gmail skill with retry logic."""
    if not GMAIL_SKILL.exists():
        logger.error("Gmail skill script not found: %s", GMAIL_SKILL)
        return False

    for attempt in range(1, MAX_RETRIES + 1):
        logger.info("Gmail send attempt %d/%d", attempt, MAX_RETRIES)
        cmd = [
            sys.executable,
            str(GMAIL_SKILL),
            "send",
            "--to", recipient,
            "--subject", subject,
            "--body", html_body,
            "--html",
        ]

        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=30,
            )
            if result.returncode == 0:
                response = json.loads(result.stdout) if result.stdout.strip() else {}
                if "error" not in response:
                    logger.info("Gmail message sent successfully")
                    return True
                logger.warning("Gmail API error: %s", response.get("error"))
            else:
                logger.warning("Gmail send failed (exit %d): %s", result.returncode, result.stderr)
        except subprocess.TimeoutExpired:
            logger.warning("Gmail send timed out (attempt %d)", attempt)
        except Exception as exc:
            logger.warning("Gmail send error (attempt %d): %s", attempt, exc)

        if attempt < MAX_RETRIES:
            logger.info("Retrying in %d seconds...", RETRY_DELAY_SECONDS)
            time.sleep(RETRY_DELAY_SECONDS)

    logger.error("Gmail delivery failed after %d attempts", MAX_RETRIES)
    return False


# ---------------------------------------------------------------------------
# Delivery Logging
# ---------------------------------------------------------------------------


def log_delivery(content: dict, telegram_ok: bool, email_ok: bool) -> None:
    """Log delivery status to delivery_log.json."""
    log_path = CONTENT_DIR / "delivery_log.json"

    log_entries = []
    if log_path.exists():
        try:
            with open(log_path, "r", encoding="utf-8") as f:
                log_entries = json.load(f)
        except (json.JSONDecodeError, IOError):
            log_entries = []

    entry = {
        "date": content.get("date", ""),
        "day_number": content.get("day_number", 0),
        "session": "morning",
        "title": content.get("title", ""),
        "domain": content.get("domain", ""),
        "telegram_sent": telegram_ok,
        "email_sent": email_ok,
        "delivered_at": datetime.now().isoformat(),
    }
    log_entries.append(entry)

    log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(log_entries, f, indent=2, ensure_ascii=False)

    logger.info("Delivery logged to %s", log_path)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Morning Delivery Pipeline - sends 9AM content via Telegram and Gmail"
    )
    parser.add_argument(
        "--day", type=int, default=None, metavar="N",
        help="Generate for a specific day number (1-365)",
    )
    parser.add_argument(
        "--date", type=str, default=None, metavar="YYYY-MM-DD",
        help="Generate for a specific date",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Preview content without sending",
    )
    parser.add_argument(
        "--telegram-only", action="store_true",
        help="Send only via Telegram",
    )
    parser.add_argument(
        "--email-only", action="store_true",
        help="Send only via Gmail",
    )
    return parser.parse_args()


def resolve_target_date(args: argparse.Namespace) -> tuple:
    """Resolve target date and day number from CLI args."""
    if args.day is not None:
        day_number = args.day
        if day_number < 1:
            logger.error("Day number must be >= 1")
            sys.exit(1)
        target_date = START_DATE + timedelta(days=day_number - 1)
        return target_date, day_number

    if args.date is not None:
        try:
            target_date = date.fromisoformat(args.date)
        except ValueError:
            logger.error("Invalid date format: %s (expected YYYY-MM-DD)", args.date)
            sys.exit(1)
        day_number = get_day_number(target_date)
        return target_date, day_number

    target_date = date.today()
    day_number = get_day_number(target_date)
    return target_date, day_number


def main() -> None:
    args = parse_args()
    target_date, day_number = resolve_target_date(args)
    week = get_week_number(day_number)

    logger.info(
        "Morning delivery for Day %d (Week %d) - %s",
        day_number, week, target_date.isoformat(),
    )

    # Load or generate content
    content = load_content(target_date, day_number)
    if content is None:
        logger.error("Failed to load or generate morning content")
        sys.exit(1)

    # Load domain config for templates
    domain_config = load_domain_config()

    # Render formatted messages
    telegram_message = render_telegram_message(content, domain_config)
    email_html = render_email_html(content, domain_config)
    email_subject = f"Day {day_number}: {content.get('title', 'Wealth Transformation')}"

    if args.dry_run:
        print("\n" + "=" * 60)
        print("  MORNING DELIVERY - DRY RUN")
        print(f"  Day {day_number} ({target_date}) - Week {week}")
        print("=" * 60)
        print("\n--- TELEGRAM MESSAGE ---\n")
        print(telegram_message)
        print("\n--- EMAIL SUBJECT ---\n")
        print(email_subject)
        print("\n--- EMAIL HTML (first 500 chars) ---\n")
        print(email_html[:500])
        print("\n" + "=" * 60)
        logger.info("Dry run complete - no messages sent")
        return

    # Send via channels
    telegram_ok = False
    email_ok = False

    send_telegram_flag = not args.email_only
    send_email_flag = not args.telegram_only

    if send_telegram_flag:
        chat_id = os.environ.get("TELEGRAM_CHAT_ID", "")
        if not chat_id:
            logger.error("TELEGRAM_CHAT_ID environment variable is not set")
        else:
            telegram_ok = send_telegram(telegram_message, chat_id)

    if send_email_flag:
        recipient = os.environ.get("GMAIL_RECIPIENT", "")
        if not recipient:
            logger.error("GMAIL_RECIPIENT environment variable is not set")
        else:
            email_ok = send_gmail(email_html, email_subject, recipient)

    # Log delivery
    log_delivery(content, telegram_ok, email_ok)

    # Summary
    if telegram_ok and email_ok:
        logger.info("Morning delivery complete - all channels successful")
    elif telegram_ok or email_ok:
        logger.warning("Morning delivery partial - some channels failed")
    else:
        logger.error("Morning delivery failed - no channels succeeded")
        sys.exit(1)


if __name__ == "__main__":
    main()
