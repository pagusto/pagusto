---
name: telegram
description: |
  Interact with Telegram - send messages, read updates, list chats, send files/images via Bot API.
  Use when user asks to: send a Telegram message, read Telegram messages, list Telegram chats,
  send a file on Telegram, send an image on Telegram, or check Telegram bot status.
  Lightweight integration using Telegram Bot API with keyring token storage.
license: MIT
metadata:
  author: pagusto
  version: "1.0"
---

# Telegram

Lightweight Telegram integration via Bot API with secure keyring token storage. No MCP server required.

> **Requires a Telegram Bot.** Create one via [@BotFather](https://t.me/BotFather) on Telegram.

## First-Time Setup

1. Open Telegram and message [@BotFather](https://t.me/BotFather)
2. Send `/newbot` and follow the prompts to create your bot
3. Copy the bot token (looks like `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`)

Store the token:
```bash
python scripts/auth.py login <YOUR_BOT_TOKEN>
```

Check authentication status:
```bash
python scripts/auth.py status
```

Logout when needed:
```bash
python scripts/auth.py logout
```

## Commands

All operations via `scripts/telegram.py`. Requires authenticated bot token.

```bash
# Get bot info (verify setup)
python scripts/telegram.py get-me

# Send a text message
python scripts/telegram.py send-message <chat_id> "Hello from Claude!"

# Send with Markdown formatting
python scripts/telegram.py send-message <chat_id> "*bold* and _italic_" --parse-mode Markdown

# Send with HTML formatting
python scripts/telegram.py send-message <chat_id> "<b>bold</b> text" --parse-mode HTML

# Reply to a specific message
python scripts/telegram.py send-message <chat_id> "Replying!" --reply-to 42

# Send a file/document
python scripts/telegram.py send-file <chat_id> /path/to/document.pdf --caption "Here's the report"

# Send an image/photo
python scripts/telegram.py send-image <chat_id> /path/to/photo.jpg --caption "Check this out"

# Get recent updates/messages
python scripts/telegram.py get-updates --limit 25

# List recently active chats
python scripts/telegram.py list-chats

# Get info about a specific chat
python scripts/telegram.py get-chat <chat_id>

# Forward a message from one chat to another
python scripts/telegram.py forward-message <to_chat_id> <from_chat_id> <message_id>
```

## Chat ID Discovery

To find a chat ID:
1. Send a message to your bot on Telegram (or add it to a group)
2. Run `python scripts/telegram.py get-updates`
3. The chat ID will appear in the response

For channels, use `@channel_username` as the chat ID.

## Important Notes

- **Bot must be added to groups/channels** before it can interact with them
- **Privacy mode**: By default, bots in groups only see messages that mention them or reply to them. Disable privacy mode via @BotFather (`/setprivacy` -> Disable) to read all group messages
- **Updates are ephemeral**: `get-updates` only returns recent, unprocessed messages (up to 24 hours). It is not a full message history API
- **File size limits**: Uploads max 50MB, downloads max 20MB via Bot API
- **Rate limits**: Telegram limits bots to ~30 messages/second to different chats, 20 messages/minute to the same group

## Token Management

Bot token stored securely using the system keyring:
- **macOS**: Keychain
- **Windows**: Windows Credential Locker
- **Linux**: Secret Service API (GNOME Keyring, KDE Wallet, etc.)

Service name: `telegram-skill-bot`
