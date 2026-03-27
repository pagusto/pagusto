---
name: ffuf-web-fuzzing
description: "Web fuzzing and security reconnaissance using ffuf (Fuzz Faster U Fool). Discover hidden directories, files, subdomains, and API endpoints. Supports authenticated fuzzing with raw requests, auto-calibration, and result analysis. Triggers on: ffuf, fuzz, web fuzzing, directory enumeration, subdomain discovery, brute force, penetration testing, security testing, hidden paths, endpoint discovery."
argument-hint: "<target URL or domain>"
license: MIT
---

# ffuf-web-fuzzing -- Web Fuzzing with ffuf

Expert guidance and helper scripts for web fuzzing using ffuf during penetration testing and security reconnaissance.

## Usage

When the user asks to fuzz a web target, use ffuf with the helper script and resources in `ffuf-skill/`.

### Prerequisites

ffuf must be installed:

```bash
# macOS
brew install ffuf

# Linux (Go required)
go install github.com/ffuf/ffuf/v2@latest
```

### Detailed Skill Instructions

For complete ffuf usage patterns, read the full skill file:

```bash
cat /home/user/pagusto/claude-config/skills/ffuf-web-fuzzing/ffuf-skill/SKILL.md
```

### Core Concepts

The `FUZZ` keyword is a placeholder replaced with wordlist entries:

```bash
# Directory enumeration
ffuf -u https://target.com/FUZZ -w /path/to/wordlist.txt

# Subdomain discovery
ffuf -u https://FUZZ.target.com -w /path/to/subdomains.txt

# POST parameter fuzzing
ffuf -u https://target.com/login -X POST -d "username=admin&password=FUZZ" -w /path/to/passwords.txt
```

### Helper Script

The `ffuf-skill/ffuf_helper.py` script provides additional automation:

```bash
python3 /home/user/pagusto/claude-config/skills/ffuf-web-fuzzing/ffuf-skill/ffuf_helper.py
```

### Common Wordlists

Check `ffuf-skill/resources/` for bundled wordlists, or use standard locations:
- `/usr/share/wordlists/` (Kali Linux)
- `/usr/share/seclists/` (SecLists)

## Important

- **Only test systems you own or have explicit written permission to test**
- Unauthorized testing is illegal -- always confirm authorization before running
- Use rate limiting (`-rate`) to avoid causing service disruption
- Review results carefully and follow responsible disclosure practices
