---
name: ios-simulator
description: "iOS Simulator automation for app testing, building, and UI interaction. 21 production scripts for semantic UI navigation, build automation, accessibility testing, and simulator lifecycle management. Uses accessibility APIs instead of pixel coordinates. Triggers on: iOS simulator, Xcode, iPhone simulator, iOS testing, xcrun simctl, app testing, accessibility audit, iOS build, simulator boot, screen mapping."
argument-hint: "<ios automation task>"
license: MIT
---

# ios-simulator -- iOS Simulator Automation Skill

Build, test, and automate iOS applications using 21 production-ready scripts with accessibility-driven navigation and structured output.

## Usage

All scripts are located in `ios-simulator-skill/scripts/`. Run the health check first:

```bash
bash /home/user/pagusto/claude-config/skills/ios-simulator/ios-simulator-skill/scripts/sim_health_check.sh
```

### Quick Start

```bash
SKILL_DIR="/home/user/pagusto/claude-config/skills/ios-simulator/ios-simulator-skill"

# Launch app
python "$SKILL_DIR/scripts/app_launcher.py" --launch com.example.app

# Map screen to see elements
python "$SKILL_DIR/scripts/screen_mapper.py"

# Tap button by text
python "$SKILL_DIR/scripts/navigator.py" --find-text "Login" --tap

# Enter text in field
python "$SKILL_DIR/scripts/navigator.py" --find-type TextField --enter-text "user@test.com"

# Accessibility audit
python "$SKILL_DIR/scripts/accessibility_audit.py"
```

### Script Categories

| Category | Scripts | Purpose |
|----------|---------|---------|
| Build & Dev | build_and_test.py, log_monitor.py | Build projects, run tests, monitor logs |
| Navigation | screen_mapper.py, navigator.py, gesture.py, keyboard.py, app_launcher.py | UI interaction via accessibility APIs |
| Testing | accessibility_audit.py, visual_diff.py, test_recorder.py, app_state_capture.py, sim_health_check.sh | WCAG compliance, visual diffs, snapshots |
| Permissions | clipboard.py, status_bar.py, push_notification.py, privacy_manager.py | Device state and permission management |
| Lifecycle | simctl_boot.py, simctl_shutdown.py, simctl_create.py, simctl_delete.py, simctl_erase.py | Simulator device management |

### Detailed Reference

For complete script documentation and all options:

```bash
cat /home/user/pagusto/claude-config/skills/ios-simulator/ios-simulator-skill/SKILL.md
```

All scripts support `--help` for detailed options and `--json` for machine-readable output.

## Important

- Requires macOS 12+ with Xcode Command Line Tools
- Uses semantic navigation (find by text/type/ID) instead of pixel coordinates
- Default output is 3-5 lines (use `--verbose` for details, `--json` for parsing)
- Auto-detects booted simulator UDID -- no need to specify `--udid` each time
