#!/usr/bin/env python3
"""
Telegram Bot - Daily Wealth & Success Summaries
================================================
Sends daily motivational/educational messages on a 7-day rotating schedule.

Schedule:
    Monday:    Reprogramacion Mental (Silva Method)
    Tuesday:   Resumen de Libro (Top 100 books)
    Wednesday: Biografia Inspiradora (Successful person profile)
    Thursday:  Maestria en Ventas (Sales technique + exercise)
    Friday:    Ingeniero IA (Claude Code tip + AI business idea)
    Saturday:  Influencia y Carisma (Social dynamics exercise)
    Sunday:    Reflexion Espiritual + Visualizacion semanal

Usage:
    # Send today's message
    python telegram_bot.py

    # Send message for a specific day (0=Monday, 6=Sunday)
    python telegram_bot.py --day 0

    # Send message for a specific week number (1-52)
    python telegram_bot.py --week 5

    # Dry run (print to console without sending)
    python telegram_bot.py --dry-run

    # Cron example (daily at 6:00 AM):
    # 0 6 * * * cd /path/to/scripts && python telegram_bot.py >> /var/log/telegram_bot.log 2>&1

Environment Variables:
    TELEGRAM_BOT_TOKEN  - Bot token from @BotFather
    TELEGRAM_CHAT_ID    - Target chat/channel ID
    CONTENT_DB_PATH     - Path to daily_content.json (optional, defaults to same directory)
    TZ                  - Timezone (recommended: America/Mexico_City or your local tz)
"""

import argparse
import json
import logging
import os
import sys
from datetime import datetime, date
from pathlib import Path
from typing import Optional

import telegram
from telegram.constants import ParseMode

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_CONTENT_PATH = SCRIPT_DIR / "daily_content.json"

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")
CONTENT_DB_PATH = os.environ.get("CONTENT_DB_PATH", str(DEFAULT_CONTENT_PATH))

DAY_NAMES = [
    "monday", "tuesday", "wednesday", "thursday",
    "friday", "saturday", "sunday",
]

DAY_THEMES = {
    "monday": "Reprogramacion Mental",
    "tuesday": "Resumen de Libro",
    "wednesday": "Biografia Inspiradora",
    "thursday": "Maestria en Ventas",
    "friday": "Ingeniero IA",
    "saturday": "Influencia y Carisma",
    "sunday": "Reflexion Espiritual",
}

DAY_EMOJIS = {
    "monday": "\U0001f9e0",       # brain
    "tuesday": "\U0001f4da",      # books
    "wednesday": "\U0001f31f",    # star
    "thursday": "\U0001f4b0",     # money bag
    "friday": "\U0001f916",       # robot
    "saturday": "\U0001f3ad",     # performing arts
    "sunday": "\U0001f54a\ufe0f", # dove
}

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("telegram_bot")

# ---------------------------------------------------------------------------
# Content loader
# ---------------------------------------------------------------------------


def load_content_db(path: str) -> dict:
    """Load the JSON content database."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error("Content database not found at %s", path)
        sys.exit(1)
    except json.JSONDecodeError as exc:
        logger.error("Invalid JSON in content database: %s", exc)
        sys.exit(1)


def get_week_number(target_date: Optional[date] = None) -> int:
    """Return ISO week number (1-53)."""
    d = target_date or date.today()
    return d.isocalendar()[1]


def get_day_of_week(target_date: Optional[date] = None) -> int:
    """Return day of week as int (0=Monday, 6=Sunday)."""
    d = target_date or date.today()
    return d.weekday()


def pick_content(db: dict, day_index: int, week: int) -> dict:
    """
    Pick the correct content entry for the given day and week.

    The JSON structure is: { "monday": [ {entry1}, {entry2}, ... ], ... }
    We rotate through entries using the week number modulo entry count,
    so content repeats only after all entries are exhausted.
    """
    day_key = DAY_NAMES[day_index]
    entries = db.get(day_key, [])
    if not entries:
        logger.warning("No content entries for %s", day_key)
        return {}
    idx = (week - 1) % len(entries)
    return entries[idx]


# ---------------------------------------------------------------------------
# Message formatters
# ---------------------------------------------------------------------------

WEALTH_ROUTINE = """
\U0001f525 *TU RUTINA DIARIA DE RIQUEZA* \U0001f525

\u2610 05:30 - Despertar + agua con limon
\u2610 05:45 - 15 min meditacion Silva (nivel alfa)
\u2610 06:00 - Visualizacion de metas (pantalla mental)
\u2610 06:15 - Journaling: 3 gratitudes + intencion del dia
\u2610 06:30 - Ejercicio fisico (45 min)
\u2610 07:15 - Lectura (30 min minimo)
\u2610 07:45 - Desayuno consciente
\u2610 08:00 - Bloque de trabajo profundo #1 (2h)
\u2610 10:00 - Revisar metricas / KPIs del negocio
\u2610 10:30 - Bloque de trabajo profundo #2 (2h)
\u2610 12:30 - Networking / seguimiento de contactos
\u2610 13:00 - Almuerzo + podcast educativo
\u2610 14:00 - Bloque creativo / contenido (2h)
\u2610 16:00 - Revision y planificacion del dia siguiente
\u2610 16:30 - Aprendizaje de habilidad nueva (1h)
\u2610 17:30 - Tiempo personal / familia
\u2610 21:00 - Reflexion nocturna + programacion del sueno (Silva)
\u2610 21:30 - Lectura ligera / descanso
\u2610 22:00 - Dormir (8h para rendimiento optimo)
""".strip()


def format_monday(entry: dict, week: int) -> str:
    """Reprogramacion Mental - Silva Method."""
    lines = [
        f"\U0001f9e0 *LUNES - REPROGRAMACION MENTAL*",
        f"\U0001f52e Semana {week} | Metodo Silva",
        "",
        f"\U0001f3af *Tecnica de la Semana:*",
        f"*{entry.get('technique_name', '')}*",
        "",
        entry.get("technique_description", ""),
        "",
        "\U0001f9d8 *Instrucciones paso a paso:*",
    ]
    for i, step in enumerate(entry.get("steps", []), 1):
        lines.append(f"{i}. {step}")
    lines.append("")
    lines.append(f"\u23f0 *Duracion recomendada:* {entry.get('duration', '15-20 min')}")
    lines.append("")
    lines.append(f"\U0001f4a1 *Ciencia detras:* {entry.get('science', '')}")
    lines.append("")
    lines.append(f"\U0001f4ac *Afirmacion del dia:*")
    lines.append(f"_{entry.get('affirmation', '')}_")
    lines.append("")
    lines.append(f"\U0001f4d6 *Cita:* _{entry.get('quote', '')}_")
    lines.append("")
    lines.append("\u2500" * 30)
    lines.append("")
    lines.append(WEALTH_ROUTINE)
    return "\n".join(lines)


def format_tuesday(entry: dict, week: int) -> str:
    """Resumen de Libro."""
    lines = [
        f"\U0001f4da *MARTES - RESUMEN DE LIBRO*",
        f"\U0001f4d6 Semana {week}",
        "",
        f"\U0001f4d5 *{entry.get('title', '')}*",
        f"\u270d\ufe0f Autor: {entry.get('author', '')}",
        f"\U0001f3f7\ufe0f Categoria: {entry.get('category', '')}",
        "",
        f"\U0001f4dd *Resumen:*",
        entry.get("summary", ""),
        "",
        "\U0001f511 *Ideas clave:*",
    ]
    for idea in entry.get("key_ideas", []):
        lines.append(f"\u2022 {idea}")
    lines.append("")
    lines.append("\U0001f3af *Acciones inmediatas:*")
    for action in entry.get("actions", []):
        lines.append(f"\u26a1 {action}")
    lines.append("")
    lines.append(f"\U0001f4ac *Cita del libro:*")
    lines.append(f"_{entry.get('quote', '')}_")
    lines.append("")
    lines.append(f"\U0001f4ca *Aplicacion al emprendimiento:*")
    lines.append(entry.get("business_application", ""))
    lines.append("")
    lines.append("\u2500" * 30)
    lines.append("")
    lines.append(WEALTH_ROUTINE)
    return "\n".join(lines)


def format_wednesday(entry: dict, week: int) -> str:
    """Biografia Inspiradora."""
    lines = [
        f"\U0001f31f *MIERCOLES - BIOGRAFIA INSPIRADORA*",
        f"\U0001f464 Semana {week}",
        "",
        f"\U0001f451 *{entry.get('name', '')}*",
        f"\U0001f4bc {entry.get('title', '')}",
        f"\U0001f4b0 Patrimonio: {entry.get('net_worth', '')}",
        "",
        f"\U0001f4d6 *Historia:*",
        entry.get("story", ""),
        "",
        "\U0001f511 *Lecciones clave:*",
    ]
    for lesson in entry.get("lessons", []):
        lines.append(f"\u2022 {lesson}")
    lines.append("")
    lines.append("\U0001f4aa *Habitos de exito:*")
    for habit in entry.get("habits", []):
        lines.append(f"\u2705 {habit}")
    lines.append("")
    lines.append(f"\U0001f4ac *Cita celebre:*")
    lines.append(f"_{entry.get('quote', '')}_")
    lines.append("")
    lines.append(f"\U0001f3af *Tu ejercicio de hoy:*")
    lines.append(entry.get("exercise", ""))
    lines.append("")
    lines.append("\u2500" * 30)
    lines.append("")
    lines.append(WEALTH_ROUTINE)
    return "\n".join(lines)


def format_thursday(entry: dict, week: int) -> str:
    """Maestria en Ventas."""
    lines = [
        f"\U0001f4b0 *JUEVES - MAESTRIA EN VENTAS*",
        f"\U0001f4c8 Semana {week}",
        "",
        f"\U0001f3af *Tecnica:* *{entry.get('technique_name', '')}*",
        f"\U0001f464 Fuente: {entry.get('source', '')}",
        "",
        f"\U0001f4dd *Descripcion:*",
        entry.get("description", ""),
        "",
        "\U0001f5e3\ufe0f *Script de ejemplo:*",
    ]
    for line in entry.get("script_lines", []):
        lines.append(f"  \u25b6\ufe0f {line}")
    lines.append("")
    lines.append("\U0001f4a1 *Principio psicologico:*")
    lines.append(entry.get("psychology", ""))
    lines.append("")
    lines.append("\U0001f3cb\ufe0f *Ejercicio de practica:*")
    lines.append(entry.get("exercise", ""))
    lines.append("")
    lines.append("\u26a0\ufe0f *Errores comunes:*")
    for err in entry.get("common_mistakes", []):
        lines.append(f"\u274c {err}")
    lines.append("")
    lines.append(f"\U0001f4ac *Cita:* _{entry.get('quote', '')}_")
    lines.append("")
    lines.append("\u2500" * 30)
    lines.append("")
    lines.append(WEALTH_ROUTINE)
    return "\n".join(lines)


def format_friday(entry: dict, week: int) -> str:
    """Ingeniero IA."""
    lines = [
        f"\U0001f916 *VIERNES - INGENIERO IA*",
        f"\U0001f4bb Semana {week}",
        "",
        f"\U0001f527 *Claude Code Tip:*",
        f"*{entry.get('tip_title', '')}*",
        "",
        entry.get("tip_description", ""),
        "",
    ]
    if entry.get("code_example"):
        lines.append("```")
        lines.append(entry["code_example"])
        lines.append("```")
        lines.append("")
    lines.append(f"\U0001f4a1 *Idea de Negocio IA:*")
    lines.append(f"*{entry.get('business_idea_title', '')}*")
    lines.append("")
    lines.append(entry.get("business_idea_description", ""))
    lines.append("")
    lines.append("\U0001f4b0 *Modelo de monetizacion:*")
    lines.append(entry.get("monetization", ""))
    lines.append("")
    lines.append("\U0001f3af *Primer paso para implementar:*")
    lines.append(entry.get("first_step", ""))
    lines.append("")
    lines.append(f"\U0001f4ca *Potencial de mercado:* {entry.get('market_potential', '')}")
    lines.append("")
    lines.append(f"\U0001f4ac *Cita:* _{entry.get('quote', '')}_")
    lines.append("")
    lines.append("\u2500" * 30)
    lines.append("")
    lines.append(WEALTH_ROUTINE)
    return "\n".join(lines)


def format_saturday(entry: dict, week: int) -> str:
    """Influencia y Carisma."""
    lines = [
        f"\U0001f3ad *SABADO - INFLUENCIA Y CARISMA*",
        f"\U0001f91d Semana {week}",
        "",
        f"\U0001f3af *Habilidad:* *{entry.get('skill_name', '')}*",
        f"\U0001f4d6 Basado en: {entry.get('source', '')}",
        "",
        f"\U0001f4dd *Concepto:*",
        entry.get("concept", ""),
        "",
        "\U0001f9ea *Ejercicio de dinamica social:*",
        entry.get("exercise", ""),
        "",
        "\U0001f5e3\ufe0f *Frases para practicar:*",
    ]
    for phrase in entry.get("practice_phrases", []):
        lines.append(f"  \U0001f4ac \"{phrase}\"")
    lines.append("")
    lines.append("\U0001f4ca *Indicadores de progreso:*")
    for indicator in entry.get("progress_indicators", []):
        lines.append(f"\u2705 {indicator}")
    lines.append("")
    lines.append(f"\u26a0\ufe0f *Advertencia:* {entry.get('warning', '')}")
    lines.append("")
    lines.append(f"\U0001f4ac *Cita:* _{entry.get('quote', '')}_")
    lines.append("")
    lines.append("\u2500" * 30)
    lines.append("")
    lines.append(WEALTH_ROUTINE)
    return "\n".join(lines)


def format_sunday(entry: dict, week: int) -> str:
    """Reflexion Espiritual + Visualizacion."""
    lines = [
        f"\U0001f54a\ufe0f *DOMINGO - REFLEXION ESPIRITUAL*",
        f"\u2728 Semana {week}",
        "",
        f"\U0001f4d6 *Tema:* *{entry.get('theme', '')}*",
        "",
        f"\U0001f9d8 *Reflexion:*",
        entry.get("reflection", ""),
        "",
        "\U0001f52e *Visualizacion guiada semanal:*",
        entry.get("visualization", ""),
        "",
        "\U0001f4dd *Preguntas para journaling:*",
    ]
    for q in entry.get("journal_questions", []):
        lines.append(f"\u2753 {q}")
    lines.append("")
    lines.append("\U0001f4cb *Revision semanal:*")
    lines.append(entry.get("weekly_review", ""))
    lines.append("")
    lines.append("\U0001f3af *Intencion para la proxima semana:*")
    lines.append(entry.get("next_week_intention", ""))
    lines.append("")
    lines.append(f"\U0001f4ac *Cita espiritual:* _{entry.get('quote', '')}_")
    lines.append("")
    lines.append("\U0001f64f *Afirmaciones de cierre:*")
    for aff in entry.get("closing_affirmations", []):
        lines.append(f"\u2728 _{aff}_")
    lines.append("")
    lines.append("\u2500" * 30)
    lines.append("")
    lines.append(WEALTH_ROUTINE)
    return "\n".join(lines)


FORMATTERS = {
    0: format_monday,
    1: format_tuesday,
    2: format_wednesday,
    3: format_thursday,
    4: format_friday,
    5: format_saturday,
    6: format_sunday,
}


def build_message(db: dict, day_index: int, week: int) -> str:
    """Build the full formatted message for a given day and week."""
    content = pick_content(db, day_index, week)
    if not content:
        return f"No hay contenido disponible para {DAY_NAMES[day_index]}, semana {week}."
    formatter = FORMATTERS[day_index]
    return formatter(content, week)


# ---------------------------------------------------------------------------
# Telegram sending
# ---------------------------------------------------------------------------


async def send_message(token: str, chat_id: str, text: str) -> None:
    """Send a message via Telegram Bot API."""
    bot = telegram.Bot(token=token)

    # Telegram has a 4096 char limit per message. Split if needed.
    MAX_LEN = 4000
    chunks = []
    while len(text) > MAX_LEN:
        # Find a good split point (newline near the limit)
        split_at = text.rfind("\n", 0, MAX_LEN)
        if split_at == -1:
            split_at = MAX_LEN
        chunks.append(text[:split_at])
        text = text[split_at:].lstrip("\n")
    chunks.append(text)

    for i, chunk in enumerate(chunks):
        try:
            await bot.send_message(
                chat_id=chat_id,
                text=chunk,
                parse_mode=ParseMode.MARKDOWN,
            )
            logger.info("Sent message chunk %d/%d (%d chars)", i + 1, len(chunks), len(chunk))
        except telegram.error.TelegramError as exc:
            logger.error("Failed to send message chunk %d: %s", i + 1, exc)
            # Retry without markdown in case of parse errors
            try:
                await bot.send_message(chat_id=chat_id, text=chunk)
                logger.info("Sent chunk %d as plain text (fallback)", i + 1)
            except telegram.error.TelegramError as exc2:
                logger.error("Plain text fallback also failed: %s", exc2)
                raise


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Telegram Bot - Daily Wealth & Success Summaries"
    )
    parser.add_argument(
        "--day",
        type=int,
        choices=range(7),
        default=None,
        help="Override day of week (0=Monday, 6=Sunday)",
    )
    parser.add_argument(
        "--week",
        type=int,
        default=None,
        help="Override week number (1-53)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print message to stdout without sending",
    )
    parser.add_argument(
        "--content-db",
        type=str,
        default=CONTENT_DB_PATH,
        help="Path to JSON content database",
    )
    return parser.parse_args()


async def main() -> None:
    args = parse_args()

    # Determine day and week
    today = date.today()
    day_index = args.day if args.day is not None else get_day_of_week(today)
    week = args.week if args.week is not None else get_week_number(today)

    day_name = DAY_NAMES[day_index]
    theme = DAY_THEMES[day_name]
    emoji = DAY_EMOJIS[day_name]

    logger.info(
        "Preparing message: %s %s (%s) - Week %d",
        emoji, day_name.capitalize(), theme, week,
    )

    # Load content
    db = load_content_db(args.content_db)
    message = build_message(db, day_index, week)

    if args.dry_run:
        print("\n" + "=" * 60)
        print(f"DRY RUN - {day_name.upper()} Week {week}")
        print("=" * 60)
        print(message)
        print("=" * 60)
        print(f"Message length: {len(message)} chars")
        return

    # Validate env vars
    if not BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN environment variable is not set")
        sys.exit(1)
    if not CHAT_ID:
        logger.error("TELEGRAM_CHAT_ID environment variable is not set")
        sys.exit(1)

    await send_message(BOT_TOKEN, CHAT_ID, message)
    logger.info("Daily message sent successfully.")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
