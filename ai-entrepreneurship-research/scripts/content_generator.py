#!/usr/bin/env python3
"""
Content Generator for Wealth System
Generates daily morning (9AM) and evening (8PM) content
based on the 365-day calendar and sources database.
"""

import argparse
import json
import logging
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_DIR = Path("/home/user/pagusto/ai-entrepreneurship-research")
SCRIPTS_DIR = BASE_DIR / "scripts"
CONTENT_DIR = BASE_DIR / "content"
GENERATED_DIR = CONTENT_DIR / "generated"
CALENDAR_PATH = CONTENT_DIR / "calendar_365.json"
SOURCES_PATH = CONTENT_DIR / "sources.json"

# The system starts on 2026-03-30 (Day 1)
START_DATE = date(2026, 3, 30)

# Timezone: Australia/Canberra (AEDT UTC+11)
TIMEZONE_NAME = "Australia/Canberra"

# Complexity ramp: weeks 1-4 = beginner, 5-12 = intermediate, 13+ = advanced
COMPLEXITY_SCHEDULE = {
    range(1, 5): "beginner",
    range(5, 13): "intermediate",
    range(13, 53): "advanced",
}

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("content_generator")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def get_day_number(target_date: date) -> int:
    """Calculate day number (1-365) from the start date."""
    delta = (target_date - START_DATE).days + 1
    if delta < 1:
        logger.error(
            "Date %s is before the start date %s", target_date, START_DATE
        )
        sys.exit(1)
    if delta > 365:
        logger.warning(
            "Date %s is beyond the 365-day calendar (day %d)", target_date, delta
        )
    return delta


def get_week_number(day_number: int) -> int:
    """Get the week number (1-52) from the day number."""
    return ((day_number - 1) // 7) + 1


def get_expected_complexity(week: int) -> str:
    """Determine expected complexity level based on week number."""
    for week_range, level in COMPLEXITY_SCHEDULE.items():
        if week in week_range:
            return level
    return "advanced"


def load_json(path: Path) -> dict:
    """Load a JSON file, exit on error."""
    if not path.exists():
        logger.error("File not found: %s", path)
        sys.exit(1)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as exc:
        logger.error("Invalid JSON in %s: %s", path, exc)
        sys.exit(1)


def save_json(path: Path, data: dict) -> None:
    """Save data to a JSON file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    logger.info("Saved: %s", path)


# ---------------------------------------------------------------------------
# Calendar and Sources lookup
# ---------------------------------------------------------------------------


def find_calendar_entry(calendar: dict, day_number: int) -> Optional[dict]:
    """
    Look up the calendar entry for a given day number.

    Supports calendar formats:
    - List indexed by day number: calendar["days"][day_number - 1]
    - Dict keyed by day string: calendar["days"]["1"], calendar["days"]["42"]
    - Flat list: calendar[day_number - 1]
    """
    if isinstance(calendar, list):
        idx = day_number - 1
        if 0 <= idx < len(calendar):
            return calendar[idx]
        return None

    days = calendar.get("days", calendar.get("calendar", None))
    if days is None:
        # Try top-level keys as day numbers
        return calendar.get(str(day_number), None)

    if isinstance(days, list):
        idx = day_number - 1
        if 0 <= idx < len(days):
            return days[idx]
        return None

    if isinstance(days, dict):
        return days.get(str(day_number), days.get(day_number, None))

    return None


def find_sources_for_topic(sources: dict, domain: str, topic: str) -> list:
    """
    Find relevant sources for a given domain and topic.

    Supports sources formats:
    - Dict keyed by domain: sources["wealth"]["books"]
    - List with domain field: [{"domain": "wealth", ...}]
    """
    results = []

    if isinstance(sources, list):
        for src in sources:
            src_domain = src.get("domain", "").lower()
            src_topic = src.get("topic", "").lower()
            if domain.lower() in src_domain or topic.lower() in src_topic:
                results.append(src)
        return results

    # Dict format - look for domain key
    domain_sources = sources.get(domain, sources.get(domain.lower(), {}))
    if isinstance(domain_sources, list):
        return domain_sources
    if isinstance(domain_sources, dict):
        # Nested by topic
        topic_sources = domain_sources.get(topic, domain_sources.get(topic.lower(), []))
        if isinstance(topic_sources, list):
            return topic_sources
        if isinstance(topic_sources, dict):
            return [topic_sources]

    return results


# ---------------------------------------------------------------------------
# Content Generation
# ---------------------------------------------------------------------------


def generate_content(
    calendar_entry: dict,
    sources: list,
    day_number: int,
    target_date: date,
    session: str,
) -> dict:
    """
    Generate structured content for a morning or evening session.

    Args:
        calendar_entry: The day's calendar entry with topic, domain, etc.
        sources: Relevant source materials.
        session: "morning" or "evening".
    """
    week = get_week_number(day_number)
    complexity = get_expected_complexity(week)

    # Extract fields from calendar entry (flexible key names)
    title = calendar_entry.get("title", calendar_entry.get("topic", f"Day {day_number}"))
    domain = calendar_entry.get("domain", calendar_entry.get("category", "general"))
    cultural_source = calendar_entry.get("cultural_source", calendar_entry.get("source", ""))
    exercise = calendar_entry.get("exercise", calendar_entry.get("practice", ""))
    quote = calendar_entry.get("quote", "")
    quote_author = calendar_entry.get("quote_author", calendar_entry.get("author", ""))
    source_name = ""

    # Pull source material
    if sources:
        primary_source = sources[0]
        source_name = primary_source.get("name", primary_source.get("title", ""))

    # Business applications from calendar or defaults
    business_apps = calendar_entry.get("business_applications", {})
    if not business_apps:
        business_apps = {
            "cleaning": calendar_entry.get("app_cleaning", ""),
            "recruiting": calendar_entry.get("app_recruiting", ""),
            "agency": calendar_entry.get("app_agency", ""),
            "passive_income": calendar_entry.get("app_passive_income", ""),
        }

    # Session-specific content
    if session == "morning":
        content_body = _build_morning_content(calendar_entry, sources, complexity)
    else:
        content_body = _build_evening_content(calendar_entry, sources, complexity)

    return {
        "day_number": day_number,
        "date": target_date.isoformat(),
        "session": session,
        "week": week,
        "title": title,
        "domain": domain,
        "complexity": complexity,
        "cultural_source": cultural_source,
        "content_body": content_body,
        "exercise": exercise,
        "business_applications": business_apps,
        "quote": quote,
        "quote_author": quote_author,
        "source_name": source_name,
        "generated_at": datetime.now().isoformat(),
    }


def _build_morning_content(entry: dict, sources: list, complexity: str) -> str:
    """Build the morning content body - educational/motivational focus."""
    parts = []

    title = entry.get("title", entry.get("topic", ""))
    domain = entry.get("domain", entry.get("category", ""))
    description = entry.get("description", entry.get("content", ""))
    key_lesson = entry.get("key_lesson", entry.get("lesson", ""))
    principles = entry.get("principles", entry.get("key_points", []))

    parts.append(f"Good morning! Today we explore: {title}")
    parts.append(f"Domain: {domain} | Complexity: {complexity}")
    parts.append("")

    if description:
        parts.append(description)
        parts.append("")

    if key_lesson:
        parts.append(f"Key Lesson: {key_lesson}")
        parts.append("")

    if principles:
        parts.append("Core Principles:")
        for i, p in enumerate(principles, 1):
            if isinstance(p, dict):
                p = p.get("text", p.get("principle", str(p)))
            parts.append(f"  {i}. {p}")
        parts.append("")

    # Add source context
    if sources:
        src = sources[0]
        src_insight = src.get("insight", src.get("summary", src.get("description", "")))
        if src_insight:
            parts.append(f"Source Insight: {src_insight}")
            parts.append("")

    return "\n".join(parts)


def _build_evening_content(entry: dict, sources: list, complexity: str) -> str:
    """Build the evening content body - reflection/application focus."""
    parts = []

    title = entry.get("title", entry.get("topic", ""))
    exercise = entry.get("exercise", entry.get("practice", ""))
    reflection = entry.get("reflection", entry.get("evening_reflection", ""))
    action_steps = entry.get("action_steps", entry.get("actions", []))

    parts.append(f"Good evening! Let's reflect on today's topic: {title}")
    parts.append(f"Complexity: {complexity}")
    parts.append("")

    if reflection:
        parts.append(f"Reflection: {reflection}")
        parts.append("")

    if exercise:
        parts.append(f"Tonight's Exercise: {exercise}")
        parts.append("")

    if action_steps:
        parts.append("Action Steps for Tomorrow:")
        for i, step in enumerate(action_steps, 1):
            if isinstance(step, dict):
                step = step.get("text", step.get("step", str(step)))
            parts.append(f"  {i}. {step}")
        parts.append("")

    # Application summary
    apps = entry.get("business_applications", {})
    if any(apps.values()) if isinstance(apps, dict) else apps:
        parts.append("Business Application Summary:")
        if isinstance(apps, dict):
            for biz, app in apps.items():
                if app:
                    parts.append(f"  - {biz.replace('_', ' ').title()}: {app}")
        parts.append("")

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Content Generator for Wealth System - generates daily morning and evening content"
    )
    parser.add_argument(
        "--day",
        type=int,
        default=None,
        metavar="N",
        help="Generate for a specific day number (1-365)",
    )
    parser.add_argument(
        "--date",
        type=str,
        default=None,
        metavar="YYYY-MM-DD",
        help="Generate for a specific date",
    )
    parser.add_argument(
        "--session",
        choices=["morning", "evening", "both"],
        default="both",
        help="Which session to generate (default: both)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print content to stdout without saving",
    )
    parser.add_argument(
        "--calendar",
        type=str,
        default=str(CALENDAR_PATH),
        help="Path to calendar_365.json",
    )
    parser.add_argument(
        "--sources",
        type=str,
        default=str(SOURCES_PATH),
        help="Path to sources.json",
    )
    return parser.parse_args()


def resolve_target_date(args: argparse.Namespace) -> tuple[date, int]:
    """Resolve the target date and day number from CLI args."""
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

    # Default: today
    target_date = date.today()
    day_number = get_day_number(target_date)
    return target_date, day_number


def main() -> None:
    args = parse_args()

    target_date, day_number = resolve_target_date(args)
    week = get_week_number(day_number)

    logger.info(
        "Generating content for Day %d (Week %d) - %s",
        day_number, week, target_date.isoformat(),
    )

    # Load data files
    calendar_path = Path(args.calendar)
    sources_path = Path(args.sources)

    calendar = load_json(calendar_path)
    sources_db = load_json(sources_path)

    # Find calendar entry
    entry = find_calendar_entry(calendar, day_number)
    if entry is None:
        logger.error("No calendar entry found for day %d", day_number)
        sys.exit(1)

    logger.info("Topic: %s", entry.get("title", entry.get("topic", "Unknown")))

    # Find relevant sources
    domain = entry.get("domain", entry.get("category", "general"))
    topic = entry.get("title", entry.get("topic", ""))
    sources = find_sources_for_topic(sources_db, domain, topic)
    logger.info("Found %d relevant sources", len(sources))

    # Generate content
    sessions = []
    if args.session in ("morning", "both"):
        sessions.append("morning")
    if args.session in ("evening", "both"):
        sessions.append("evening")

    for session in sessions:
        content = generate_content(entry, sources, day_number, target_date, session)

        if args.dry_run:
            print(f"\n{'='*60}")
            print(f"  {session.upper()} - Day {day_number} ({target_date})")
            print(f"{'='*60}")
            print(json.dumps(content, indent=2, ensure_ascii=False))
        else:
            filename = f"{target_date.isoformat()}-{session}.json"
            output_path = GENERATED_DIR / filename
            save_json(output_path, content)

    if not args.dry_run:
        logger.info("Content generation complete for %s", target_date.isoformat())
    else:
        logger.info("Dry run complete - no files saved")


if __name__ == "__main__":
    main()
