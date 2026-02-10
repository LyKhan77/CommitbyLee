# 🚀 Release Notes - v0.1.0

## Commit by Lee - VSCode Extension (First Release)

**Release Date**: 2026-02-10
**Version**: 0.1.0
**Status**: Initial Release

---

## ✨ What's New

Ini adalah **versi pertama** dari Commit by Lee VSCode Extension! Extension ini mengubah CLI tool menjadi full-featured VSCode extension yang memungkinkan kamu generate commit message secara otomatis menggunakan AI.

### Features

- 🤖 **AI-Powered Commit Generation**
  - Uses Ollama + Qwen3:4B model
  - Analyzes staged git changes
  - Generates descriptive commit messages

- 🖥️ **VSCode Integration**
  - Seamless Git integration via VSCode Git Extension API
  - Interactive webview panel for commit preview
  - Keyboard shortcut support (Ctrl+Shift+G)

- 🌍 **Multilingual**
  - Indonesian (Bahasa Indonesia)
  - English

- 🎨 **Multiple Commit Styles**
  - Conventional Commits (default)
  - Emoji style
  - Simple style

- ⚙️ **Configurable**
  - Ollama server URL
  - Model selection
  - Language preference
  - Commit style preference
  - Auto-commit option

- 🔧 **Developer Tools**
  - Test Ollama connection command
  - List available models
  - Configuration management

---

## 📦 Installation

### Method 1: Install from VSIX (Recommended)

1. Download `commit-by-lee-0.1.0.vsix` dari [GitHub Release](https://github.com/LyKhan77/CommitbyLee/releases/tag/v0.1.0)
2. Buka VSCode
3. Extensions (Ctrl+Shift+X)
4. Menu "..." → "Install from VSIX..."
5. Pilih file yang didownload

### Method 2: Manual Install

```bash
# Clone repository
git clone https://github.com/LyKhan77/CommitbyLee.git
cd CommitbyLee/vscode-extension

# Install dependencies
npm install

# Build extension
npm run compile

# Press F5 in VSCode to launch Extension Development Host
```

---

## ⚙️ Configuration

Setelah install, buka VSCode Settings (Ctrl+,) dan cari "commitbylee":

```json
{
  "commitbylee.ollamaHost": "http://localhost:11434",
  "commitbylee.ollamaModel": "qwen3:4b",
  "commitbylee.language": "id",
  "commitbylee.style": "conventional",
  "commitbylee.autoCommit": false,
  "commitbylee.temperature": 0.7
}
```

---

## 🚀 Usage

### Quick Start

1. **Make changes** to your code
2. **Stage changes**: `git add .` (or use VSCode Source Control)
3. **Generate commit**:
   - Press `Ctrl+Shift+G`
   - Or Command Palette: "Commit by Lee: Generate Commit Message"
4. **Preview** the generated commit message
5. **Choose action**:
   - ✓ Accept - Commit with the message
   - ✎ Edit - Modify before committing
   - ✗ Cancel - Abort

### Commands

| Command | Shortcut | Description |
|---------|----------|-------------|
| `commitbylee.generate` | `Ctrl+Shift+G` | Generate commit message |
| `commitbylee.testConnection` | - | Test Ollama connection |
| `commitbylee.openConfig` | - | Open configuration settings |

---

## 📖 Documentation

- [Installation Guide](https://github.com/LyKhan77/CommitbyLee/blob/main/vscode-extension/INSTALL.md)
- [Usage Guide](https://github.com/LyKhan77/CommitbyLee/blob/main/docs/usage.md)
- [Deployment Guide](https://github.com/LyKhan77/CommitbyLee/blob/main/docs/deployment-guide.md)
- [GitHub Release Guide](https://github.com/LyKhan77/CommitbyLee/blob/main/docs/github-release-guide.md)

---

## 🔧 System Requirements

- VSCode 1.85.0 or higher
- Git repository
- Internet connection (for Ollama server)
- Windows / macOS / Linux

---

## 🐛 Known Issues

None reported yet.

---

## 🙏 Credits

- **Ollama** - LLM runtime
- **Qwen3:4B** - Multilingual LLM by Alibaba
- **VSCode** - Extension API

---

## 📝 License

MIT License - See [LICENSE](https://github.com/LyKhan77/CommitbyLee/blob/main/vscode-extension/LICENSE)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📧 Contact

Lee - [GitHub](https://github.com/LyKhan77)

---

## 🔗 Links

- **GitHub Repository**: https://github.com/LyKhan77/CommitbyLee
- **Download VSIX**: https://github.com/LyKhan77/CommitbyLee/releases/download/v0.1.0/commit-by-lee-0.1.0.vsix
- **Issue Tracker**: https://github.com/LyKhan77/CommitbyLee/issues

---

**Made with ❤️ by Lee**

🎉 Thank you for using Commit by Lee!
