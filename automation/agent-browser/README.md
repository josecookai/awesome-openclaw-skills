# Agent Browser 🌐

[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://openclaw.ai)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

> A fast Rust-based headless browser automation CLI with Node.js fallback that enables AI agents to navigate, click, type, and snapshot pages via structured commands.

## ✨ What is Agent Browser?

**Agent Browser** is a high-performance browser automation tool built in Rust (with Node.js fallback) that allows AI agents to interact with web pages programmatically. It provides a structured command interface for navigation, interaction, data extraction, and testing.

## 🚀 Features

| Feature | Description |
|---------|-------------|
| **🚀 Fast & Reliable** | Rust core for maximum performance |
| **🎯 Element References** | Stable `@e1`, `@e2` refs from snapshots |
| **📸 Screenshots & PDF** | Capture pages as images or PDFs |
| **🎥 Video Recording** | Record automation sessions |
| **📱 Device Emulation** | Simulate mobile/tablet devices |
| **🔐 State Management** | Save/load login sessions |
| **🌐 Network Control** | Intercept and mock API requests |
| **📊 JSON Output** | Machine-readable command results |

## 📦 Installation

```bash
# Via npm (recommended)
npm install -g agent-browser
agent-browser install

# Via ClawdHub
clawdhub install agent-browser
```

## 💡 Quick Start

```bash
# 1. Open a webpage
agent-browser open https://example.com

# 2. Get interactive elements
agent-browser snapshot -i
# Output: textbox "Email" [ref=e1], button "Submit" [ref=e2]

# 3. Interact with elements
agent-browser fill @e1 "user@example.com"
agent-browser click @e2

# 4. Wait for navigation
agent-browser wait --load networkidle

# 5. Capture result
agent-browser screenshot result.png
```

## 📋 Common Commands

### Navigation
```bash
agent-browser open <url>       # Navigate to URL
agent-browser back             # Go back
agent-browser reload           # Reload page
agent-browser close            # Close browser
```

### Page Analysis
```bash
agent-browser snapshot         # Full accessibility tree
agent-browser snapshot -i      # Interactive elements only
agent-browser snapshot -c      # Compact output
```

### Interactions
```bash
agent-browser click @e1              # Click element
agent-browser fill @e2 "text"        # Fill input
agent-browser type @e2 "text"        # Type without clearing
agent-browser press Enter            # Press key
agent-browser select @e1 "value"     # Select dropdown
agent-browser check @e1              # Check checkbox
```

### Information Extraction
```bash
agent-browser get text @e1      # Get element text
agent-browser get title         # Get page title
agent-browser get url           # Get current URL
agent-browser get html @e1      # Get innerHTML
```

### Screenshots & PDFs
```bash
agent-browser screenshot              # Screenshot to stdout
agent-browser screenshot page.png     # Save to file
agent-browser screenshot --full       # Full page screenshot
agent-browser pdf output.pdf          # Save as PDF
```

### Session Management
```bash
agent-browser state save auth.json    # Save session
agent-browser state load auth.json    # Load session
```

## 🎯 Use Cases

### 1. Web Scraping
```bash
agent-browser open https://news.ycombinator.com
agent-browser snapshot -i
agent-browser get text @e1 --json
```

### 2. Form Automation
```bash
agent-browser open https://example.com/login
agent-browser snapshot -i
agent-browser fill @e1 "username"
agent-browser fill @e2 "password"
agent-browser click @e3
agent-browser wait --url "/dashboard"
agent-browser state save login.json
```

### 3. UI Testing
```bash
agent-browser open https://myapp.com
agent-browser snapshot -i
agent-browser click @e1
agent-browser wait --text "Success"
agent-browser is visible @e2
```

### 4. Data Extraction
```bash
agent-browser open https://example.com/data
agent-browser get count ".item"
agent-browser get text ".item:first" --json
```

## 🔧 Advanced Features

### Network Interception
```bash
agent-browser network route https://api.example.com --body '{"mock": true}'
agent-browser network route https://tracker.com --abort
```

### Device Emulation
```bash
agent-browser set device "iPhone 14"
agent-browser set viewport 1920 1080
agent-browser set geo 37.7749 -122.4194
```

### Video Recording
```bash
agent-browser record start demo.webm
agent-browser click @e1
agent-browser fill @e2 "text"
agent-browser record stop
```

### Multi-Session
```bash
agent-browser --session user1 open site-a.com
agent-browser --session user2 open site-b.com
agent-browser session list
```

## 📊 JSON Output

Add `--json` for machine-readable output:
```bash
agent-browser snapshot -i --json
agent-browser get text @e1 --json
```

## 🐛 Debugging

```bash
agent-browser open example.com --headed    # Show browser window
agent-browser console                       # View console messages
agent-browser errors                        # View page errors
agent-browser highlight @e1                # Highlight element
```

## ⚠️ Requirements

- Node.js 18+
- npm or pnpm
- For Rust core: See [agent-browser](https://github.com/vercel-labs/agent-browser) repo

## 🔗 Resources

- **Skill Repository**: https://github.com/TheSethRose/Agent-Browser-CLI
- **CLI Repository**: https://github.com/vercel-labs/agent-browser
- **Documentation**: See SKILL.md for full command reference

## 🤝 Contributing

Contributions welcome! See CONTRIBUTING.md for guidelines.

## 📝 License

MIT License

## 🙏 Credits

Created by the OpenClaw community and Vercel Labs.

---

*Automate the web, one command at a time.* 🌐
