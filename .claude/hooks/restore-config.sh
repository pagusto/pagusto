#!/bin/bash
set -euo pipefail

# =============================================================================
# Claude Config Restore — Pull from GitHub and install to ~/.claude/
# Runs on SessionStart to ensure config is up to date
# =============================================================================

REPO_DIR="${CLAUDE_PROJECT_DIR:-/home/user/pagusto}"
CONFIG_DIR="$REPO_DIR/claude-config"
CLAUDE_DIR="$HOME/.claude"
MANIFEST="$CONFIG_DIR/.sync-manifest.json"
LOCAL_MANIFEST="$CLAUDE_DIR/.sync-manifest-local.json"

echo "[restore] Checking for config updates..."

# Pull latest from GitHub
cd "$REPO_DIR"
git fetch origin 2>/dev/null || true
git pull origin HEAD 2>/dev/null || true

# Check if claude-config exists in repo
if [ ! -d "$CONFIG_DIR" ]; then
    echo "[restore] No claude-config/ found in repo. Skipping."
    exit 0
fi

# Compare manifests to detect changes
NEEDS_UPDATE=false
if [ ! -f "$LOCAL_MANIFEST" ]; then
    NEEDS_UPDATE=true
elif [ -f "$MANIFEST" ]; then
    REMOTE_SYNC=$(grep -o '"lastSync":\s*"[^"]*"' "$MANIFEST" 2>/dev/null | head -1 || echo "")
    LOCAL_SYNC=$(grep -o '"lastSync":\s*"[^"]*"' "$LOCAL_MANIFEST" 2>/dev/null | head -1 || echo "")
    if [ "$REMOTE_SYNC" != "$LOCAL_SYNC" ]; then
        NEEDS_UPDATE=true
    fi
fi

if [ "$NEEDS_UPDATE" = false ]; then
    echo "[restore] Config is up to date. No changes needed."
    exit 0
fi

echo "[restore] Updates detected. Restoring config..."

# ---- RESTORE EACH COMPONENT ----

# 1. Agents
if [ -d "$CONFIG_DIR/agents" ]; then
    echo "[restore] Restoring agents..."
    mkdir -p "$CLAUDE_DIR/agents"
    cp -r "$CONFIG_DIR/agents"/* "$CLAUDE_DIR/agents/" 2>/dev/null || true
fi

# 2. Skills
if [ -d "$CONFIG_DIR/skills" ]; then
    echo "[restore] Restoring skills..."
    mkdir -p "$CLAUDE_DIR/skills"
    for skill_dir in "$CONFIG_DIR/skills"/*/; do
        skill_name=$(basename "$skill_dir")
        mkdir -p "$CLAUDE_DIR/skills/$skill_name"
        cp -r "$skill_dir"* "$CLAUDE_DIR/skills/$skill_name/" 2>/dev/null || true
    done
fi

# 3. Commands
if [ -d "$CONFIG_DIR/commands" ]; then
    echo "[restore] Restoring commands..."
    mkdir -p "$CLAUDE_DIR/commands"
    cp -r "$CONFIG_DIR/commands"/* "$CLAUDE_DIR/commands/" 2>/dev/null || true
fi

# 4. Hooks
if [ -d "$CONFIG_DIR/hooks" ]; then
    echo "[restore] Restoring hooks..."
    mkdir -p "$CLAUDE_DIR/hooks"
    cp "$CONFIG_DIR/hooks"/* "$CLAUDE_DIR/hooks/" 2>/dev/null || true
    chmod +x "$CLAUDE_DIR/hooks"/*.sh 2>/dev/null || true
    chmod +x "$CLAUDE_DIR/hooks"/*.js 2>/dev/null || true
fi

# 5. Plugins
if [ -d "$CONFIG_DIR/plugins" ]; then
    echo "[restore] Restoring plugins..."
    mkdir -p "$CLAUDE_DIR/plugins"
    cp "$CONFIG_DIR/plugins"/*.json "$CLAUDE_DIR/plugins/" 2>/dev/null || true
fi

# 6. Get-Shit-Done
if [ -d "$CONFIG_DIR/get-shit-done" ]; then
    echo "[restore] Restoring GSD framework..."
    mkdir -p "$CLAUDE_DIR/get-shit-done"
    cp -r "$CONFIG_DIR/get-shit-done"/* "$CLAUDE_DIR/get-shit-done/" 2>/dev/null || true
    chmod +x "$CLAUDE_DIR/get-shit-done/bin"/* 2>/dev/null || true
fi

# 7. GSD manifest
[ -f "$CONFIG_DIR/gsd-file-manifest.json" ] && \
    cp "$CONFIG_DIR/gsd-file-manifest.json" "$CLAUDE_DIR/"

# 8. Memory
if [ -d "$CONFIG_DIR/memory" ]; then
    echo "[restore] Restoring memory..."
    # Find or create project memory directory
    PROJECT_DIR=""
    for d in "$CLAUDE_DIR"/projects/*/; do
        if [ -d "$d" ]; then
            PROJECT_DIR="$d"
            break
        fi
    done
    if [ -z "$PROJECT_DIR" ]; then
        # Create based on repo path
        ENCODED_PATH=$(echo "$REPO_DIR" | sed 's|/|-|g; s|^-||')
        PROJECT_DIR="$CLAUDE_DIR/projects/$ENCODED_PATH"
        mkdir -p "$PROJECT_DIR"
    fi
    mkdir -p "$PROJECT_DIR/memory"
    cp "$CONFIG_DIR/memory"/*.md "$PROJECT_DIR/memory/" 2>/dev/null || true
    # Also copy MEMORY.md to project root if it exists
    [ -f "$CONFIG_DIR/memory/MEMORY.md" ] && cp "$CONFIG_DIR/memory/MEMORY.md" "$PROJECT_DIR/"
fi

# ---- UPDATE LOCAL MANIFEST ----
if [ -f "$MANIFEST" ]; then
    cp "$MANIFEST" "$LOCAL_MANIFEST"
fi

# Count what was restored
AGENT_COUNT=$(find "$CLAUDE_DIR/agents" -name "*.md" 2>/dev/null | wc -l)
SKILL_COUNT=$(find "$CLAUDE_DIR/skills" -maxdepth 1 -type d 2>/dev/null | tail -n+2 | wc -l)
COMMAND_COUNT=$(find "$CLAUDE_DIR/commands" -name "*.md" 2>/dev/null | wc -l)
HOOK_COUNT=$(find "$CLAUDE_DIR/hooks" -type f 2>/dev/null | wc -l)

echo "[restore] Config restored!"
echo "[restore] Agents: $AGENT_COUNT | Skills: $SKILL_COUNT | Commands: $COMMAND_COUNT | Hooks: $HOOK_COUNT"
