# Changelog

All notable changes to the "Commit by Lee" VSCode extension will be documented in this file.

## [0.1.0] - 2026-02-10

### Added
- Initial release of Commit by Lee VSCode extension
- AI-powered commit message generation using Ollama and Qwen3:4B
- Support for multiple commit message styles (conventional, emoji, simple)
- Multilingual support (Bahasa Indonesia and English)
- Interactive commit message preview panel
- Test Ollama connection command
- Configurable settings via VSCode settings
- Keyboard shortcut (Ctrl+Shift+G) for quick commit generation
- Auto-commit option
- Git integration using VSCode Git Extension API

### Features
- Generate commit messages from staged changes
- Preview commit message before committing
- Edit commit message before applying
- Test connection to Ollama server
- List available Ollama models
- Per-workspace configuration support

### Configuration
- `commitbylee.ollamaHost`: Ollama server URL
- `commitbylee.ollamaModel`: Model name
- `commitbylee.language`: Commit message language (id/en)
- `commitbylee.style`: Commit message style
- `commitbylee.autoCommit`: Auto-commit without confirmation
- `commitbylee.temperature`: LLM temperature

### Commands
- `commitbylee.generate`: Generate commit message (Ctrl+Shift+G)
- `commitbylee.testConnection`: Test Ollama connection
- `commitbylee.openConfig`: Open configuration settings
