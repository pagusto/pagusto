---
name: playwright
description: "Browser automation and web testing using Playwright. Write and execute custom Playwright scripts for page testing, form filling, screenshots, responsive design validation, link checking, and any browser-based automation. Visible browser by default. Triggers on: playwright, browser test, web test, screenshot, form test, responsive test, browser automation, end-to-end test, e2e test, check website, test page."
argument-hint: "<browser automation task or URL>"
license: MIT
---

# playwright -- Browser Automation Skill

General-purpose browser automation using Playwright. Claude writes custom Playwright code for any automation task, executes it via the universal executor, and returns results with screenshots and console output.

## Usage

The skill is located in `skills/playwright-skill/`. All automation runs through the universal executor `run.js`.

### Prerequisites

Install dependencies (one-time):

```bash
cd /home/user/pagusto/claude-config/skills/playwright/skills/playwright-skill && npm run setup
```

### Running Automation

Write a temporary Playwright script and execute it via `run.js`:

```bash
node /home/user/pagusto/claude-config/skills/playwright/skills/playwright-skill/run.js /tmp/my-test.js
```

### Detailed Skill Instructions

For the complete workflow (server detection, script patterns, helpers):

```bash
cat /home/user/pagusto/claude-config/skills/playwright/skills/playwright-skill/SKILL.md
```

### Workflow

1. User describes what they want to test or automate
2. Write custom Playwright code to a temp file in `/tmp/`
3. Execute via `run.js` which handles module resolution
4. Browser opens visibly and automation runs
5. Return results with console output and screenshots

### Example Script

```javascript
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: false, slowMo: 100 });
  const page = await browser.newPage();
  await page.goto('https://example.com');
  await page.screenshot({ path: '/tmp/screenshot.png' });
  console.log('Title:', await page.title());
  await browser.close();
})();
```

### Helpers

Optional utility functions are available in `skills/playwright-skill/lib/helpers.js` for common tasks like dev server detection.

### API Reference

For advanced Playwright APIs (selectors, network interception, authentication, mobile emulation):

```bash
cat /home/user/pagusto/claude-config/skills/playwright/skills/playwright-skill/API_REFERENCE.md
```

## Configuration

- **Headless:** `false` (browser visible by default)
- **Slow Motion:** `100ms` for visibility
- **Timeout:** `30s`
- **Screenshots:** Saved to `/tmp/`

## Important

- Always execute scripts through `run.js` to ensure proper module resolution
- Save test scripts to `/tmp/` to avoid polluting project directories
- For localhost testing, detect running dev servers first using the helpers
