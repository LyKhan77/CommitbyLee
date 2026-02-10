# Commit by Lee - VSCode Extension

Generate commit messages automatically with AI using Ollama and Qwen3:4B model.

## Features

- 🤖 **AI-Powered** - Uses Qwen3:4B to generate commit messages
- 🌍 **Multilingual** - Support Bahasa Indonesia & English
- 🎨 **Multiple Styles** - Conventional Commits, Emoji, or Simple
- ⚡ **Fast** - Generate commit messages in seconds
- 🔒 **Privacy** - No code sent to public cloud
- 🖥️ **Integrated** - Works seamlessly within VSCode

## Installation

### From Marketplace (Coming Soon)

Search for "Commit by Lee" in VSCode Extensions marketplace.

### From Source

1. Clone this repository
2. Install dependencies: `npm install`
3. Build the extension: `npm run compile`
4. Install in VSCode: Press F5 to open Extension Development Host

## Usage

### Basic Workflow

1. Make changes to your code
2. Stage changes: `git add .` (or use VSCode Source Control)
3. Press `Ctrl+Shift+G` or run `Commit by Lee: Generate Commit Message` from Command Palette
4. Preview the generated commit message
5. Click **Accept** to commit, **Edit** to modify, or **Cancel** to abort

### Commands

- `Commit by Lee: Generate Commit Message` (Ctrl+Shift+G) - Generate commit message from staged changes
- `Commit by Lee: Test Ollama Connection` - Test connection to Ollama server
- `Commit by Lee: Open Configuration` - Open extension settings

## Configuration

Configure the extension in VSCode Settings:

### Settings

- `commitbylee.ollamaHost` - Ollama server URL (default: `http://localhost:11434`)
- `commitbylee.ollamaModel` - Model name (default: `qwen3:4b`)
- `commitbylee.language` - Commit message language: `id` (Indonesian) or `en` (English)
- `commitbylee.style` - Commit message style: `conventional`, `emoji`, or `simple`
- `commitbylee.autoCommit` - Automatically commit without confirmation (default: `false`)
- `commitbylee.temperature` - LLM temperature 0-1 (default: `0.7`)

### Example Configuration

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

## Commit Message Styles

### Conventional Commits (Default)

```
feat(auth): tambahkan autentikasi pengguna

Implement OAuth2 login flow dengan Google provider
```

### Emoji Style

```
✨ feat: tambahkan autentikasi pengguna

Implement OAuth2 login flow dengan Google provider
```

### Simple Style

```
Tambahkan fitur autentikasi pengguna dengan OAuth2
```

## Requirements

- VSCode 1.85.0 or higher
- Git repository
- Ollama server (or use `https://ollama.iotech.my.id`)

## Development

### Setup

```bash
# Install dependencies
npm install

# Compile TypeScript
npm run compile

# Watch for changes
npm run watch

# Run tests
npm test
```

### Build

```bash
# Install vsce (VSCode Extension Manager)
npm install -g @vscode/vsce

# Package extension
vsce package
```

## Troubleshooting

### No Git Repository

Make sure you have a git repository open in VSCode.

### No Staged Changes

Stage your changes first:
```bash
git add .
```

### Connection Failed

1. Test connection: Run `Commit by Lee: Test Ollama Connection`
2. Check Ollama server URL in settings
3. Verify Ollama server is accessible

## License

MIT License - see LICENSE file for details

## Author

Lee

## Support

For issues and questions, please visit: https://github.com/lee/commit-by-lee
