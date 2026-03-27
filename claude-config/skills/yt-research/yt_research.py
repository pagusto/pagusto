#!/usr/bin/env python3
"""YouTube Research Tool — scrapes metadata from YouTube search results using yt-dlp."""

import json
import subprocess
import sys


def search_youtube(query: str, max_results: int = 25) -> list[dict]:
    """Search YouTube and return video metadata."""
    search_url = f"ytsearch{max_results}:{query}"

    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--dump-json",
        "--flat-playlist",
        "--no-download",
        "--no-warnings",
        search_url,
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

    if result.returncode != 0:
        print(f"Error: {result.stderr}", file=sys.stderr)
        return []

    videos = []
    for line in result.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            data = json.loads(line)
            video = {
                "title": data.get("title", "N/A"),
                "url": data.get("url") or f"https://www.youtube.com/watch?v={data.get('id', '')}",
                "author": data.get("uploader") or data.get("channel", "N/A"),
                "views": data.get("view_count", "N/A"),
                "duration": data.get("duration_string") or _format_duration(data.get("duration")),
                "upload_date": data.get("upload_date", "N/A"),
                "description": (data.get("description") or "")[:200],
            }
            videos.append(video)
        except json.JSONDecodeError:
            continue

    return videos


def _format_duration(seconds):
    """Convert seconds to HH:MM:SS or MM:SS."""
    if not seconds:
        return "N/A"
    seconds = int(seconds)
    h, remainder = divmod(seconds, 3600)
    m, s = divmod(remainder, 60)
    if h > 0:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


def main():
    import argparse

    parser = argparse.ArgumentParser(description="YouTube Research Tool")
    parser.add_argument("query", help="Search query")
    parser.add_argument("-n", "--num-results", type=int, default=25, help="Number of results")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    videos = search_youtube(args.query, args.num_results)

    if args.json:
        print(json.dumps(videos, indent=2))
    else:
        for i, v in enumerate(videos, 1):
            print(f"\n{'='*60}")
            print(f"  #{i}: {v['title']}")
            print(f"  Author: {v['author']}")
            print(f"  Views: {v['views']:,}" if isinstance(v['views'], int) else f"  Views: {v['views']}")
            print(f"  Duration: {v['duration']}")
            print(f"  URL: {v['url']}")
            print(f"  Uploaded: {v['upload_date']}")
        print(f"\n{'='*60}")
        print(f"Total results: {len(videos)}")


if __name__ == "__main__":
    main()
