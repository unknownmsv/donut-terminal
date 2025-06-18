# 🍩 Donut Terminal - Installer (Beta)

Welcome to **Donut Terminal**, a modern terminal experience designed for mobile and lightweight systems.  
This installer sets up the **Donut CLI**, **AI integration** (via `ollama` and your own AI proxy), and provides several smart shortcuts via `donut.lang`.

---

## 🚀 Features

- Custom AI assistant powered by `ollama` or your proxy server.
- Built-in language mapping (`donut.lang`) for easy command aliases.
- Works smoothly on Termux, Ubuntu, and minimal systems.
- Lightweight Vim-based text editing (`donutTTE`).
- Sudo toggle mode with `o$` prefix.
- Full offline support when used with local models.

---

## 📦 What This Installer Does

- Installs system dependencies (Python, pip, git, curl)
- Clones the latest `donut-terminal` source code
- Installs and configures `ollama`
- Pulls your preferred model (like `qwen` or `llama3`)
- Starts your AI proxy (optional)

---

## 🛠 Requirements

- Linux-based environment (Ubuntu, Termux, Debian, etc.)
- Python 3.6+
- Internet connection (for initial setup)

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/donut-terminal.git
cd donut-terminal
chmod +x ai-setup.sh
./ai-setup.sh
```
# donut-terminal
