# Telegram Bot Configuration

## Bot
- **Username**: @pagusto_bot
- **Name**: Paulsito
- **Bot ID**: 8742421423

## Default Chat
- **Chat ID**: 6883969392 (Paul's personal chat)

## Auth
- Token stored in system keyring (service: `telegram-skill-bot`, account: `main-account`)
- Token obtained from @BotFather
- To re-authenticate: `python scripts/auth.py login <TOKEN>`

## Usage
```bash
# Send message to Paul
python scripts/telegram.py send-message 6883969392 "message here"

# Send file to Paul
python scripts/telegram.py send-file 6883969392 /path/to/file

# Send image to Paul
python scripts/telegram.py send-image 6883969392 /path/to/image.jpg
```
