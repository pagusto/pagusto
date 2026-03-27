#!/bin/bash
set -euo pipefail

# =============================================================================
# Claude Config Sync — Push ~/.claude/ config to GitHub repo pagusto/pagusto
# Syncs: skills, agents, commands, hooks, plugins, get-shit-done, memory
# =============================================================================

REPO_DIR="${CLAUDE_PROJECT_DIR:-/home/user/pagusto}"
CONFIG_DIR="$REPO_DIR/claude-config"
CLAUDE_DIR="$HOME/.claude"
MANIFEST="$CONFIG_DIR/.sync-manifest.json"

echo "[sync] Starting config sync to GitHub..."

# Create config directory
mkdir -p "$CONFIG_DIR"

# ---- SYNC EACH COMPONENT ----

# 1. Agents
echo "[sync] Syncing agents..."
rm -rf "$CONFIG_DIR/agents"
cp -r "$CLAUDE_DIR/agents" "$CONFIG_DIR/agents" 2>/dev/null || true

# 2. Skills (exclude marketplace caches and node_modules)
echo "[sync] Syncing skills..."
rm -rf "$CONFIG_DIR/skills"
mkdir -p "$CONFIG_DIR/skills"
if [ -d "$CLAUDE_DIR/skills" ]; then
    for skill_dir in "$CLAUDE_DIR/skills"/*/; do
        skill_name=$(basename "$skill_dir")
        # Skip marketplace caches
        if [[ "$skill_name" == "n8n-"* ]] || [[ "$skill_name" == "skill-seekers"* ]]; then
            continue
        fi
        mkdir -p "$CONFIG_DIR/skills/$skill_name"
        rsync -a --exclude='node_modules' --exclude='.git' --exclude='__pycache__' \
            "$skill_dir" "$CONFIG_DIR/skills/$skill_name/" 2>/dev/null || \
            cp -r "$skill_dir" "$CONFIG_DIR/skills/$skill_name/" 2>/dev/null || true
    done
fi

# 3. Commands
echo "[sync] Syncing commands..."
rm -rf "$CONFIG_DIR/commands"
cp -r "$CLAUDE_DIR/commands" "$CONFIG_DIR/commands" 2>/dev/null || true

# 4. Hooks
echo "[sync] Syncing hooks..."
rm -rf "$CONFIG_DIR/hooks"
mkdir -p "$CONFIG_DIR/hooks"
for f in "$CLAUDE_DIR/hooks"/*; do
    [ -f "$f" ] && cp "$f" "$CONFIG_DIR/hooks/" 2>/dev/null || true
done

# 5. Plugins (config only, no caches)
echo "[sync] Syncing plugins..."
rm -rf "$CONFIG_DIR/plugins"
mkdir -p "$CONFIG_DIR/plugins"
for f in blocklist.json installed_plugins.json known_marketplaces.json; do
    [ -f "$CLAUDE_DIR/plugins/$f" ] && cp "$CLAUDE_DIR/plugins/$f" "$CONFIG_DIR/plugins/"
done

# 6. Get-Shit-Done framework
echo "[sync] Syncing GSD framework..."
rm -rf "$CONFIG_DIR/get-shit-done"
cp -r "$CLAUDE_DIR/get-shit-done" "$CONFIG_DIR/get-shit-done" 2>/dev/null || true

# 7. GSD manifest
[ -f "$CLAUDE_DIR/gsd-file-manifest.json" ] && \
    cp "$CLAUDE_DIR/gsd-file-manifest.json" "$CONFIG_DIR/"

# 8. Settings (global — sanitize secrets)
echo "[sync] Syncing settings..."
if [ -f "$CLAUDE_DIR/settings.json" ]; then
    # Copy settings but strip any API keys
    sed 's/"apiKey":\s*"[^"]*"/"apiKey": "REDACTED"/g' \
        "$CLAUDE_DIR/settings.json" > "$CONFIG_DIR/settings.json"
fi

# 9. Memory files
echo "[sync] Syncing memory..."
rm -rf "$CONFIG_DIR/memory"
# Find memory directories in projects
for mem_dir in "$CLAUDE_DIR"/projects/*/memory/; do
    if [ -d "$mem_dir" ]; then
        mkdir -p "$CONFIG_DIR/memory"
        cp "$mem_dir"/*.md "$CONFIG_DIR/memory/" 2>/dev/null || true
    fi
done
# Also check for MEMORY.md at project level
for mem_file in "$CLAUDE_DIR"/projects/*/MEMORY.md; do
    if [ -f "$mem_file" ]; then
        mkdir -p "$CONFIG_DIR/memory"
        cp "$mem_file" "$CONFIG_DIR/memory/" 2>/dev/null || true
    fi
done

# ---- BUILD MANIFEST ----
echo "[sync] Building sync manifest..."
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
AGENT_COUNT=$(find "$CONFIG_DIR/agents" -name "*.md" 2>/dev/null | wc -l)
SKILL_COUNT=$(find "$CONFIG_DIR/skills" -maxdepth 1 -type d 2>/dev/null | tail -n+2 | wc -l)
COMMAND_COUNT=$(find "$CONFIG_DIR/commands" -name "*.md" 2>/dev/null | wc -l)
HOOK_COUNT=$(find "$CONFIG_DIR/hooks" -type f 2>/dev/null | wc -l)
MEMORY_COUNT=$(find "$CONFIG_DIR/memory" -name "*.md" 2>/dev/null | wc -l)

cat > "$MANIFEST" << MANIFEST_EOF
{
  "version": "1.0.0",
  "lastSync": "$TIMESTAMP",
  "counts": {
    "agents": $AGENT_COUNT,
    "skills": $SKILL_COUNT,
    "commands": $COMMAND_COUNT,
    "hooks": $HOOK_COUNT,
    "memory": $MEMORY_COUNT
  },
  "source": "$(hostname)",
  "user": "$(whoami)"
}
MANIFEST_EOF

# ---- GIT PUSH ----
echo "[sync] Pushing to GitHub..."
cd "$REPO_DIR"
git add claude-config/
git commit -m "sync: update claude config $(date +%Y-%m-%d_%H:%M)" 2>/dev/null || {
    echo "[sync] No changes to commit"
    exit 0
}

# Push with retry (exponential backoff)
for attempt in 1 2 3 4; do
    if git push -u origin HEAD 2>/dev/null; then
        echo "[sync] Push successful!"
        break
    fi
    wait_time=$((2 ** attempt))
    echo "[sync] Push failed, retrying in ${wait_time}s..."
    sleep $wait_time
done

echo "[sync] Config sync complete!"
echo "[sync] Agents: $AGENT_COUNT | Skills: $SKILL_COUNT | Commands: $COMMAND_COUNT | Hooks: $HOOK_COUNT | Memory: $MEMORY_COUNT"
