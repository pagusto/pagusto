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
CONTENT_DIR = BASE_DIR / "content"
GENERATED_DIR = CONTENT_DIR / "generated"
CALENDAR_PATH = CONTENT_DIR / "calendar_365.json"
SOURCES_PATH = CONTENT_DIR / "sources.json"

START_DATE = date(2026, 3, 30)

COMPLEXITY_SCHEDULE = {
    range(1, 13): "basic",
    range(13, 27): "intermediate",
    range(27, 41): "advanced",
    range(41, 53): "master",
}

# Domain display names and emojis
DOMAIN_CONFIG = {
    "mental_reprogramming": {"name": "Mental Reprogramming", "emoji": "\U0001f9e0"},
    "book_summary": {"name": "Book Wisdom", "emoji": "\U0001f4da"},
    "biography": {"name": "Inspiring Biography", "emoji": "\U0001f31f"},
    "sales_persuasion": {"name": "Sales & Persuasion", "emoji": "\U0001f3af"},
    "ai_engineering": {"name": "AI Engineering", "emoji": "\U0001f916"},
    "influence_charisma": {"name": "Influence & Charisma", "emoji": "\U0001f525"},
    "spirituality": {"name": "Spirituality", "emoji": "\U0001f54a\ufe0f"},
    "reflection_night_technique": {"name": "Reflection & Night Technique", "emoji": "\U0001f319"},
    "book_exercise": {"name": "Book Exercise", "emoji": "\U0001f4dd"},
    "biography_lesson": {"name": "Biography Lesson", "emoji": "\U0001f4a1"},
    "sales_roleplay": {"name": "Sales Role-Play", "emoji": "\U0001f3ad"},
    "ai_action_plan": {"name": "AI Action Plan", "emoji": "\U0001f680"},
    "podcast_recommendation": {"name": "Audio Recommendation", "emoji": "\U0001f3a7"},
    "weekly_planning": {"name": "Weekly Planning", "emoji": "\U0001f4c5"},
}

CULTURAL_FLAGS = {
    "western": "\U0001f1fa\U0001f1f8",
    "eastern": "\U0001f1ee\U0001f1f3",
    "latin": "\U0001f1e7\U0001f1f7",
    "african": "\U0001f1ff\U0001f1e6",
    "japanese": "\U0001f1ef\U0001f1f5",
    "middle_eastern": "\U0001f1f8\U0001f1e6",
    "indigenous": "\U0001f30d",
}

# Business application templates by domain
BUSINESS_TEMPLATES = {
    "mental_reprogramming": {
        "cleaning": "Use alpha state visualization before client meetings to project confidence",
        "recruiting": "Apply mental rehearsal before interviews to sharpen intuition",
        "agency": "Reprogram limiting beliefs about your agency's growth potential",
        "passive_income": "Visualize passive income streams flowing during meditation",
    },
    "book_summary": {
        "cleaning": "Apply the book's core principle to optimize your cleaning operations",
        "recruiting": "Use the author's framework to improve candidate selection",
        "agency": "Implement the key strategy to differentiate your AI agency",
        "passive_income": "Adapt the wealth principle to create a new income stream",
    },
    "biography": {
        "cleaning": "Apply this leader's persistence to grow your cleaning business",
        "recruiting": "Use their people skills approach in your recruiting work",
        "agency": "Follow their entrepreneurial path to build your agency",
        "passive_income": "Study how they created wealth that works without them",
    },
    "sales_persuasion": {
        "cleaning": "Practice this technique in your next cleaning service pitch",
        "recruiting": "Use this persuasion method when presenting candidates to clients",
        "agency": "Apply this sales framework to close AI agency deals",
        "passive_income": "Use this influence principle to convert leads on autopilot",
    },
    "ai_engineering": {
        "cleaning": "Automate scheduling and client communication with AI tools",
        "recruiting": "Use Claude Code to build candidate screening automations",
        "agency": "Master this technique to deliver better AI solutions to clients",
        "passive_income": "Build this as a SaaS product for recurring revenue",
    },
    "influence_charisma": {
        "cleaning": "Use charisma techniques to retain clients and get referrals",
        "recruiting": "Apply influence skills to build stronger client relationships",
        "agency": "Leverage personal branding to attract agency clients",
        "passive_income": "Build an influential personal brand that sells while you sleep",
    },
    "spirituality": {
        "cleaning": "Find purpose and meaning in service to others through your work",
        "recruiting": "Connect people with their calling - it's a spiritual practice",
        "agency": "Build your agency with integrity and conscious leadership",
        "passive_income": "Align your income streams with your higher purpose",
    },
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
    delta = (target_date - START_DATE).days + 1
    if delta < 1:
        logger.error("Date %s is before the start date %s", target_date, START_DATE)
        sys.exit(1)
    if delta > 365:
        logger.warning("Date %s is beyond the 365-day calendar (day %d)", target_date, delta)
    return delta


def get_week_number(day_number: int) -> int:
    return ((day_number - 1) // 7) + 1


def get_complexity(week: int) -> str:
    for week_range, level in COMPLEXITY_SCHEDULE.items():
        if week in week_range:
            return level
    return "master"


def load_json(path: Path) -> dict:
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
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    logger.info("Saved: %s", path)


# ---------------------------------------------------------------------------
# Calendar and Sources lookup
# ---------------------------------------------------------------------------


def find_calendar_entry(calendar: dict, day_number: int) -> Optional[dict]:
    days = calendar.get("days", [])
    if isinstance(days, list):
        idx = day_number - 1
        if 0 <= idx < len(days):
            return days[idx]
    elif isinstance(days, dict):
        return days.get(str(day_number))
    return None


def find_source_by_name(sources_db: dict, source_name: str, domain: str) -> Optional[dict]:
    """Find the best matching source by name across all source collections."""
    if not source_name:
        return None

    name_lower = source_name.lower()

    # Search books
    for book in sources_db.get("books", []):
        author = book.get("author", "").lower()
        title = book.get("title", "").lower()
        if author in name_lower or name_lower in author or title in name_lower:
            return {"type": "book", **book}

    # Search biographies
    for bio in sources_db.get("biographies", []):
        name = bio.get("name", "").lower()
        if name in name_lower or name_lower in name:
            return {"type": "biography", **bio}

    # Search techniques
    for tech in sources_db.get("techniques", []):
        tname = tech.get("name", "").lower()
        origin = tech.get("origin", "").lower()
        if tname in name_lower or origin in name_lower:
            return {"type": "technique", **tech}

    # Search podcasts
    for pod in sources_db.get("podcasts", []):
        ptitle = pod.get("title", "").lower()
        host = pod.get("host", "").lower()
        if ptitle in name_lower or host in name_lower:
            return {"type": "podcast", **pod}

    return None


# ---------------------------------------------------------------------------
# Content Generation
# ---------------------------------------------------------------------------


def generate_content(
    calendar_entry: dict,
    sources_db: dict,
    day_number: int,
    target_date: date,
    session: str,
) -> dict:
    """Generate structured content for a morning or evening session."""
    week = get_week_number(day_number)
    complexity = get_complexity(week)

    # Extract session-specific data from calendar entry
    session_data = calendar_entry.get(session, {})
    domain = session_data.get("domain", "general")
    topic_hint = session_data.get("topic_hint", f"Day {day_number}")
    source_name = session_data.get("source_name", "")
    cultural_source = calendar_entry.get("cultural_source", "western")
    day_of_week = calendar_entry.get("day_of_week", "")

    # Find matching source
    source = find_source_by_name(sources_db, source_name, domain)

    # Get display config
    domain_info = DOMAIN_CONFIG.get(domain, {"name": domain.replace("_", " ").title(), "emoji": ""})
    cultural_flag = CULTURAL_FLAGS.get(cultural_source, "")

    # Get quote from source
    quote = ""
    quote_author = ""
    if source:
        quote = source.get("best_quote", "")
        quote_author = source.get("author", source.get("name", source.get("origin", "")))

    # Build business applications
    base_domain = domain.split("_")[0] if "_" in domain else domain
    biz_templates = BUSINESS_TEMPLATES.get(domain, BUSINESS_TEMPLATES.get(base_domain, {}))
    if not biz_templates:
        # Find closest match
        for key in BUSINESS_TEMPLATES:
            if key in domain or domain in key:
                biz_templates = BUSINESS_TEMPLATES[key]
                break

    # Build content body
    if session == "morning":
        content_body = _build_morning_body(topic_hint, domain_info, source, complexity, cultural_source)
        exercise = _build_exercise(topic_hint, domain, source, complexity)
    else:
        content_body = _build_evening_body(topic_hint, domain_info, source, complexity, day_number)
        exercise = ""

    # Reflection and night technique for evening
    reflection_question = ""
    night_technique = ""
    tomorrow_preview = ""
    affirmation = ""
    if session == "evening":
        reflection_question = _build_reflection(topic_hint, domain, source)
        night_technique = _build_night_technique(topic_hint, source, complexity)
        tomorrow_preview = _build_tomorrow_preview(calendar_entry, sources_db, day_number)
        affirmation = _build_affirmation(domain, cultural_source, week)

    return {
        "day_number": day_number,
        "date": target_date.isoformat(),
        "session": session,
        "week": week,
        "day_of_week": day_of_week,
        "title": topic_hint,
        "domain": domain,
        "domain_display": domain_info["name"],
        "domain_emoji": domain_info["emoji"],
        "complexity": complexity,
        "cultural_source": cultural_source,
        "cultural_flag": cultural_flag,
        "content_body": content_body,
        "exercise": exercise,
        "business_applications": {
            "cleaning": biz_templates.get("cleaning", ""),
            "recruiting": biz_templates.get("recruiting", ""),
            "agency": biz_templates.get("agency", ""),
            "passive_income": biz_templates.get("passive_income", ""),
        },
        "quote": quote,
        "quote_author": quote_author,
        "source_name": source_name,
        "reflection_question": reflection_question,
        "night_technique": night_technique,
        "tomorrow_preview": tomorrow_preview,
        "affirmation": affirmation,
        "generated_at": datetime.now().isoformat(),
    }


def _build_morning_body(topic: str, domain_info: dict, source: Optional[dict], complexity: str, culture: str) -> str:
    parts = []
    parts.append(f"Today we explore *{topic}* from the {domain_info['name']} domain.")
    parts.append("")

    if source:
        stype = source.get("type", "")
        if stype == "book":
            parts.append(f"From the book *{source['title']}* by {source['author']}:")
            parts.append("")
            cats = source.get("categories", [])
            if cats:
                parts.append(f"Categories: {', '.join(cats)}")
        elif stype == "biography":
            parts.append(f"Learning from *{source['name']}* ({source.get('culture', 'global')} tradition):")
            parts.append("")
            lesson = source.get("key_lesson", "")
            if lesson:
                parts.append(f"Key Lesson: {lesson}")
        elif stype == "technique":
            parts.append(f"Technique: *{source['name']}* (from {source.get('origin', 'unknown')}):")
            parts.append("")
            duration = source.get("duration", "")
            if duration:
                parts.append(f"Duration: {duration}")
            cat = source.get("category", "")
            if cat:
                parts.append(f"Category: {cat}")
        elif stype == "podcast":
            parts.append(f"Recommended: *{source['title']}* by {source.get('host', 'unknown')}")
            parts.append("")
            platform = source.get("platform", "")
            if platform:
                parts.append(f"Available on: {platform}")

    parts.append("")
    parts.append(f"Level: {complexity.title()} | Culture: {culture.replace('_', ' ').title()}")

    return "\n".join(parts)


def _build_evening_body(topic: str, domain_info: dict, source: Optional[dict], complexity: str, day_number: int) -> str:
    parts = []
    parts.append(f"Let's reflect on today's journey through *{topic}*.")
    parts.append("")

    if source:
        quote = source.get("best_quote", "")
        author = source.get("author", source.get("name", source.get("origin", "")))
        if quote:
            parts.append(f'Remember: "{quote}" - {author}')
            parts.append("")

    parts.append(f"Day {day_number} is complete. Every day you grow stronger.")

    return "\n".join(parts)


def _build_exercise(topic: str, domain: str, source: Optional[dict], complexity: str) -> str:
    exercises = {
        "mental_reprogramming": f"Practice the {topic} technique for 15 minutes. Find a quiet space, close your eyes, and follow the guided steps.",
        "book_summary": f"Write down 3 key insights from today's lesson and how you'll apply ONE of them this week.",
        "biography": f"Identify ONE habit from today's biography that you can adopt starting today.",
        "sales_persuasion": f"Practice today's technique in a real conversation. Track the response you get.",
        "ai_engineering": f"Open Claude Code and build a small automation based on today's tip. Ship something small.",
        "influence_charisma": f"Apply today's influence principle in your next interaction. Notice the effect.",
        "spirituality": f"Spend 10 minutes in silent meditation reflecting on today's spiritual practice.",
    }

    base = domain.split("_")[0] if "_" in domain else domain
    for key in exercises:
        if key in domain or domain in key or base in key:
            return exercises[key]

    return f"Spend 15 minutes actively applying today's lesson on {topic}."


def _build_reflection(topic: str, domain: str, source: Optional[dict]) -> str:
    reflections = {
        "reflection_night_technique": f"How did today's practice of {topic} change your state of mind? What did you feel during the exercise?",
        "book_exercise": f"Which insight from today's book resonated most with your current situation? How will you apply it tomorrow?",
        "biography_lesson": f"What aspect of today's biography challenged your current thinking? What would they do in your shoes?",
        "sales_roleplay": f"How did you apply today's sales technique? What response did you get? How would you refine it?",
        "ai_action_plan": f"What did you build or automate today? How does it move you closer to your AI agency goal?",
        "podcast_recommendation": f"What was the most impactful idea from today's audio content? How does it connect to your week's theme?",
        "weekly_planning": f"Looking back at this week: what was your biggest win? What will you double down on next week?",
    }
    return reflections.get(domain, f"How did today's exploration of {topic} shift your perspective?")


def _build_night_technique(topic: str, source: Optional[dict], complexity: str) -> str:
    techniques = [
        "Silva Three-Finger Technique: Touch thumb to first two fingers. At this signal, your mind enters alpha state. Visualize tomorrow's success in vivid detail.",
        "Neville Goddard's SATS: As you fall asleep, replay your desired outcome as if it already happened. Feel the joy, the gratitude, the reality of it.",
        "Joe Dispenza's Heart Coherence: Place your hand on your heart. Breathe slowly. Feel gratitude for 3 things. Elevate your energy before sleep.",
        "Silva Glass of Water: Before bed, drink half a glass of water while thinking about a problem. Sleep on it. Drink the other half upon waking. Trust the answer that comes.",
        "Mirror Technique: Look into your eyes in the mirror for 2 minutes. Affirm: 'Every day, in every way, I am getting better and better.'",
    ]
    from hashlib import md5
    idx = int(md5(topic.encode()).hexdigest(), 16) % len(techniques)
    return techniques[idx]


def _build_tomorrow_preview(calendar_entry: dict, sources_db: dict, day_number: int) -> str:
    """Build a preview of tomorrow's topic."""
    calendar = load_json(CALENDAR_PATH)
    tomorrow = find_calendar_entry(calendar, day_number + 1)
    if tomorrow:
        morning = tomorrow.get("morning", {})
        return f"Tomorrow: {morning.get('topic_hint', 'New discovery')} ({morning.get('source_name', '')})"
    return "Tomorrow brings new wisdom. Rest well."


def _build_affirmation(domain: str, culture: str, week: int) -> str:
    affirmations = [
        "I am a powerful creator of wealth and value.",
        "My mind is a money magnet. Abundance flows to me effortlessly.",
        "I deserve success, and I work daily to earn it.",
        "Every challenge is an opportunity in disguise.",
        "I am building an empire, one day at a time.",
        "My businesses grow because I grow.",
        "I attract the right people, opportunities, and resources.",
        "Financial freedom is my birthright, and I claim it now.",
        "I am the architect of my destiny.",
        "Today's effort is tomorrow's wealth.",
    ]
    idx = (week - 1) % len(affirmations)
    return affirmations[idx]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Content Generator for Wealth System"
    )
    parser.add_argument("--day", type=int, default=None, metavar="N",
                        help="Generate for a specific day number (1-365)")
    parser.add_argument("--date", type=str, default=None, metavar="YYYY-MM-DD",
                        help="Generate for a specific date")
    parser.add_argument("--session", choices=["morning", "evening", "both"],
                        default="both", help="Which session to generate (default: both)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print content to stdout without saving")
    parser.add_argument("--calendar", type=str, default=str(CALENDAR_PATH))
    parser.add_argument("--sources", type=str, default=str(SOURCES_PATH))
    return parser.parse_args()


def resolve_target_date(args: argparse.Namespace) -> tuple[date, int]:
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

    logger.info("Generating content for Day %d (Week %d) - %s", day_number, week, target_date.isoformat())

    calendar = load_json(Path(args.calendar))
    sources_db = load_json(Path(args.sources))

    entry = find_calendar_entry(calendar, day_number)
    if entry is None:
        logger.error("No calendar entry found for day %d", day_number)
        sys.exit(1)

    morning_data = entry.get("morning", {})
    logger.info("Topic: %s (Source: %s)", morning_data.get("topic_hint", "Unknown"), morning_data.get("source_name", ""))

    sessions = []
    if args.session in ("morning", "both"):
        sessions.append("morning")
    if args.session in ("evening", "both"):
        sessions.append("evening")

    for session in sessions:
        content = generate_content(entry, sources_db, day_number, target_date, session)

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
