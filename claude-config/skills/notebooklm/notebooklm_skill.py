#!/usr/bin/env python3
"""NotebookLM Skill — Create notebooks, add sources, generate artifacts via notebooklm-py."""

import asyncio
import json
import sys
import argparse


async def create_notebook(name: str) -> dict:
    """Create a new NotebookLM notebook."""
    from notebooklm import NotebookLMClient

    async with await NotebookLMClient.from_storage() as client:
        nb = await client.notebooks.create(name)
        return {"notebook_id": nb.id, "name": name, "status": "created"}


async def add_youtube_sources(notebook_id: str, urls: list[str]) -> dict:
    """Add YouTube URLs as sources to a notebook."""
    from notebooklm import NotebookLMClient

    async with await NotebookLMClient.from_storage() as client:
        added = []
        failed = []
        for url in urls:
            try:
                await client.sources.add_url(notebook_id, url, wait=True)
                added.append(url)
            except Exception as e:
                failed.append({"url": url, "error": str(e)})

        return {
            "notebook_id": notebook_id,
            "added": len(added),
            "failed": len(failed),
            "failures": failed,
        }


async def generate_artifact(notebook_id: str, artifact_type: str, instructions: str = "") -> dict:
    """Generate an artifact (infographic, audio, quiz, etc.) from a notebook."""
    from notebooklm import NotebookLMClient

    async with await NotebookLMClient.from_storage() as client:
        artifacts = client.artifacts

        generators = {
            "audio": lambda: artifacts.generate_audio(notebook_id, instructions=instructions or "make it engaging"),
            "infographic": lambda: artifacts.generate_infographic(notebook_id),
            "quiz": lambda: artifacts.generate_quiz(notebook_id),
            "flashcards": lambda: artifacts.generate_flashcards(notebook_id),
            "slide-deck": lambda: artifacts.generate_slide_deck(notebook_id),
            "mind-map": lambda: artifacts.generate_mind_map(notebook_id),
        }

        if artifact_type not in generators:
            return {"error": f"Unknown artifact type: {artifact_type}. Supported: {list(generators.keys())}"}

        status = await generators[artifact_type]()
        await artifacts.wait_for_completion(notebook_id, status.task_id)
        return {"notebook_id": notebook_id, "artifact_type": artifact_type, "status": "completed", "task_id": status.task_id}


async def download_artifact(notebook_id: str, artifact_type: str, output_path: str) -> dict:
    """Download a generated artifact."""
    from notebooklm import NotebookLMClient

    async with await NotebookLMClient.from_storage() as client:
        downloaders = {
            "audio": lambda: client.artifacts.download_audio(notebook_id, output_path),
            "infographic": lambda: client.artifacts.download_infographic(notebook_id, output_path),
            "quiz": lambda: client.artifacts.download_quiz(notebook_id, output_path, output_format="markdown"),
            "flashcards": lambda: client.artifacts.download_flashcards(notebook_id, output_path, output_format="json"),
            "slide-deck": lambda: client.artifacts.download_slide_deck(notebook_id, output_path),
            "mind-map": lambda: client.artifacts.download_mind_map(notebook_id, output_path),
        }

        if artifact_type not in downloaders:
            return {"error": f"Unknown artifact type: {artifact_type}"}

        await downloaders[artifact_type]()
        return {"artifact_type": artifact_type, "output_path": output_path, "status": "downloaded"}


async def chat_with_notebook(notebook_id: str, question: str) -> dict:
    """Ask a question against the notebook sources."""
    from notebooklm import NotebookLMClient

    async with await NotebookLMClient.from_storage() as client:
        result = await client.chat.ask(notebook_id, question)
        return {"question": question, "answer": result.answer}


def main():
    parser = argparse.ArgumentParser(description="NotebookLM Skill")
    subparsers = parser.add_subparsers(dest="command")

    # Create notebook
    create_parser = subparsers.add_parser("create", help="Create a notebook")
    create_parser.add_argument("name", help="Notebook name")

    # Add sources
    add_parser = subparsers.add_parser("add-sources", help="Add YouTube URLs")
    add_parser.add_argument("notebook_id", help="Notebook ID")
    add_parser.add_argument("urls", nargs="+", help="YouTube URLs to add")

    # Generate artifact
    gen_parser = subparsers.add_parser("generate", help="Generate an artifact")
    gen_parser.add_argument("notebook_id", help="Notebook ID")
    gen_parser.add_argument("type", choices=["audio", "infographic", "quiz", "flashcards", "slide-deck", "mind-map"])
    gen_parser.add_argument("--instructions", default="", help="Custom instructions")

    # Download artifact
    dl_parser = subparsers.add_parser("download", help="Download an artifact")
    dl_parser.add_argument("notebook_id", help="Notebook ID")
    dl_parser.add_argument("type", choices=["audio", "infographic", "quiz", "flashcards", "slide-deck", "mind-map"])
    dl_parser.add_argument("output", help="Output file path")

    # Chat
    chat_parser = subparsers.add_parser("chat", help="Ask a question")
    chat_parser.add_argument("notebook_id", help="Notebook ID")
    chat_parser.add_argument("question", help="Question to ask")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "create":
        result = asyncio.run(create_notebook(args.name))
    elif args.command == "add-sources":
        result = asyncio.run(add_youtube_sources(args.notebook_id, args.urls))
    elif args.command == "generate":
        result = asyncio.run(generate_artifact(args.notebook_id, args.type, args.instructions))
    elif args.command == "download":
        result = asyncio.run(download_artifact(args.notebook_id, args.type, args.output))
    elif args.command == "chat":
        result = asyncio.run(chat_with_notebook(args.notebook_id, args.question))

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
