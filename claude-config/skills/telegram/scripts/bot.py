#!/usr/bin/env python3
"""
Telegram Bot powered by Claude AI.
Polls for messages and responds using the Anthropic API.
Run this script on your PC to keep the bot active.
"""

import json
import os
import sys
import time
import signal

import anthropic
import httpx

# Configuration
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
ALLOWED_CHAT_IDS = os.environ.get("ALLOWED_CHAT_IDS", "")

BOT_API = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"
CLAUDE_MODEL = "claude-sonnet-4-20250514"
MAX_TOKENS = 4096

# Conversation history per chat (in-memory)
conversations: dict[int, list] = {}
MAX_HISTORY = 20  # messages per chat

SYSTEM_PROMPT = """Eres Paulsito, el asistente personal de Pablo Agusto via Telegram.
Responde de forma concisa y directa. Usa el mismo idioma que el usuario.
Si te escriben en español, responde en español. Si en inglés, en inglés.
Puedes usar emojis cuando sea apropiado para Telegram."""

running = True


def signal_handler(sig, frame):
    global running
    print("\nApagando bot...")
    running = False


def telegram_request(method: str, params: dict = None) -> dict:
    """Make a request to Telegram Bot API."""
    try:
        resp = httpx.post(f"{BOT_API}/{method}", json=params or {}, timeout=30)
        return resp.json()
    except Exception as e:
        print(f"Error Telegram API: {e}")
        return {"ok": False, "error": str(e)}


def get_updates(offset: int = None) -> list:
    """Poll for new messages."""
    params = {"timeout": 30, "allowed_updates": ["message"]}
    if offset is not None:
        params["offset"] = offset
    result = telegram_request("getUpdates", params)
    if result.get("ok"):
        return result.get("result", [])
    return []


def send_message(chat_id: int, text: str, reply_to: int = None):
    """Send a message, splitting if too long for Telegram (4096 char limit)."""
    chunks = [text[i:i+4000] for i in range(0, len(text), 4000)]
    for chunk in chunks:
        params = {
            "chat_id": chat_id,
            "text": chunk,
            "parse_mode": "Markdown",
        }
        if reply_to:
            params["reply_to_message_id"] = reply_to
        result = telegram_request("sendMessage", params)
        if not result.get("ok"):
            # Retry without Markdown if it fails
            params.pop("parse_mode")
            telegram_request("sendMessage", params)


def send_typing(chat_id: int):
    """Show 'typing...' indicator."""
    telegram_request("sendChatAction", {"chat_id": chat_id, "action": "typing"})


def ask_claude(chat_id: int, user_message: str) -> str:
    """Send message to Claude and get response."""
    # Manage conversation history
    if chat_id not in conversations:
        conversations[chat_id] = []

    conversations[chat_id].append({"role": "user", "content": user_message})

    # Trim history
    if len(conversations[chat_id]) > MAX_HISTORY:
        conversations[chat_id] = conversations[chat_id][-MAX_HISTORY:]

    try:
        client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)
        response = client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=MAX_TOKENS,
            system=SYSTEM_PROMPT,
            messages=conversations[chat_id],
        )
        assistant_text = response.content[0].text
        conversations[chat_id].append({"role": "assistant", "content": assistant_text})
        return assistant_text
    except anthropic.APIError as e:
        return f"Error de API: {e.message}"
    except Exception as e:
        return f"Error: {str(e)}"


def is_allowed(chat_id: int) -> bool:
    """Check if chat is allowed."""
    if not ALLOWED_CHAT_IDS:
        return True  # No restriction
    allowed = [int(x.strip()) for x in ALLOWED_CHAT_IDS.split(",") if x.strip()]
    return chat_id in allowed


def handle_command(chat_id: int, text: str) -> str | None:
    """Handle bot commands. Returns response or None."""
    if text == "/start":
        return "Hola! Soy Paulsito, tu asistente con Claude AI. Escribime lo que necesites."
    elif text == "/clear":
        conversations.pop(chat_id, None)
        return "Conversacion borrada. Empezamos de cero."
    elif text == "/help":
        return (
            "Comandos:\n"
            "/start - Iniciar bot\n"
            "/clear - Borrar historial de conversacion\n"
            "/help - Ver comandos\n\n"
            "Escribime cualquier cosa y te respondo con Claude AI."
        )
    return None


def main():
    global running

    if not TELEGRAM_TOKEN:
        print("Error: Set TELEGRAM_BOT_TOKEN environment variable")
        sys.exit(1)
    if not ANTHROPIC_KEY:
        print("Error: Set ANTHROPIC_API_KEY environment variable")
        sys.exit(1)

    signal.signal(signal.SIGINT, signal_handler)

    # Verify bot
    me = telegram_request("getMe")
    if not me.get("ok"):
        print(f"Error: Invalid bot token")
        sys.exit(1)

    bot_name = me["result"]["username"]
    print(f"Bot @{bot_name} activo! Esperando mensajes...")
    print("Presiona Ctrl+C para apagar")

    offset = None

    while running:
        try:
            updates = get_updates(offset)

            for update in updates:
                offset = update["update_id"] + 1
                msg = update.get("message")
                if not msg or "text" not in msg:
                    continue

                chat_id = msg["chat"]["id"]
                text = msg["text"].strip()
                user = msg.get("from", {})
                name = user.get("first_name", "Unknown")

                if not is_allowed(chat_id):
                    send_message(chat_id, "No autorizado.")
                    continue

                print(f"[{name}] {text[:80]}")

                # Check commands
                cmd_response = handle_command(chat_id, text)
                if cmd_response:
                    send_message(chat_id, cmd_response, msg["message_id"])
                    continue

                # Send to Claude
                send_typing(chat_id)
                response = ask_claude(chat_id, text)
                send_message(chat_id, response, msg["message_id"])
                print(f"[Bot] {response[:80]}")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

    print("Bot apagado.")


if __name__ == "__main__":
    main()
