#!/usr/bin/env python3
"""
Bot token management for Telegram Bot API.
Cross-platform secure storage using keyring library.
"""

import json
import sys
import time
from typing import Optional

import httpx
import keyring

# Telegram Bot API
BOT_API_BASE = "https://api.telegram.org/bot"

# Keyring configuration
KEYCHAIN_SERVICE = "telegram-skill-bot"
KEYCHAIN_ACCOUNT = "main-account"


def validate_token(token: str) -> Optional[dict]:
    """Validate a bot token by calling getMe. Returns bot info if valid."""
    try:
        resp = httpx.get(f"{BOT_API_BASE}{token}/getMe", timeout=15)
        data = resp.json()
        if data.get("ok"):
            return data["result"]
        return None
    except (httpx.HTTPError, json.JSONDecodeError):
        return None


def get_bot_token() -> Optional[str]:
    """Retrieve bot token from secure storage."""
    try:
        data_str = keyring.get_password(KEYCHAIN_SERVICE, KEYCHAIN_ACCOUNT)
        if not data_str:
            return None
        data = json.loads(data_str)
        return data.get("bot_token")
    except (json.JSONDecodeError, keyring.errors.KeyringError) as e:
        print(f"Error reading token: {e}", file=sys.stderr)
        return None


def save_bot_token(token: str, bot_info: dict) -> bool:
    """Save bot token to secure storage."""
    data = {
        "bot_token": token,
        "bot_info": bot_info,
        "updatedAt": int(time.time() * 1000),
    }
    try:
        keyring.set_password(KEYCHAIN_SERVICE, KEYCHAIN_ACCOUNT, json.dumps(data))
        return True
    except keyring.errors.KeyringError as e:
        print(f"Error saving token: {e}", file=sys.stderr)
        return False


def clear_bot_token() -> bool:
    """Clear bot token from secure storage."""
    try:
        keyring.delete_password(KEYCHAIN_SERVICE, KEYCHAIN_ACCOUNT)
        return True
    except keyring.errors.PasswordDeleteError:
        return False
    except keyring.errors.KeyringError as e:
        print(f"Error clearing token: {e}", file=sys.stderr)
        return False


def get_bot_info() -> Optional[dict]:
    """Retrieve stored bot info (username, id, etc.)."""
    try:
        data_str = keyring.get_password(KEYCHAIN_SERVICE, KEYCHAIN_ACCOUNT)
        if not data_str:
            return None
        data = json.loads(data_str)
        return data.get("bot_info")
    except (json.JSONDecodeError, keyring.errors.KeyringError):
        return None


def get_valid_bot_token(interactive: bool = True) -> Optional[str]:
    """
    Get a valid bot token.

    Args:
        interactive: If True, will print helpful messages when no token exists.
                    If False, will silently return None.
    """
    token = get_bot_token()

    if not token:
        if interactive:
            print(
                "No bot token found. Run: python scripts/auth.py login <TOKEN>",
                file=sys.stderr,
            )
        return None

    return token


def main():
    """CLI for auth operations."""
    import argparse

    parser = argparse.ArgumentParser(description="Telegram Bot token management")
    subparsers = parser.add_subparsers(dest="command")

    login_parser = subparsers.add_parser("login", help="Store and validate bot token")
    login_parser.add_argument("token", help="Bot token from @BotFather")

    subparsers.add_parser("logout", help="Clear stored token")
    subparsers.add_parser("token", help="Print current bot token")
    subparsers.add_parser("status", help="Check authentication status")

    args = parser.parse_args()

    if args.command == "login":
        print("Validating token...", file=sys.stderr)
        bot_info = validate_token(args.token)
        if bot_info:
            save_bot_token(args.token, bot_info)
            username = bot_info.get("username", "unknown")
            print(f"Login successful! Bot: @{username}")
        else:
            print("Invalid token. Check your token from @BotFather.", file=sys.stderr)
            sys.exit(1)

    elif args.command == "logout":
        if clear_bot_token():
            print("Logged out successfully.")
        else:
            print("No token to clear.")

    elif args.command == "token":
        token = get_bot_token()
        if token:
            print(token)
        else:
            print(
                "Not authenticated. Run: python scripts/auth.py login <TOKEN>",
                file=sys.stderr,
            )
            sys.exit(1)

    elif args.command == "status":
        token = get_bot_token()
        bot_info = get_bot_info()
        if token and bot_info:
            username = bot_info.get("username", "unknown")
            bot_id = bot_info.get("id", "unknown")
            print(f"Status: Authenticated")
            print(f"Bot: @{username} (ID: {bot_id})")
        elif token:
            print(f"Status: Authenticated (bot info not cached)")
        else:
            print("Status: Not authenticated")
            print("Run: python scripts/auth.py login <TOKEN>")
            sys.exit(1)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
