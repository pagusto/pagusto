#!/usr/bin/env python3
"""
Bot token management for Telegram Bot API.
Cross-platform secure storage using keyring library.
"""

import json
import sys
import time
from typing import Optional

import os

import httpx

KEYRING_AVAILABLE = False
keyring = None
# Keyring can cause Rust-level panics in cloud environments (pyo3_runtime.PanicException)
# which cannot be caught by Python try/except. Test in a subprocess first.
import subprocess as _sp
try:
    _result = _sp.run(
        [sys.executable, "-c", "import keyring; keyring.get_password('__test__','__test__')"],
        capture_output=True, timeout=5
    )
    if _result.returncode == 0:
        import keyring as _kr
        keyring = _kr
        KEYRING_AVAILABLE = True
except Exception:
    pass

# Telegram Bot API
BOT_API_BASE = "https://api.telegram.org/bot"

# Keyring configuration
KEYCHAIN_SERVICE = "telegram-skill-bot"
KEYCHAIN_ACCOUNT = "main-account"

# File-based fallback for environments without keyring
TOKEN_FILE = os.path.expanduser("~/.claude/skills/telegram/token.json")


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


def _read_token_file() -> Optional[dict]:
    """Read token data from file-based storage."""
    try:
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE) as f:
                return json.load(f)
    except (json.JSONDecodeError, OSError):
        pass
    return None


def _write_token_file(data: dict) -> bool:
    """Write token data to file-based storage."""
    try:
        os.makedirs(os.path.dirname(TOKEN_FILE), exist_ok=True)
        with open(TOKEN_FILE, "w") as f:
            json.dump(data, f)
        os.chmod(TOKEN_FILE, 0o600)
        return True
    except OSError as e:
        print(f"Error writing token file: {e}", file=sys.stderr)
        return False


def get_bot_token() -> Optional[str]:
    """Retrieve bot token. Checks: env var -> file -> keyring."""
    # 1. Environment variable (highest priority)
    env_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if env_token:
        return env_token

    # 2. File-based storage
    data = _read_token_file()
    if data and data.get("bot_token"):
        return data["bot_token"]

    # 3. Keyring (if available)
    if KEYRING_AVAILABLE:
        try:
            data_str = keyring.get_password(KEYCHAIN_SERVICE, KEYCHAIN_ACCOUNT)
            if data_str:
                kd = json.loads(data_str)
                return kd.get("bot_token")
        except Exception:
            pass

    return None


def save_bot_token(token: str, bot_info: dict) -> bool:
    """Save bot token to file storage (and keyring if available)."""
    data = {
        "bot_token": token,
        "bot_info": bot_info,
        "updatedAt": int(time.time() * 1000),
    }
    saved = _write_token_file(data)
    if KEYRING_AVAILABLE:
        try:
            keyring.set_password(KEYCHAIN_SERVICE, KEYCHAIN_ACCOUNT, json.dumps(data))
        except Exception:
            pass
    return saved


def clear_bot_token() -> bool:
    """Clear bot token from all storage."""
    cleared = False
    try:
        if os.path.exists(TOKEN_FILE):
            os.remove(TOKEN_FILE)
            cleared = True
    except OSError:
        pass
    if KEYRING_AVAILABLE:
        try:
            keyring.delete_password(KEYCHAIN_SERVICE, KEYCHAIN_ACCOUNT)
            cleared = True
        except Exception:
            pass
    return cleared


def get_bot_info() -> Optional[dict]:
    """Retrieve stored bot info (username, id, etc.)."""
    data = _read_token_file()
    if data and data.get("bot_info"):
        return data["bot_info"]
    if KEYRING_AVAILABLE:
        try:
            data_str = keyring.get_password(KEYCHAIN_SERVICE, KEYCHAIN_ACCOUNT)
            if data_str:
                kd = json.loads(data_str)
                return kd.get("bot_info")
        except Exception:
            pass
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
