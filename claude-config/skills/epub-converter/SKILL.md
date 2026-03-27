---
name: epub-converter
description: "Convert markdown documents and chat summaries into professional EPUB3 ebook files. Works with raw markdown text or markdown files. Output works on Apple Books, Kindle, Kobo, Google Play Books, and any EPUB reader. Triggers on: epub, ebook, convert markdown, markdown to epub, create ebook, kindle, export book, publish document."
argument-hint: "<markdown content or file path> [--title TITLE] [--author AUTHOR]"
license: MIT
---

# epub-converter -- Markdown to EPUB Converter

Converts markdown documents into professional EPUB3 ebook files that work across all major reading platforms.

## Usage

When the user asks to convert markdown to an EPUB, use the Python scripts in the `markdown-to-epub/` subdirectory.

### Prerequisites

Install dependencies first (one-time):

```bash
pip install -r /home/user/pagusto/claude-config/skills/epub-converter/markdown-to-epub/requirements.txt
```

### Converting Markdown to EPUB

```python
import sys
sys.path.insert(0, "/home/user/pagusto/claude-config/skills/epub-converter")
from markdown_to_epub.scripts.epub_generator import create_epub_from_markdown

create_epub_from_markdown(
    markdown_content,
    output_path="output.epub",
    title="My Book",
    author="Author Name"
)
```

### Parameters

- `markdown_content` (required): Raw markdown string to convert
- `output_path` (required): Where to save the .epub file
- `title` (optional): Book title (extracted from frontmatter or first H1 if not provided)
- `author` (optional): Author name

### Supported Markdown Features

- Headers (H1-H6) with automatic chapter detection from H1
- Bold, italic, links, lists, blockquotes
- Code blocks with monospace fonts and syntax highlighting
- Tables with styled headers and alternating row colors
- YAML frontmatter for metadata (title, author, language, date)

## Workflow

1. User provides markdown content (inline or as a file path)
2. Read the markdown content
3. Call `create_epub_from_markdown()` with the content and output path
4. Confirm the EPUB was created and provide the file path

## Important

- If the user provides a file path, read the file contents first, then pass them to the converter
- Default to the user's home directory or current directory for output if no path is specified
- YAML frontmatter in the markdown (title, author, language, date) will be used as metadata automatically
