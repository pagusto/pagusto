#!/usr/bin/env bash
# =============================================================================
# Configuracion de Cron - Telegram Bot y Correo Diario
# =============================================================================
# Configura los cron jobs para enviar mensajes automaticos:
#   - Telegram Bot: 6:00 AM diario
#   - Correo Diario: 8:00 AM diario
#
# Uso:
#   chmod +x crontab_setup.sh
#   ./crontab_setup.sh
#
# Para personalizar zona horaria:
#   TIMEZONE="America/Bogota" ./crontab_setup.sh
#
# Para personalizar horarios:
#   TELEGRAM_HOUR=7 EMAIL_HOUR=9 ./crontab_setup.sh
# =============================================================================

set -euo pipefail

# ---------------------------------------------------------------------------
# Configuracion
# ---------------------------------------------------------------------------

# Directorio donde viven los scripts
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Zona horaria (configurable via variable de entorno)
TIMEZONE="${TIMEZONE:-America/Mexico_City}"

# Horarios (configurable via variables de entorno)
TELEGRAM_HOUR="${TELEGRAM_HOUR:-6}"
TELEGRAM_MINUTE="${TELEGRAM_MINUTE:-0}"
EMAIL_HOUR="${EMAIL_HOUR:-8}"
EMAIL_MINUTE="${EMAIL_MINUTE:-0}"

# Directorio de logs
LOG_DIR="${LOG_DIR:-/var/log/daily-messages}"

# Ruta al interprete de Python
PYTHON_BIN="${PYTHON_BIN:-$(which python3 2>/dev/null || which python 2>/dev/null || echo "python3")}"

# Archivos de log
TELEGRAM_LOG="${LOG_DIR}/telegram_bot.log"
EMAIL_LOG="${LOG_DIR}/daily_email.log"

# Marcador para identificar nuestros cron jobs
CRON_MARKER="# daily-wealth-messages"

# ---------------------------------------------------------------------------
# Colores para la salida
# ---------------------------------------------------------------------------

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # Sin color

# ---------------------------------------------------------------------------
# Funciones auxiliares
# ---------------------------------------------------------------------------

info()    { echo -e "${GREEN}[INFO]${NC}    $*"; }
warn()    { echo -e "${YELLOW}[AVISO]${NC}  $*"; }
error()   { echo -e "${RED}[ERROR]${NC}  $*"; }
header()  { echo -e "\n${BLUE}========================================${NC}"; echo -e "${BLUE}  $*${NC}"; echo -e "${BLUE}========================================${NC}\n"; }

# ---------------------------------------------------------------------------
# Verificaciones previas
# ---------------------------------------------------------------------------

header "Configuracion de Cron Jobs"

info "Directorio de scripts: ${SCRIPT_DIR}"
info "Zona horaria: ${TIMEZONE}"
info "Telegram: ${TELEGRAM_HOUR}:$(printf '%02d' ${TELEGRAM_MINUTE}) diario"
info "Correo:   ${EMAIL_HOUR}:$(printf '%02d' ${EMAIL_MINUTE}) diario"
info "Python:   ${PYTHON_BIN}"

# Verificar que los scripts existen
if [ ! -f "${SCRIPT_DIR}/telegram_bot.py" ]; then
    error "No se encontro telegram_bot.py en ${SCRIPT_DIR}"
    exit 1
fi

if [ ! -f "${SCRIPT_DIR}/daily_email.py" ]; then
    error "No se encontro daily_email.py en ${SCRIPT_DIR}"
    exit 1
fi

# Verificar que Python esta disponible
if ! command -v "${PYTHON_BIN}" &>/dev/null; then
    error "Python no encontrado en: ${PYTHON_BIN}"
    error "Instala Python 3 o define PYTHON_BIN con la ruta correcta."
    exit 1
fi

PYTHON_VERSION=$("${PYTHON_BIN}" --version 2>&1)
info "Version de Python: ${PYTHON_VERSION}"

# ---------------------------------------------------------------------------
# Crear directorio de logs
# ---------------------------------------------------------------------------

header "Creando directorio de logs"

if [ ! -d "${LOG_DIR}" ]; then
    if sudo mkdir -p "${LOG_DIR}" 2>/dev/null; then
        sudo chmod 755 "${LOG_DIR}"
        sudo chown "$(whoami):$(id -gn)" "${LOG_DIR}"
        info "Directorio creado: ${LOG_DIR}"
    else
        # Si no hay sudo, usar directorio en home
        LOG_DIR="${HOME}/.local/log/daily-messages"
        TELEGRAM_LOG="${LOG_DIR}/telegram_bot.log"
        EMAIL_LOG="${LOG_DIR}/daily_email.log"
        mkdir -p "${LOG_DIR}"
        warn "Sin permisos para /var/log. Usando: ${LOG_DIR}"
    fi
else
    info "Directorio de logs ya existe: ${LOG_DIR}"
fi

# Crear archivos de log si no existen
touch "${TELEGRAM_LOG}" 2>/dev/null || true
touch "${EMAIL_LOG}" 2>/dev/null || true
info "Log de Telegram: ${TELEGRAM_LOG}"
info "Log de Correo:   ${EMAIL_LOG}"

# ---------------------------------------------------------------------------
# Configurar zona horaria del sistema (informativo)
# ---------------------------------------------------------------------------

header "Zona horaria"

if [ -f /etc/timezone ]; then
    CURRENT_TZ=$(cat /etc/timezone 2>/dev/null || echo "desconocida")
    info "Zona horaria actual del sistema: ${CURRENT_TZ}"
fi

if [ "${CURRENT_TZ:-}" != "${TIMEZONE}" ]; then
    warn "La zona horaria del sistema puede diferir de la configurada."
    warn "Los cron jobs usaran TZ=${TIMEZONE} en sus lineas."
    info "Para cambiar la zona del sistema: sudo timedatectl set-timezone ${TIMEZONE}"
fi

# ---------------------------------------------------------------------------
# Construir lineas de cron
# ---------------------------------------------------------------------------

header "Configurando cron jobs"

# Linea de cron para Telegram Bot (6:00 AM)
CRON_TELEGRAM="${TELEGRAM_MINUTE} ${TELEGRAM_HOUR} * * * TZ=${TIMEZONE} cd ${SCRIPT_DIR} && ${PYTHON_BIN} telegram_bot.py >> ${TELEGRAM_LOG} 2>&1 ${CRON_MARKER}-telegram"

# Linea de cron para Correo Diario (8:00 AM)
CRON_EMAIL="${EMAIL_MINUTE} ${EMAIL_HOUR} * * * TZ=${TIMEZONE} cd ${SCRIPT_DIR} && ${PYTHON_BIN} daily_email.py >> ${EMAIL_LOG} 2>&1 ${CRON_MARKER}-email"

info "Cron Telegram: ${CRON_TELEGRAM}"
info "Cron Correo:   ${CRON_EMAIL}"

# ---------------------------------------------------------------------------
# Instalar cron jobs (preservando los existentes)
# ---------------------------------------------------------------------------

# Obtener crontab actual (ignorar error si esta vacia)
CURRENT_CRONTAB=$(crontab -l 2>/dev/null || echo "")

# Eliminar lineas anteriores con nuestro marcador
CLEAN_CRONTAB=$(echo "${CURRENT_CRONTAB}" | grep -v "${CRON_MARKER}" || true)

# Agregar nuevas lineas
NEW_CRONTAB="${CLEAN_CRONTAB}
${CRON_TELEGRAM}
${CRON_EMAIL}"

# Limpiar lineas vacias multiples
NEW_CRONTAB=$(echo "${NEW_CRONTAB}" | sed '/^$/N;/^\n$/d')

# Instalar nuevo crontab
echo "${NEW_CRONTAB}" | crontab -

info "Cron jobs instalados exitosamente."

# ---------------------------------------------------------------------------
# Mostrar crontab actual
# ---------------------------------------------------------------------------

header "Crontab actual"

crontab -l 2>/dev/null || echo "(vacio)"

# ---------------------------------------------------------------------------
# Resumen y proximos pasos
# ---------------------------------------------------------------------------

header "Resumen"

echo -e "${GREEN}Configuracion completada exitosamente.${NC}\n"
echo "Horario configurado:"
echo "  - Telegram Bot:  Todos los dias a las ${TELEGRAM_HOUR}:$(printf '%02d' ${TELEGRAM_MINUTE}) (${TIMEZONE})"
echo "  - Correo Diario: Todos los dias a las ${EMAIL_HOUR}:$(printf '%02d' ${EMAIL_MINUTE}) (${TIMEZONE})"
echo ""
echo "Archivos de log:"
echo "  - Telegram: ${TELEGRAM_LOG}"
echo "  - Correo:   ${EMAIL_LOG}"
echo ""
echo -e "${YELLOW}Proximos pasos:${NC}"
echo "  1. Configura las variables de entorno necesarias:"
echo "     - TELEGRAM_BOT_TOKEN y TELEGRAM_CHAT_ID (para Telegram)"
echo "     - SMTP_USER, SMTP_PASSWORD, EMAIL_FROM, EMAIL_TO (para correo)"
echo ""
echo "  2. Puedes agregar las variables en ~/.bashrc o en un archivo .env:"
echo "     export TELEGRAM_BOT_TOKEN='tu-token-aqui'"
echo "     export SMTP_USER='tucorreo@gmail.com'"
echo "     export SMTP_PASSWORD='tu-contrasena-de-aplicacion'"
echo "     export EMAIL_FROM='tucorreo@gmail.com'"
echo "     export EMAIL_TO='destinatario@ejemplo.com'"
echo ""
echo "  3. Prueba cada script manualmente primero:"
echo "     cd ${SCRIPT_DIR}"
echo "     ${PYTHON_BIN} telegram_bot.py --dry-run"
echo "     ${PYTHON_BIN} daily_email.py --dry-run"
echo ""
echo "  4. Para ver los logs en tiempo real:"
echo "     tail -f ${TELEGRAM_LOG}"
echo "     tail -f ${EMAIL_LOG}"
echo ""
echo "  5. Para desinstalar los cron jobs:"
echo "     crontab -l | grep -v '${CRON_MARKER}' | crontab -"
echo ""
