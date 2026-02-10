# Installation Guide - Commit by Lee VSCode Extension

## Prerequisites

Before installing the extension, ensure you have:

1. **VSCode** version 1.85.0 or higher
2. **Git** installed and initialized in your project
3. **Node.js** and npm (for development)

## Installation Methods

### Method 1: Install from VSIX Package (Recommended)

1. Build the extension package (.vsix):
   ```bash
   cd vscode-extension
   npm install -g @vscode/vsce
   vsce package
   ```

2. Install the extension:
   - Open VSCode
   - Go to Extensions (Ctrl+Shift+X)
   - Click "..." (three dots) menu
   - Select "Install from VSIX..."
   - Choose the generated `commit-by-lee-0.1.0.vsix` file

### Method 2: Install in Development Mode

1. Open the extension folder in VSCode:
   ```bash
   code vscode-extension
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Press `F5` to launch a new VSCode window with the extension loaded

### Method 3: Publish to Marketplace (Future)

Once published, you can install directly from the VSCode Marketplace by searching for "Commit by Lee".

## Post-Installation Setup

### 1. Configure Ollama Connection

Open VSCode Settings (Ctrl+,) and search for "commitbylee":

```json
{
  "commitbylee.ollamaHost": "https://ollama.iotech.my.id",
  "commitbylee.ollamaModel": "qwen3:4b",
  "commitbylee.language": "id",
  "commitbylee.style": "conventional"
}
```

### 2. Test Connection

1. Open Command Palette (Ctrl+Shift+P)
2. Run: `Commit by Lee: Test Ollama Connection`
3. Check the output channel for results

### 3. Generate Your First Commit Message

1. Make some changes to your code
2. Stage the changes: `git add .` (or use VSCode Source Control)
3. Press `Ctrl+Shift+G` or run `Commit by Lee: Generate Commit Message`
4. Preview the generated commit message
5. Click **Accept** to commit, **Edit** to modify, or **Cancel** to abort

## Troubleshooting

### Extension Not Activating

- Check VSCode version (must be 1.85.0+)
- Check Output panel > "Commit by Lee" channel for errors

### Connection Failed

- Verify Ollama server URL in settings
- Test connection manually:
  ```bash
  curl https://ollama.iotech.my.id/api/tags
  ```

### No Git Repository

- Ensure you have a `.git` folder in your project
- Initialize if needed: `git init`

### Build Errors

- Clear node_modules and reinstall:
  ```bash
  rm -rf node_modules package-lock.json
  npm install
  npm run compile
  ```

## Uninstallation

To remove the extension:

1. Go to Extensions (Ctrl+Shift+X)
2. Search for "Commit by Lee"
3. Click the gear icon
4. Select "Uninstall"

## Next Steps

- Read the [User Guide](../docs/usage.md)
- Configure keyboard shortcuts
- Set up auto-commit if desired
