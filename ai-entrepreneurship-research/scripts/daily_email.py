#!/usr/bin/env python3
"""
Daily Email - Riqueza y Exito Diario
=====================================
Envia correos HTML diarios con contenido motivacional/educativo
usando el mismo sistema de rotacion que telegram_bot.py.

Horario:
    Lunes:     Reprogramacion Mental (Metodo Silva)
    Martes:    Resumen de Libro (Top 100 libros)
    Miercoles: Biografia Inspiradora (Perfil de persona exitosa)
    Jueves:    Maestria en Ventas (Tecnica + ejercicio)
    Viernes:   Ingeniero IA (Claude Code tip + idea de negocio IA)
    Sabado:    Influencia y Carisma (Ejercicio de dinamica social)
    Domingo:   Reflexion Espiritual + Visualizacion semanal

Uso:
    # Enviar el correo de hoy
    python daily_email.py

    # Enviar correo para un dia especifico (0=Lunes, 6=Domingo)
    python daily_email.py --day 0

    # Enviar correo para una semana especifica (1-52)
    python daily_email.py --week 5

    # Ejecucion en seco (genera HTML en archivo sin enviar)
    python daily_email.py --dry-run

    # Cron (diario a las 8:00 AM):
    # 0 8 * * * cd /path/to/scripts && python daily_email.py >> /var/log/daily_email.log 2>&1

Variables de Entorno:
    SMTP_HOST      - Servidor SMTP (default: smtp.gmail.com)
    SMTP_PORT      - Puerto SMTP (default: 587)
    SMTP_USER      - Usuario SMTP (correo electronico)
    SMTP_PASSWORD   - Contrasena SMTP o contrasena de aplicacion
    EMAIL_FROM     - Direccion del remitente
    EMAIL_TO       - Direccion(es) del destinatario (separadas por coma)
    CONTENT_DB_PATH - Ruta a daily_content.json (opcional)
    TZ             - Zona horaria (recomendado: America/Mexico_City)
"""

import argparse
import json
import logging
import os
import smtplib
import sys
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from typing import Optional

try:
    from jinja2 import Environment, FileSystemLoader, TemplateNotFound
except ImportError:
    print("Error: Jinja2 no esta instalado. Ejecuta: pip install Jinja2")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Configuracion
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_CONTENT_PATH = SCRIPT_DIR / "daily_content.json"
TEMPLATE_FILE = "email_template.html"

SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER", "")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "")
EMAIL_FROM = os.environ.get("EMAIL_FROM", "")
EMAIL_TO = os.environ.get("EMAIL_TO", "")
CONTENT_DB_PATH = os.environ.get("CONTENT_DB_PATH", str(DEFAULT_CONTENT_PATH))

DAY_NAMES = [
    "monday", "tuesday", "wednesday", "thursday",
    "friday", "saturday", "sunday",
]

DAY_NAMES_ES = [
    "Lunes", "Martes", "Miercoles", "Jueves",
    "Viernes", "Sabado", "Domingo",
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
    "monday": "\U0001f9e0",
    "tuesday": "\U0001f4da",
    "wednesday": "\U0001f31f",
    "thursday": "\U0001f4b0",
    "friday": "\U0001f916",
    "saturday": "\U0001f3ad",
    "sunday": "\U0001f54a\ufe0f",
}

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("daily_email")

# ---------------------------------------------------------------------------
# Carga de contenido (misma logica que telegram_bot.py)
# ---------------------------------------------------------------------------


def load_content_db(path: str) -> dict:
    """Carga la base de datos JSON de contenido."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error("Base de datos de contenido no encontrada en %s", path)
        sys.exit(1)
    except json.JSONDecodeError as exc:
        logger.error("JSON invalido en base de datos de contenido: %s", exc)
        sys.exit(1)


def get_week_number(target_date: Optional[date] = None) -> int:
    """Retorna el numero de semana ISO (1-53)."""
    d = target_date or date.today()
    return d.isocalendar()[1]


def get_day_of_week(target_date: Optional[date] = None) -> int:
    """Retorna el dia de la semana como int (0=Lunes, 6=Domingo)."""
    d = target_date or date.today()
    return d.weekday()


def pick_content(db: dict, day_index: int, week: int) -> dict:
    """
    Selecciona el contenido correcto para el dia y semana dados.

    La estructura JSON es: { "monday": [ {entrada1}, {entrada2}, ... ], ... }
    Rota entre entradas usando el numero de semana modulo el total de entradas.
    """
    day_key = DAY_NAMES[day_index]
    entries = db.get(day_key, [])
    if not entries:
        logger.warning("No hay entradas de contenido para %s", day_key)
        return {}
    idx = (week - 1) % len(entries)
    return entries[idx]


# ---------------------------------------------------------------------------
# Preparacion de variables para la plantilla
# ---------------------------------------------------------------------------

RUTINA_ITEMS = [
    ("05:30", "Despertar + agua con limon"),
    ("05:45", "15 min meditacion Silva (nivel alfa)"),
    ("06:00", "Visualizacion de metas (pantalla mental)"),
    ("06:15", "Journaling: 3 gratitudes + intencion del dia"),
    ("06:30", "Ejercicio fisico (45 min)"),
    ("07:15", "Lectura (30 min minimo)"),
    ("07:45", "Desayuno consciente"),
    ("08:00", "Bloque de trabajo profundo #1 (2h)"),
    ("10:00", "Revisar metricas / KPIs del negocio"),
    ("10:30", "Bloque de trabajo profundo #2 (2h)"),
    ("12:30", "Networking / seguimiento de contactos"),
    ("13:00", "Almuerzo + podcast educativo"),
    ("14:00", "Bloque creativo / contenido (2h)"),
    ("16:00", "Revision y planificacion del dia siguiente"),
    ("16:30", "Aprendizaje de habilidad nueva (1h)"),
    ("17:30", "Tiempo personal / familia"),
    ("21:00", "Reflexion nocturna + programacion del sueno (Silva)"),
    ("21:30", "Lectura ligera / descanso"),
    ("22:00", "Dormir (8h para rendimiento optimo)"),
]


def build_template_context(entry: dict, day_index: int, week: int) -> dict:
    """
    Construye el diccionario de contexto para la plantilla Jinja2.
    Extrae campos comunes y especificos del dia.
    """
    day_key = DAY_NAMES[day_index]
    day_name_es = DAY_NAMES_ES[day_index]
    theme = DAY_THEMES[day_key]
    emoji = DAY_EMOJIS[day_key]
    today = date.today()

    ctx = {
        # Generales
        "fecha": today.strftime("%d de %B de %Y"),
        "fecha_corta": today.strftime("%d/%m/%Y"),
        "dia_nombre": day_name_es,
        "dia_key": day_key,
        "tema": theme,
        "emoji": emoji,
        "semana": week,
        "anio": today.year,
        "rutina_items": RUTINA_ITEMS,

        # Campos comunes (con valores por defecto)
        "afirmacion": entry.get("affirmation", ""),
        "cita": entry.get("quote", ""),

        # Lunes - Reprogramacion Mental
        "tecnica_nombre": entry.get("technique_name", ""),
        "tecnica_descripcion": entry.get("technique_description", ""),
        "pasos": entry.get("steps", []),
        "duracion": entry.get("duration", "15-20 min"),
        "ciencia": entry.get("science", ""),

        # Martes - Resumen de Libro
        "libro_titulo": entry.get("title", ""),
        "libro_autor": entry.get("author", ""),
        "libro_categoria": entry.get("category", ""),
        "libro_resumen": entry.get("summary", ""),
        "ideas_clave": entry.get("key_ideas", []),
        "acciones": entry.get("actions", []),
        "aplicacion_negocio": entry.get("business_application", ""),

        # Miercoles - Biografia Inspiradora
        "persona_nombre": entry.get("name", ""),
        "persona_titulo": entry.get("title", ""),
        "patrimonio": entry.get("net_worth", ""),
        "historia": entry.get("story", ""),
        "lecciones": entry.get("lessons", []),
        "habitos": entry.get("habits", []),
        "ejercicio": entry.get("exercise", ""),

        # Jueves - Maestria en Ventas
        "ventas_tecnica": entry.get("technique_name", ""),
        "ventas_fuente": entry.get("source", ""),
        "ventas_descripcion": entry.get("description", ""),
        "script_lines": entry.get("script_lines", []),
        "psicologia": entry.get("psychology", ""),
        "ventas_ejercicio": entry.get("exercise", ""),
        "errores_comunes": entry.get("common_mistakes", []),

        # Viernes - Ingeniero IA
        "tip_titulo": entry.get("tip_title", ""),
        "tip_descripcion": entry.get("tip_description", ""),
        "codigo_ejemplo": entry.get("code_example", ""),
        "idea_negocio_titulo": entry.get("business_idea_title", ""),
        "idea_negocio_descripcion": entry.get("business_idea_description", ""),
        "monetizacion": entry.get("monetization", ""),
        "primer_paso": entry.get("first_step", ""),
        "potencial_mercado": entry.get("market_potential", ""),

        # Sabado - Influencia y Carisma
        "habilidad_nombre": entry.get("skill_name", ""),
        "habilidad_fuente": entry.get("source", ""),
        "concepto": entry.get("concept", ""),
        "dinamica_ejercicio": entry.get("exercise", ""),
        "frases_practicar": entry.get("practice_phrases", []),
        "indicadores_progreso": entry.get("progress_indicators", []),
        "advertencia": entry.get("warning", ""),

        # Domingo - Reflexion Espiritual
        "tema_espiritual": entry.get("theme", ""),
        "reflexion": entry.get("reflection", ""),
        "visualizacion": entry.get("visualization", ""),
        "preguntas_journal": entry.get("journal_questions", []),
        "revision_semanal": entry.get("weekly_review", ""),
        "intencion_proxima_semana": entry.get("next_week_intention", ""),
        "afirmaciones_cierre": entry.get("closing_affirmations", []),
    }

    # Accion del dia: varía segun el dia
    accion = ""
    if day_key == "monday":
        accion = f"Practica la tecnica '{ctx['tecnica_nombre']}' durante {ctx['duracion']} hoy."
    elif day_key == "tuesday":
        accion = f"Lee al menos un capitulo de '{ctx['libro_titulo']}' y aplica una idea clave."
    elif day_key == "wednesday":
        accion = ctx.get("ejercicio", "Reflexiona sobre las lecciones de hoy.")
    elif day_key == "thursday":
        accion = ctx.get("ventas_ejercicio", "Practica el script de ventas con alguien de confianza.")
    elif day_key == "friday":
        accion = ctx.get("primer_paso", "Implementa el tip de Claude Code en tu proyecto actual.")
    elif day_key == "saturday":
        accion = ctx.get("dinamica_ejercicio", "Practica las frases de influencia en una conversacion real.")
    elif day_key == "sunday":
        accion = ctx.get("intencion_proxima_semana", "Define tu intencion para la proxima semana.")
    ctx["accion_del_dia"] = accion

    # Libro recomendado (solo aplica martes, pero siempre lo incluimos)
    if day_key == "tuesday" and ctx["libro_titulo"]:
        ctx["libro_recomendado"] = f"{ctx['libro_titulo']} - {ctx['libro_autor']}"
    else:
        ctx["libro_recomendado"] = ""

    return ctx


# ---------------------------------------------------------------------------
# Renderizado de plantilla
# ---------------------------------------------------------------------------


def render_email(context: dict) -> str:
    """Renderiza la plantilla HTML con Jinja2."""
    env = Environment(
        loader=FileSystemLoader(str(SCRIPT_DIR)),
        autoescape=True,
    )
    try:
        template = env.get_template(TEMPLATE_FILE)
    except TemplateNotFound:
        logger.error("Plantilla no encontrada: %s/%s", SCRIPT_DIR, TEMPLATE_FILE)
        sys.exit(1)

    return template.render(**context)


# ---------------------------------------------------------------------------
# Envio de correo
# ---------------------------------------------------------------------------


def send_email(
    smtp_host: str,
    smtp_port: int,
    smtp_user: str,
    smtp_password: str,
    email_from: str,
    email_to: str,
    subject: str,
    html_body: str,
) -> None:
    """Envia un correo HTML via SMTP con TLS."""
    recipients = [addr.strip() for addr in email_to.split(",") if addr.strip()]

    msg = MIMEMultipart("alternative")
    msg["From"] = email_from
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = subject

    # Version texto plano (fallback basico)
    text_part = MIMEText(
        "Tu navegador no soporta HTML. Abre este correo en un cliente compatible.",
        "plain",
        "utf-8",
    )
    html_part = MIMEText(html_body, "html", "utf-8")

    msg.attach(text_part)
    msg.attach(html_part)

    try:
        logger.info("Conectando a %s:%d ...", smtp_host, smtp_port)
        with smtplib.SMTP(smtp_host, smtp_port, timeout=30) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(smtp_user, smtp_password)
            server.sendmail(email_from, recipients, msg.as_string())
        logger.info(
            "Correo enviado exitosamente a %s (%d destinatarios)",
            ", ".join(recipients),
            len(recipients),
        )
    except smtplib.SMTPAuthenticationError:
        logger.error(
            "Error de autenticacion SMTP. Verifica SMTP_USER y SMTP_PASSWORD. "
            "Para Gmail, usa una contrasena de aplicacion: "
            "https://myaccount.google.com/apppasswords"
        )
        sys.exit(1)
    except smtplib.SMTPException as exc:
        logger.error("Error SMTP al enviar correo: %s", exc)
        sys.exit(1)
    except OSError as exc:
        logger.error("Error de conexion: %s", exc)
        sys.exit(1)


# ---------------------------------------------------------------------------
# Principal
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Correo Diario - Riqueza y Exito"
    )
    parser.add_argument(
        "--day",
        type=int,
        choices=range(7),
        default=None,
        help="Dia de la semana (0=Lunes, 6=Domingo)",
    )
    parser.add_argument(
        "--week",
        type=int,
        default=None,
        help="Numero de semana (1-53)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Genera HTML en archivo sin enviar correo",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Ruta del archivo de salida para --dry-run (default: dry_run_email.html)",
    )
    parser.add_argument(
        "--content-db",
        type=str,
        default=CONTENT_DB_PATH,
        help="Ruta a la base de datos JSON de contenido",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # Determinar dia y semana
    today = date.today()
    day_index = args.day if args.day is not None else get_day_of_week(today)
    week = args.week if args.week is not None else get_week_number(today)

    day_key = DAY_NAMES[day_index]
    day_name_es = DAY_NAMES_ES[day_index]
    theme = DAY_THEMES[day_key]
    emoji = DAY_EMOJIS[day_key]

    logger.info(
        "Preparando correo: %s %s (%s) - Semana %d",
        emoji, day_name_es, theme, week,
    )

    # Cargar contenido
    db = load_content_db(args.content_db)
    entry = pick_content(db, day_index, week)

    if not entry:
        logger.error("No hay contenido disponible para %s, semana %d", day_key, week)
        sys.exit(1)

    # Construir contexto y renderizar
    context = build_template_context(entry, day_index, week)
    html_body = render_email(context)

    subject = f"{emoji} {day_name_es}: {theme} | Semana {week}"

    if args.dry_run:
        output_path = args.output or str(SCRIPT_DIR / "dry_run_email.html")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_body)
        logger.info("HTML generado en: %s", output_path)
        logger.info("Asunto: %s", subject)
        logger.info("Longitud del HTML: %d caracteres", len(html_body))
        print(f"\nEjecucion en seco completada.")
        print(f"Archivo: {output_path}")
        print(f"Asunto: {subject}")
        return

    # Validar variables de entorno
    missing = []
    if not SMTP_USER:
        missing.append("SMTP_USER")
    if not SMTP_PASSWORD:
        missing.append("SMTP_PASSWORD")
    if not EMAIL_FROM:
        missing.append("EMAIL_FROM")
    if not EMAIL_TO:
        missing.append("EMAIL_TO")

    if missing:
        logger.error(
            "Variables de entorno faltantes: %s", ", ".join(missing)
        )
        sys.exit(1)

    send_email(
        smtp_host=SMTP_HOST,
        smtp_port=SMTP_PORT,
        smtp_user=SMTP_USER,
        smtp_password=SMTP_PASSWORD,
        email_from=EMAIL_FROM,
        email_to=EMAIL_TO,
        subject=subject,
        html_body=html_body,
    )
    logger.info("Correo diario enviado exitosamente.")


if __name__ == "__main__":
    main()
