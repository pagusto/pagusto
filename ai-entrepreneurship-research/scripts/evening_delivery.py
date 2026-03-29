#!/usr/bin/env python3
"""
Evening Delivery Pipeline for Wealth System
Orchestrates 8PM content delivery via Telegram and Gmail.

Usage:
    python evening_delivery.py              # Generate and send today's evening content
    python evening_delivery.py --dry-run    # Preview without sending
    python evening_delivery.py --day 5      # Generate for specific day number
    python evening_delivery.py --date 2026-04-05  # Generate for specific date
    python evening_delivery.py --telegram-only     # Send only via Telegram
    python evening_delivery.py --email-only        # Send only via Gmail

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

BASE_DIR = Path("/home/user/pagusto/ai-entrepreneurship-research")
SCRIPTS_DIR = BASE_DIR / "scripts"
CONTENT_DIR = BASE_DIR / "content"
GENERATED_DIR = CONTENT_DIR / "generated"
TEMPLATES_DIR = BASE_DIR / "templates"
DOMAIN_CONFIG_PATH = TEMPLATES_DIR / "domain_config.json"

TELEGRAM_SKILL = Path("/home/user/pagusto/claude-config/skills/telegram/scripts/telegram.py")
GMAIL_SKILL = Path("/home/user/pagusto/claude-config/skills/gmail/scripts/gmail.py")
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
logger = logging.getLogger("evening_delivery")

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
    """Generate evening content using content_generator.py."""
    output_path = GENERATED_DIR / f"{target_date.isoformat()}-evening.json"

    if output_path.exists():
        logger.info("Evening content already exists: %s", output_path)
        return output_path

    logger.info("Generating evening content for day %d (%s)", day_number, target_date)
    cmd = [
        sys.executable, str(CONTENT_GENERATOR),
        "--day", str(day_number),
        "--session", "evening",
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
    """Load or generate evening content."""
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

    # Extract evening-specific fields from content body or direct fields
    content_body = content.get("content_body", "")

    # Try to extract structured evening fields
    reflection_question = content.get("reflection", "")
    night_technique = content.get("exercise", "")
    affirmation = content.get("quote", "")

    # If we have a content_body but no structured fields, use the body
    if not reflection_question and content_body:
        reflection_question = content_body

    # Build tomorrow preview from next day's calendar entry (best effort)
    tomorrow_preview = content.get("tomorrow_preview", "Stay tuned for tomorrow's lesson.")

    return {
        "day_number": content.get("day_number", 0),
        "date_formatted": content.get("date", ""),
        "week_number": content.get("week", 1),
        "title": content.get("title", ""),
        "domain": domain,
        "complexity": content.get("complexity", "beginner"),
        "reflection_question": reflection_question,
        "night_technique": night_technique,
        "tomorrow_preview": tomorrow_preview,
        "affirmation": affirmation,
        "content_body": content_body,
        "cultural_source": content.get("cultural_source", ""),
        "quote": content.get("quote", ""),
        "quote_author": content.get("quote_author", ""),
    }


def render_telegram_message(content: dict, domain_config: dict) -> str:
    """Render evening content as Telegram Markdown message."""
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=False,
    )

    try:
        template = env.get_template("evening_telegram.md")
    except Exception as exc:
        logger.error("Failed to load evening Telegram template: %s", exc)
        return _fallback_telegram_format(content)

    template_vars = get_template_vars(content, domain_config)
    return template.render(**template_vars)


def render_email_html(content: dict, domain_config: dict) -> str:
    """Render evening content as HTML email using the evening section of email template."""
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
    title = content.get("title", "Evening Reflection")
    body = content.get("content_body", "")
    quote = content.get("quote", "")
    author = content.get("quote_author", "")

    parts = [
        f"*Good evening, Paul.*",
        "",
        f"*Day {day} Reflection: {title}*",
        "",
        body,
    ]
    if quote:
        parts.append("")
        parts.append(f'_"{quote}"_ -- {author}')

    return "\n".join(parts)


def _fallback_email_format(content: dict) -> str:
    """Fallback email format if template fails."""
    title = content.get("title", "Evening Reflection")
    body = content.get("content_body", "").replace("\n", "<br>")
    return f"<html><body><h1>{title}</h1><p>{body}</p></body></html>"


# ---------------------------------------------------------------------------
# Delivery: Telegram
# ---------------------------------------------------------------------------


def send_telegram(message: str, chat_id: str) -> bool:
    """Send message via Telegram skill with retry logic."""
    if not TELEGRAM_SKILL.exists():
        logger.error("Telegram skill script not found: %s", TELEGRAM_SKILL)
        return False

    for attempt in range(1, MAX_RETRIES + 1):
        logger.info("Telegram send attempt %d/%d", attempt, MAX_RETRIES)
        cmd = [
            sys.executable,
            str(TELEGRAM_SKILL),
            "send-message",
            chat_id,
            message,
            "--parse-mode", "Markdown",
        ]

        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=30,
            )
            if result.returncode == 0:
                response = json.loads(result.stdout) if result.stdout.strip() else {}
                if "error" not in response:
                    logger.info("Telegram message sent successfully")
                    return True
                logger.warning("Telegram API error: %s", response.get("error"))
            else:
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
        "session": "evening",
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
        description="Evening Delivery Pipeline - sends 8PM content via Telegram and Gmail"
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
        "Evening delivery for Day %d (Week %d) - %s",
        day_number, week, target_date.isoformat(),
    )

    # Load or generate content
    content = load_content(target_date, day_number)
    if content is None:
        logger.error("Failed to load or generate evening content")
        sys.exit(1)

    # Load domain config for templates
    domain_config = load_domain_config()

    # Render formatted messages
    telegram_message = render_telegram_message(content, domain_config)
    email_html = render_email_html(content, domain_config)
    email_subject = f"Day {day_number} Evening: {content.get('title', 'Wealth Transformation')}"

    if args.dry_run:
        print("\n" + "=" * 60)
        print("  EVENING DELIVERY - DRY RUN")
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
        logger.info("Evening delivery complete - all channels successful")
    elif telegram_ok or email_ok:
        logger.warning("Evening delivery partial - some channels failed")
    else:
        logger.error("Evening delivery failed - no channels succeeded")
        sys.exit(1)


if __name__ == "__main__":
    main()
