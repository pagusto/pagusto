# Configuracion del Bot de Telegram - Resumenes Diarios de Riqueza

## Paso 1: Crear el Bot en Telegram

1. Abre Telegram y busca `@BotFather`
2. Envia el comando `/newbot`
3. Elige un nombre para tu bot (ejemplo: "Mi Coach de Riqueza")
4. Elige un username (ejemplo: `mi_coach_riqueza_bot`)
5. BotFather te dara un **token**. Guardalo de forma segura.
   - Ejemplo: `7123456789:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

## Paso 2: Obtener tu Chat ID

### Opcion A: Chat personal
1. Busca `@userinfobot` en Telegram
2. Enviale cualquier mensaje
3. Te respondera con tu **Chat ID** (un numero como `123456789`)

### Opcion B: Grupo o canal
1. Agrega tu bot al grupo/canal
2. Envia un mensaje en el grupo
3. Visita: `https://api.telegram.org/bot<TU_TOKEN>/getUpdates`
4. Busca el campo `"chat": {"id": -100XXXXXXXXXX}` en la respuesta JSON
5. El numero (incluyendo el signo negativo) es tu Chat ID

## Paso 3: Configurar variables de entorno

### Linux / macOS
```bash
# Agrega estas lineas a ~/.bashrc o ~/.zshrc
export TELEGRAM_BOT_TOKEN="7123456789:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export TELEGRAM_CHAT_ID="123456789"

# Recarga el perfil
source ~/.bashrc
```

### Alternativa: Archivo .env
```bash
# Crea un archivo .env en el directorio del script
echo 'TELEGRAM_BOT_TOKEN=7123456789:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' > .env
echo 'TELEGRAM_CHAT_ID=123456789' >> .env

# Asegurate de que .env esta en .gitignore
echo '.env' >> .gitignore
```

## Paso 4: Instalar dependencias

```bash
cd /home/user/pagusto/ai-entrepreneurship-research/scripts
pip install -r requirements.txt
```

## Paso 5: Probar el bot

```bash
# Prueba sin enviar (imprime en consola)
python telegram_bot.py --dry-run

# Prueba enviando el mensaje de hoy
python telegram_bot.py

# Prueba un dia especifico (0=Lunes, 6=Domingo)
python telegram_bot.py --day 0 --week 1 --dry-run
```

## Paso 6: Configurar ejecucion automatica con Cron

```bash
# Abre el editor de cron
crontab -e

# Agrega esta linea para ejecutar todos los dias a las 6:00 AM
0 6 * * * cd /home/user/pagusto/ai-entrepreneurship-research/scripts && /usr/bin/python3 telegram_bot.py >> /var/log/telegram_bot.log 2>&1
```

### Nota importante sobre cron y variables de entorno

Cron no carga tu perfil de shell, asi que necesitas incluir las variables directamente:

```bash
# Opcion 1: Variables en la linea de cron
0 6 * * * TELEGRAM_BOT_TOKEN="tu_token" TELEGRAM_CHAT_ID="tu_chat_id" cd /home/user/pagusto/ai-entrepreneurship-research/scripts && /usr/bin/python3 telegram_bot.py >> /var/log/telegram_bot.log 2>&1

# Opcion 2: Cargar desde archivo (mas seguro)
0 6 * * * . /home/user/.telegram_env && cd /home/user/pagusto/ai-entrepreneurship-research/scripts && /usr/bin/python3 telegram_bot.py >> /var/log/telegram_bot.log 2>&1
```

## Paso 7: Verificar que funciona

```bash
# Revisa los logs
tail -f /var/log/telegram_bot.log

# Revisa que cron esta configurado
crontab -l
```

## Estructura de contenido

El bot lee su contenido de `daily_content.json`. Para agregar mas contenido:

1. Abre `daily_content.json`
2. Cada dia de la semana tiene un array de entradas
3. El bot rota automaticamente por semana (semana 1 = entrada 1, semana 2 = entrada 2, etc.)
4. Cuando se agotan las entradas, vuelve a empezar desde la primera

### Ejemplo de estructura:
```json
{
  "monday": [
    {
      "technique_name": "Nombre de la tecnica",
      "technique_description": "Descripcion detallada...",
      "steps": ["Paso 1", "Paso 2", "Paso 3"],
      "duration": "15 min",
      "science": "Explicacion cientifica...",
      "affirmation": "Afirmacion del dia",
      "quote": "Cita motivacional"
    }
  ]
}
```

## Solucion de problemas

| Problema | Solucion |
|----------|----------|
| "TELEGRAM_BOT_TOKEN not set" | Verifica que la variable de entorno este configurada |
| "Chat not found" | Asegurate de que el bot esta agregado al chat/grupo |
| Mensaje no llega | Revisa que el Chat ID sea correcto (incluye el signo - para grupos) |
| Error de formato | El bot intentara reenviar sin formato Markdown automaticamente |
| Cron no ejecuta | Verifica con `crontab -l` y revisa `/var/log/syslog` |

## Seguridad

- **NUNCA** compartas tu token de bot publicamente
- **NUNCA** hagas commit de archivos `.env` a git
- Considera usar un gestor de secretos para produccion
- El token permite control total del bot, tratalo como una contrasena
