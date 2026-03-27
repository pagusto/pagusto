#!/bin/bash
set -euo pipefail

# =============================================================================
# SessionStart Hook — Auto-restore Claude config from GitHub on session start
# =============================================================================

# Output async mode for non-blocking startup
echo '{"async": true, "asyncTimeout": 300000}'

# Only run in remote/cloud environment
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
    exit 0
fi

REPO_DIR="${CLAUDE_PROJECT_DIR:-/home/user/pagusto}"

# Run the restore script
if [ -f "$REPO_DIR/.claude/hooks/restore-config.sh" ]; then
    bash "$REPO_DIR/.claude/hooks/restore-config.sh"
fi
