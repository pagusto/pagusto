#!/usr/bin/env python3
"""
Telegram Bot API operations.
Lightweight integration for sending/reading messages, files, and images.
"""

import argparse
import json
import mimetypes
import os
import sys
from typing import Optional

import httpx

from auth import get_valid_bot_token

BOT_API_BASE = "https://api.telegram.org/bot"


def api_request(
    method: str,
    params: Optional[dict] = None,
    files: Optional[dict] = None,
) -> dict:
    """Make a request to the Telegram Bot API.

    Args:
        method: Bot API method name (e.g. 'sendMessage', 'getMe')
        params: Query/form parameters
        files: Files to upload as multipart form data
    """
    token = get_valid_bot_token()
    if not token:
        return {"error": "Failed to get bot token"}

    url = f"{BOT_API_BASE}{token}/{method}"

    try:
        if files:
            # Multipart upload for files
            form_data = {}
            if params:
                form_data = {k: str(v) for k, v in params.items() if v is not None}

            file_uploads = {}
            for key, file_path in files.items():
                if not os.path.isfile(file_path):
                    return {"error": f"File not found: {file_path}"}
                mime_type, _ = mimetypes.guess_type(file_path)
                if not mime_type:
                    mime_type = "application/octet-stream"
                filename = os.path.basename(file_path)
                file_uploads[key] = (filename, open(file_path, "rb"), mime_type)

            try:
                resp = httpx.post(
                    url, data=form_data, files=file_uploads, timeout=60
                )
            finally:
                for f in file_uploads.values():
                    f[1].close()
        else:
            # Regular JSON request
            resp = httpx.post(url, json=params or {}, timeout=30)

        data = resp.json()
        if data.get("ok"):
            return data.get("result", data)
        return {"error": data.get("description", "Unknown error")}

    except httpx.HTTPError as e:
        return {"error": f"Request failed: {e}"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response"}


def get_me() -> dict:
    """Get bot information."""
    return api_request("getMe")


def send_message(
    chat_id: str,
    text: str,
    parse_mode: Optional[str] = None,
    reply_to: Optional[int] = None,
) -> dict:
    """Send a text message to a chat."""
    params = {"chat_id": chat_id, "text": text}
    if parse_mode:
        params["parse_mode"] = parse_mode
    if reply_to:
        params["reply_to_message_id"] = reply_to
    return api_request("sendMessage", params)


def send_file(
    chat_id: str, file_path: str, caption: Optional[str] = None
) -> dict:
    """Send a document/file to a chat."""
    params = {"chat_id": chat_id}
    if caption:
        params["caption"] = caption
    return api_request("sendDocument", params, files={"document": file_path})


def send_image(
    chat_id: str, file_path: str, caption: Optional[str] = None
) -> dict:
    """Send a photo to a chat."""
    params = {"chat_id": chat_id}
    if caption:
        params["caption"] = caption
    return api_request("sendPhoto", params, files={"photo": file_path})


def get_updates(limit: int = 25, offset: Optional[int] = None) -> dict:
    """Get recent updates (messages, etc.)."""
    params = {"limit": limit, "allowed_updates": ["message"]}
    if offset is not None:
        params["offset"] = offset
    return api_request("getUpdates", params)


def list_chats(limit: int = 100) -> list:
    """List recently active chats by parsing getUpdates."""
    result = get_updates(limit=limit)
    if isinstance(result, dict) and "error" in result:
        return result

    if not isinstance(result, list):
        return {"error": "Unexpected response format"}

    seen = {}
    for update in result:
        msg = update.get("message", {})
        chat = msg.get("chat")
        if chat:
            chat_id = chat.get("id")
            if chat_id and chat_id not in seen:
                seen[chat_id] = {
                    "id": chat_id,
                    "type": chat.get("type"),
                    "title": chat.get("title"),
                    "username": chat.get("username"),
                    "first_name": chat.get("first_name"),
                    "last_name": chat.get("last_name"),
                }

    return list(seen.values())


def get_chat(chat_id: str) -> dict:
    """Get information about a chat."""
    return api_request("getChat", {"chat_id": chat_id})


def forward_message(
    chat_id: str, from_chat_id: str, message_id: int
) -> dict:
    """Forward a message from one chat to another."""
    return api_request(
        "forwardMessage",
        {
            "chat_id": chat_id,
            "from_chat_id": from_chat_id,
            "message_id": message_id,
        },
    )


def main():
    parser = argparse.ArgumentParser(description="Telegram Bot API operations")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # get-me
    subparsers.add_parser("get-me", help="Get bot information")

    # send-message
    send_msg = subparsers.add_parser("send-message", help="Send a text message")
    send_msg.add_argument("chat_id", help="Chat ID or @username")
    send_msg.add_argument("text", help="Message text")
    send_msg.add_argument(
        "--parse-mode", choices=["Markdown", "HTML"], help="Text formatting mode"
    )
    send_msg.add_argument(
        "--reply-to", type=int, help="Message ID to reply to"
    )

    # send-file
    send_f = subparsers.add_parser("send-file", help="Send a document/file")
    send_f.add_argument("chat_id", help="Chat ID or @username")
    send_f.add_argument("file_path", help="Path to file")
    send_f.add_argument("--caption", help="File caption")

    # send-image
    send_img = subparsers.add_parser("send-image", help="Send a photo")
    send_img.add_argument("chat_id", help="Chat ID or @username")
    send_img.add_argument("file_path", help="Path to image")
    send_img.add_argument("--caption", help="Photo caption")

    # get-updates
    get_upd = subparsers.add_parser("get-updates", help="Get recent updates")
    get_upd.add_argument(
        "--limit", type=int, default=25, help="Max updates to return"
    )
    get_upd.add_argument("--offset", type=int, help="Update offset")

    # list-chats
    list_c = subparsers.add_parser(
        "list-chats", help="List recently active chats"
    )
    list_c.add_argument(
        "--limit", type=int, default=100, help="Max updates to scan"
    )

    # get-chat
    get_c = subparsers.add_parser("get-chat", help="Get chat info")
    get_c.add_argument("chat_id", help="Chat ID or @username")

    # forward-message
    fwd = subparsers.add_parser("forward-message", help="Forward a message")
    fwd.add_argument("chat_id", help="Destination chat ID")
    fwd.add_argument("from_chat_id", help="Source chat ID")
    fwd.add_argument("message_id", type=int, help="Message ID to forward")

    args = parser.parse_args()

    if args.command == "get-me":
        result = get_me()
    elif args.command == "send-message":
        result = send_message(
            args.chat_id, args.text, args.parse_mode, args.reply_to
        )
    elif args.command == "send-file":
        result = send_file(args.chat_id, args.file_path, args.caption)
    elif args.command == "send-image":
        result = send_image(args.chat_id, args.file_path, args.caption)
    elif args.command == "get-updates":
        result = get_updates(args.limit, args.offset)
    elif args.command == "list-chats":
        result = list_chats(args.limit)
    elif args.command == "get-chat":
        result = get_chat(args.chat_id)
    elif args.command == "forward-message":
        result = forward_message(
            args.chat_id, args.from_chat_id, args.message_id
        )
    else:
        result = {"error": f"Unknown command: {args.command}"}

    print(json.dumps(result, indent=2, ensure_ascii=False))

    if isinstance(result, dict) and "error" in result:
        sys.exit(1)


if __name__ == "__main__":
    main()
