# Installation Guide - Commit by Lee

Complete guide to install and setup Commit by Lee on your system.

## Requirements

- Python 3.11 or higher
- Git
- Internet connection (for Ollama server access)

## Installation Methods

### Method 1: Install from PyPI (Recommended when published)

```bash
pip install commit-by-lee
```

### Method 2: Install from Source

#### Step 1: Clone Repository

```bash
git clone https://github.com/lee/commit-by-lee.git
cd commit-by-lee/core
```

#### Step 2: Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

#### Step 4: Install in Development Mode

```bash
pip install -e .
```

## Verify Installation

After installation, verify that Commit by Lee is working:

```bash
commit-by-lee --version
```

Expected output:
```
Commit by Lee v0.1.0
```

## Test Ollama Connection

Test connection to the Ollama server:

```bash
commit-by-lee test-connection
```

Expected output:
```
============================================================
Testing Ollama Connection
============================================================

Host: https://ollama.iotech.my.id
Model: qwen3:4b

Testing connection...
[OK] Connection successful!

Found 27 model(s):
  • qwen3:4b (2499.4 MB)
  • mistral:latest (3922.8 MB)
  ...
```

## Configuration

### Option 1: Environment Variables (Quick Start)

Create a `.env` file in your project directory:

```bash
# Ollama Configuration
OLLAMA_HOST=https://ollama.iotech.my.id
OLLAMA_MODEL=qwen3:4b
OLLAMA_TIMEOUT=30
OLLAMA_TEMPERATURE=0.7

# App Configuration
COMMIT_BY_LEE_LANGUAGE=id
COMMIT_BY_LEE_STYLE=conventional
```

### Option 2: Global Config File

Create a config file at `~/.commit-by-lee.yaml`:

```yaml
ollama:
  host: https://ollama.iotech.my.id
  model: qwen3:4b
  timeout: 30
  temperature: 0.7

app:
  language: id  # id or en
  style: conventional
  auto_commit: false

git:
  scope_mappings:
    src/auth/: auth
    src/ui/: ui
    src/api/: api
    src/utils/: utils
  commit_types:
    - feat
    - fix
    - docs
    - refactor
    - test
    - chore
```

### Option 3: Project-Specific Config

Create `.commit-by-lee.yaml` in your project root:

```yaml
ollama:
  model: qwen3:4b

app:
  language: en
  style: emoji
```

## Troubleshooting

### Python Not Found

**Problem:** `python: command not found`

**Solution:**
- Make sure Python 3.11+ is installed
- On Windows, add Python to PATH
- Use `python3` instead of `python` on macOS/Linux

### Connection Failed

**Problem:** `Connection failed` when running `commit-by-lee test-connection`

**Solutions:**
1. Check internet connection
2. Verify Ollama server is accessible: `curl https://ollama.iotech.my.id/api/tags`
3. Check if firewall blocks the connection
4. Try a different network

### Git Not Found

**Problem:** `Git not found. Please ensure git is installed.`

**Solution:**
- Install Git from https://git-scm.com/
- Add Git to system PATH

### Import Errors

**Problem:** `ModuleNotFoundError: No module named 'commit_by_lee'`

**Solution:**
- Make sure you're in the correct directory
- Reinstall: `pip install -e .`
- Check virtual environment is activated

## Uninstallation

To uninstall Commit by Lee:

```bash
pip uninstall commit-by-lee
```

To remove config files:

```bash
# Global config
rm ~/.commit-by-lee.yaml

# Project config (in each project)
rm .commit-by-lee.yaml
```

## Next Steps

After successful installation:

1. Read the [Usage Guide](usage.md) to learn how to use Commit by Lee
2. Check the [Configuration Guide](configuration.md) for advanced settings
3. Start generating commit messages!

## Getting Help

If you encounter any issues:

1. Check the [Troubleshooting](#troubleshooting) section above
2. Search existing issues on GitHub
3. Create a new issue with details about your problem
4. Contact: lee@example.com

---

Happy committing! 🚀
