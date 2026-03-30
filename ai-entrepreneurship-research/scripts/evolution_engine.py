#!/usr/bin/env python3
"""
Evolution Engine for Wealth System
Self-improvement engine that tracks deliveries, ensures quality,
and generates weekly reports.

Usage:
    python evolution_engine.py --check        # Verify system health
    python evolution_engine.py --report       # Generate current week report
    python evolution_engine.py --report --week 3  # Generate report for specific week
    python evolution_engine.py --log-summary  # Show delivery log summary

Environment Variables:
    None required - reads from local data files.
"""

import argparse
import json
import logging
import sys
from collections import Counter, defaultdict
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
DELIVERY_LOG_PATH = CONTENT_DIR / "delivery_log.json"
REPORTS_DIR = BASE_DIR / "reports"

START_DATE = date(2026, 3, 30)

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
logger = logging.getLogger("evolution_engine")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def get_day_number(target_date: date) -> int:
    """Calculate day number (1-365) from the start date."""
    delta = (target_date - START_DATE).days + 1
    return max(delta, 0)


def get_week_number(day_number: int) -> int:
    """Get the week number (1-52) from the day number."""
    if day_number < 1:
        return 0
    return ((day_number - 1) // 7) + 1


def get_expected_complexity(week: int) -> str:
    """Determine expected complexity level based on week number."""
    for week_range, level in COMPLEXITY_SCHEDULE.items():
        if week in week_range:
            return level
    return "advanced"


def get_week_dates(week_number: int) -> tuple:
    """Get the start and end dates for a given week number."""
    week_start_day = (week_number - 1) * 7 + 1
    week_end_day = min(week_start_day + 6, 365)
    start_date = START_DATE + timedelta(days=week_start_day - 1)
    end_date = START_DATE + timedelta(days=week_end_day - 1)
    return start_date, end_date


def load_json(path: Path) -> Optional[dict]:
    """Load a JSON file, return None on error."""
    if not path.exists():
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as exc:
        logger.error("Failed to load %s: %s", path, exc)
        return None


def load_delivery_log() -> list:
    """Load the delivery log."""
    data = load_json(DELIVERY_LOG_PATH)
    if data is None:
        return []
    if isinstance(data, list):
        return data
    return []


# ---------------------------------------------------------------------------
# Topic Repetition Check
# ---------------------------------------------------------------------------


def check_topic_repetition(delivery_log: list) -> list:
    """Check for repeated topics in the delivery log."""
    issues = []
    seen_topics = {}

    for entry in delivery_log:
        title = entry.get("title", "")
        day = entry.get("day_number", 0)
        session = entry.get("session", "")

        if not title:
            continue

        key = f"{title}|{session}"
        if key in seen_topics:
            prev_day = seen_topics[key]
            issues.append(
                f"Topic repeated: '{title}' ({session}) on day {prev_day} and day {day}"
            )
        else:
            seen_topics[key] = day

    return issues


# ---------------------------------------------------------------------------
# Complexity Check
# ---------------------------------------------------------------------------


def check_complexity(delivery_log: list) -> list:
    """Verify complexity levels are appropriate for each week."""
    issues = []

    for entry in delivery_log:
        day = entry.get("day_number", 0)
        if day < 1:
            continue

        week = get_week_number(day)
        expected = get_expected_complexity(week)

        # Check generated content files for complexity
        date_str = entry.get("date", "")
        session = entry.get("session", "morning")
        if date_str:
            content_path = GENERATED_DIR / f"{date_str}-{session}.json"
            content = load_json(content_path)
            if content:
                actual = content.get("complexity", "")
                if actual and actual != expected:
                    issues.append(
                        f"Day {day} ({session}): complexity is '{actual}', "
                        f"expected '{expected}' for week {week}"
                    )

    return issues


# ---------------------------------------------------------------------------
# Delivery Health Check
# ---------------------------------------------------------------------------


def check_delivery_gaps(delivery_log: list) -> list:
    """Check for missing deliveries (days without both morning and evening)."""
    issues = []
    today = date.today()
    current_day = get_day_number(today)

    if current_day < 1:
        return issues

    # Build map of delivered days
    delivered = defaultdict(set)
    for entry in delivery_log:
        day = entry.get("day_number", 0)
        session = entry.get("session", "")
        if day > 0 and session:
            delivered[day].add(session)

    # Check each day up to today
    for day in range(1, min(current_day + 1, 366)):
        sessions = delivered.get(day, set())
        if "morning" not in sessions:
            day_date = START_DATE + timedelta(days=day - 1)
            issues.append(f"Day {day} ({day_date}): missing morning delivery")
        if "evening" not in sessions:
            day_date = START_DATE + timedelta(days=day - 1)
            issues.append(f"Day {day} ({day_date}): missing evening delivery")

    return issues


def check_delivery_failures(delivery_log: list) -> list:
    """Check for failed deliveries (where neither channel succeeded)."""
    issues = []

    for entry in delivery_log:
        telegram_ok = entry.get("telegram_sent", False)
        email_ok = entry.get("email_sent", False)
        day = entry.get("day_number", 0)
        session = entry.get("session", "")

        if not telegram_ok and not email_ok:
            issues.append(
                f"Day {day} ({session}): both Telegram and Gmail delivery failed"
            )
        elif not telegram_ok:
            issues.append(f"Day {day} ({session}): Telegram delivery failed")
        elif not email_ok:
            issues.append(f"Day {day} ({session}): Gmail delivery failed")

    return issues


# ---------------------------------------------------------------------------
# System Health Check
# ---------------------------------------------------------------------------


def run_health_check() -> dict:
    """Run a full system health check."""
    results = {
        "status": "healthy",
        "checks": {},
        "issues": [],
        "checked_at": datetime.now().isoformat(),
    }

    # 1. Check calendar file exists
    calendar_ok = CALENDAR_PATH.exists()
    results["checks"]["calendar_file"] = "OK" if calendar_ok else "MISSING"
    if not calendar_ok:
        results["issues"].append("Calendar file missing: calendar_365.json")

    # 2. Check sources file exists
    sources_path = CONTENT_DIR / "sources.json"
    sources_ok = sources_path.exists()
    results["checks"]["sources_file"] = "OK" if sources_ok else "MISSING"
    if not sources_ok:
        results["issues"].append("Sources file missing: sources.json")

    # 3. Check generated content directory
    generated_ok = GENERATED_DIR.exists()
    results["checks"]["generated_dir"] = "OK" if generated_ok else "MISSING"
    if generated_ok:
        generated_files = list(GENERATED_DIR.glob("*.json"))
        results["checks"]["generated_count"] = len(generated_files)
    else:
        results["checks"]["generated_count"] = 0

    # 4. Check delivery log
    delivery_log = load_delivery_log()
    results["checks"]["delivery_log_entries"] = len(delivery_log)

    # 5. Check for topic repetition
    repetition_issues = check_topic_repetition(delivery_log)
    results["checks"]["topic_repetition"] = (
        "OK" if not repetition_issues else f"{len(repetition_issues)} issues"
    )
    results["issues"].extend(repetition_issues)

    # 6. Check complexity levels
    complexity_issues = check_complexity(delivery_log)
    results["checks"]["complexity_levels"] = (
        "OK" if not complexity_issues else f"{len(complexity_issues)} issues"
    )
    results["issues"].extend(complexity_issues)

    # 7. Check delivery failures
    failure_issues = check_delivery_failures(delivery_log)
    results["checks"]["delivery_failures"] = (
        "OK" if not failure_issues else f"{len(failure_issues)} issues"
    )
    results["issues"].extend(failure_issues)

    # 8. Check templates
    templates_dir = BASE_DIR / "templates"
    morning_template = templates_dir / "morning_telegram.md"
    evening_template = templates_dir / "evening_telegram.md"
    email_template = templates_dir / "email_daily.html"
    results["checks"]["morning_template"] = "OK" if morning_template.exists() else "MISSING"
    results["checks"]["evening_template"] = "OK" if evening_template.exists() else "MISSING"
    results["checks"]["email_template"] = "OK" if email_template.exists() else "MISSING"

    # Set overall status
    if results["issues"]:
        results["status"] = "degraded" if len(results["issues"]) < 5 else "unhealthy"

    return results


# ---------------------------------------------------------------------------
# Weekly Report Generation
# ---------------------------------------------------------------------------


def generate_weekly_report(week_number: int) -> str:
    """Generate a markdown report for the specified week."""
    start_date, end_date = get_week_dates(week_number)
    expected_complexity = get_expected_complexity(week_number)

    delivery_log = load_delivery_log()

    # Filter entries for this week
    week_start_day = (week_number - 1) * 7 + 1
    week_end_day = min(week_start_day + 6, 365)
    week_entries = [
        e for e in delivery_log
        if week_start_day <= e.get("day_number", 0) <= week_end_day
    ]

    # Calculate stats
    total_deliveries = len(week_entries)
    morning_count = sum(1 for e in week_entries if e.get("session") == "morning")
    evening_count = sum(1 for e in week_entries if e.get("session") == "evening")
    telegram_success = sum(1 for e in week_entries if e.get("telegram_sent"))
    email_success = sum(1 for e in week_entries if e.get("email_sent"))
    expected_deliveries = min(week_end_day - week_start_day + 1, 7) * 2

    # Domain distribution
    domains = Counter(e.get("domain", "unknown") for e in week_entries)

    # Topics covered
    topics = [e.get("title", "Unknown") for e in week_entries if e.get("session") == "morning"]

    # Delivery gap analysis
    delivered_days = defaultdict(set)
    for e in week_entries:
        delivered_days[e.get("day_number", 0)].add(e.get("session", ""))

    missing_deliveries = []
    for day in range(week_start_day, week_end_day + 1):
        sessions = delivered_days.get(day, set())
        day_date = START_DATE + timedelta(days=day - 1)
        if "morning" not in sessions:
            missing_deliveries.append(f"Day {day} ({day_date}): morning")
        if "evening" not in sessions:
            missing_deliveries.append(f"Day {day} ({day_date}): evening")

    # Build report
    lines = [
        f"# Week {week_number} Report",
        f"",
        f"**Period:** {start_date.isoformat()} to {end_date.isoformat()}",
        f"**Days:** {week_start_day} to {week_end_day}",
        f"**Expected Complexity:** {expected_complexity}",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"",
        f"---",
        f"",
        f"## Delivery Summary",
        f"",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Total Deliveries | {total_deliveries}/{expected_deliveries} |",
        f"| Morning Messages | {morning_count}/{min(week_end_day - week_start_day + 1, 7)} |",
        f"| Evening Messages | {evening_count}/{min(week_end_day - week_start_day + 1, 7)} |",
        f"| Telegram Success | {telegram_success}/{total_deliveries} |",
        f"| Email Success | {email_success}/{total_deliveries} |",
        f"| Completion Rate | {total_deliveries / expected_deliveries * 100:.0f}% |" if expected_deliveries > 0 else "| Completion Rate | N/A |",
        f"",
        f"## Topics Covered",
        f"",
    ]

    if topics:
        for i, topic in enumerate(topics, 1):
            lines.append(f"{i}. {topic}")
    else:
        lines.append("_No topics delivered this week._")

    lines.extend([
        f"",
        f"## Domain Distribution",
        f"",
    ])

    if domains:
        for domain, count in domains.most_common():
            lines.append(f"- **{domain.replace('_', ' ').title()}**: {count} messages")
    else:
        lines.append("_No domain data available._")

    lines.extend([
        f"",
        f"## Missing Deliveries",
        f"",
    ])

    if missing_deliveries:
        for missing in missing_deliveries:
            lines.append(f"- {missing}")
    else:
        lines.append("None - all deliveries completed successfully.")

    # Repetition check
    week_topics_check = check_topic_repetition(week_entries)
    lines.extend([
        f"",
        f"## Quality Checks",
        f"",
        f"- **Topic Repetition:** {'No issues found' if not week_topics_check else f'{len(week_topics_check)} issues'}",
        f"- **Complexity Level:** {expected_complexity} (expected for week {week_number})",
    ])

    if week_topics_check:
        lines.append("")
        lines.append("### Repetition Issues")
        for issue in week_topics_check:
            lines.append(f"- {issue}")

    lines.extend([
        f"",
        f"---",
        f"",
        f"_Report generated by Evolution Engine_",
    ])

    return "\n".join(lines)


def save_weekly_report(week_number: int, report: str) -> Path:
    """Save a weekly report to the reports directory."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORTS_DIR / f"week_{week_number}_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    logger.info("Report saved to %s", report_path)
    return report_path


# ---------------------------------------------------------------------------
# Log Summary
# ---------------------------------------------------------------------------


def print_log_summary() -> None:
    """Print a summary of the delivery log."""
    delivery_log = load_delivery_log()

    if not delivery_log:
        print("No deliveries recorded yet.")
        return

    total = len(delivery_log)
    morning = sum(1 for e in delivery_log if e.get("session") == "morning")
    evening = sum(1 for e in delivery_log if e.get("session") == "evening")
    telegram_ok = sum(1 for e in delivery_log if e.get("telegram_sent"))
    email_ok = sum(1 for e in delivery_log if e.get("email_sent"))
    both_failed = sum(
        1 for e in delivery_log
        if not e.get("telegram_sent") and not e.get("email_sent")
    )

    # Date range
    dates = [e.get("date", "") for e in delivery_log if e.get("date")]
    first_date = min(dates) if dates else "N/A"
    last_date = max(dates) if dates else "N/A"

    # Unique days
    unique_days = len(set(e.get("day_number", 0) for e in delivery_log if e.get("day_number")))

    print(f"\n{'='*50}")
    print(f"  DELIVERY LOG SUMMARY")
    print(f"{'='*50}")
    print(f"  Total Entries:     {total}")
    print(f"  Morning Messages:  {morning}")
    print(f"  Evening Messages:  {evening}")
    print(f"  Unique Days:       {unique_days}")
    print(f"  Date Range:        {first_date} to {last_date}")
    print(f"  Telegram Success:  {telegram_ok}/{total} ({telegram_ok/total*100:.0f}%)" if total else "")
    print(f"  Email Success:     {email_ok}/{total} ({email_ok/total*100:.0f}%)" if total else "")
    print(f"  Both Failed:       {both_failed}")
    print(f"{'='*50}\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Evolution Engine - self-improvement and tracking for the Wealth System"
    )
    parser.add_argument(
        "--check", action="store_true",
        help="Run a full system health check",
    )
    parser.add_argument(
        "--report", action="store_true",
        help="Generate a weekly report (default: current week)",
    )
    parser.add_argument(
        "--week", type=int, default=None,
        help="Week number for the report (1-52)",
    )
    parser.add_argument(
        "--log-summary", action="store_true",
        help="Show delivery log summary",
    )
    parser.add_argument(
        "--json", action="store_true",
        help="Output results as JSON (for --check)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if not args.check and not args.report and not args.log_summary:
        logger.error("No action specified. Use --check, --report, or --log-summary")
        sys.exit(1)

    if args.check:
        results = run_health_check()

        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print(f"\n{'='*50}")
            print(f"  SYSTEM HEALTH CHECK")
            print(f"  Status: {results['status'].upper()}")
            print(f"{'='*50}")
            print()
            print("Checks:")
            for check, value in results["checks"].items():
                icon = "OK" if value == "OK" else "!!"
                print(f"  [{icon}] {check}: {value}")

            if results["issues"]:
                print(f"\nIssues ({len(results['issues'])}):")
                for issue in results["issues"]:
                    print(f"  - {issue}")
            else:
                print("\nNo issues found.")

            print(f"\n{'='*50}\n")

    if args.report:
        if args.week is not None:
            week_number = args.week
        else:
            today = date.today()
            current_day = get_day_number(today)
            if current_day < 1:
                logger.error("System has not started yet (start date: %s)", START_DATE)
                sys.exit(1)
            week_number = get_week_number(current_day)

        logger.info("Generating report for week %d", week_number)
        report = generate_weekly_report(week_number)
        report_path = save_weekly_report(week_number, report)

        print(report)
        print(f"\nSaved to: {report_path}")

    if args.log_summary:
        print_log_summary()


if __name__ == "__main__":
    main()
