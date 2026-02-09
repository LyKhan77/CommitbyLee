# Usage Guide - Commit by Lee

Learn how to use Commit by Lee to generate commit messages automatically.

## Basic Workflow

### 1. Make Changes to Your Code

```bash
# Edit your files
# For example:
echo "print('Hello, World!')" > hello.py
```

### 2. Stage Your Changes

```bash
# Stage all changes
git add .

# Or stage specific files
git add hello.py
```

### 3. Generate Commit Message

```bash
# Generate and preview commit message
commit-by-lee generate
```

This will:
- Analyze your staged changes
- Send to Qwen3:4B model
- Generate a commit message
- Show preview for confirmation
- Execute git commit if you accept

### 4. Review and Confirm

After running the command, you'll see:

```
🤖 Commit by Lee

🔌 Checking Ollama connection...
✓ Connected to Ollama

📝 Analyzing staged changes...
  Files changed: 1
  Insertions: +1
  Deletions: -0

🧠 Generating commit message with Qwen3:4B...

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃         📄 Preview                      ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━ Commit by Lee ━━━┫
┃                                         ┃
┃ feat: tambahkan file hello world        ┃
┃                                         ┃
┃ Membuat file hello.py untuk demo        ┃
┃                                         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

✨ Accept this commit message? [y/N]:
```

Type `y` to accept and commit, or `n` to cancel.

## Command Reference

### `commit-by-lee generate`

Generate commit message from staged changes.

**Options:**

- `--yes, -y`: Auto-commit without confirmation
- `--lang`: Set language (`id` or `en`)
- `--style`: Set commit style (`conventional`, `emoji`, or `simple`)

**Examples:**

```bash
# Basic usage
commit-by-lee generate

# Auto-commit without confirmation
commit-by-lee generate --yes

# Generate in English
commit-by-lee generate --lang en

# Use emoji style
commit-by-lee generate --style emoji
```

### `commit-by-lee test-connection`

Test connection to Ollama server.

**Example:**

```bash
commit-by-lee test-connection
```

Output:
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

### `commit-by-lee config`

Show current configuration.

**Example:**

```bash
commit-by-lee config
```

Output:
```
⚙️  Commit by Lee Configuration

Ollama Settings:
  Host: https://ollama.iotech.my.id
  Model: qwen3:4b
  Timeout: 30s
  Temperature: 0.7

App Settings:
  Language: id
  Style: conventional
  Auto-commit: false

Config File:
  C:\Users\Lee\.commit-by-lee.yaml
```

## Language Options

### Bahasa Indonesia (Default)

```bash
commit-by-lee generate --lang id
```

Output:
```
feat(auth): tambahkan autentikasi pengguna

Implement OAuth2 login flow dengan Google provider
```

### English

```bash
commit-by-lee generate --lang en
```

Output:
```
feat(auth): add user authentication

Implement OAuth2 login flow with Google provider
```

## Commit Message Styles

### Conventional Commits (Default)

```bash
commit-by-lee generate --style conventional
```

Format:
```
type(scope): subject

body
```

Example:
```
feat(api): tambahkan endpoint user registration

Membuat endpoint POST /api/users/register untuk
registrasi pengguna baru dengan validasi email
```

### Emoji Style

```bash
commit-by-lee generate --style emoji
```

Format:
```
🎉 type: subject

body
```

Example:
```
✨ feat: tambahkan endpoint user registration

Membuat endpoint POST /api/users/register untuk
registrasi pengguna baru dengan validasi email
```

### Simple Style

```bash
commit-by-lee generate --style simple
```

Format:
```
subject only
```

Example:
```
Tambahkan endpoint user registration dengan validasi email
```

## Advanced Usage

### Auto-Commit Mode

Skip confirmation dialog:

```bash
commit-by-lee generate --yes
```

Useful for:
- CI/CD pipelines
- Automated workflows
- Quick commits

### Batch Processing

Generate multiple commits at once:

```bash
# Stage first batch
git add file1.py file2.py
commit-by-lee generate --yes

# Stage second batch
git add file3.py file4.py
commit-by-lee generate --yes
```

### Custom Configuration Per Project

Create `.commit-by-lee.yaml` in project root:

```yaml
ollama:
  model: qwen3:4b

app:
  language: en  # Override global setting
  style: emoji
```

## Tips and Best Practices

### 1. Stage Related Changes Together

```bash
# Good: Related changes in one commit
git add auth.py auth_test.py
commit-by-lee generate

# Better: Separate unrelated changes
git add auth.py
commit-by-lee generate
git add auth_test.py
commit-by-lee generate
```

### 2. Write Clear Code Comments

Qwen3:4B uses your code comments to understand changes:

```python
# Good: Clear comments
def login(user):
    # Authenticate user with OAuth2
    pass

# Bad: No context
def login(x):
    pass
```

### 3. Review Before Committing

Always review the generated message:

```bash
commit-by-lee generate
# Don't use --yes for important commits
```

### 4. Use Appropriate Language

```bash
# Indonesian team
commit-by-lee generate --lang id

# International team
commit-by-lee generate --lang en
```

## Common Scenarios

### Bug Fix

```bash
# Fix the bug
vim fix_bug.py

# Stage the fix
git add fix_bug.py

# Generate commit
commit-by-lee generate
```

Typical output:
```
fix(auth): perbaiki validasi password

- Tambah minimum length check
- Perbaiki error message
```

### New Feature

```bash
# Add new feature
vim new_feature.py

# Stage the feature
git add new_feature.py

# Generate commit
commit-by-lee generate
```

Typical output:
```
feat(ui): tambahkan dark mode support

Implement toggle untuk dark mode dengan
persistent storage di localStorage
```

### Refactoring

```bash
# Refactor code
vim old_code.py

# Stage changes
git add old_code.py

# Generate commit
commit-by-lee generate
```

Typical output:
```
refactor(api): optimasi query database

- Reduce query count dari 5 ke 2
- Improve response time
```

## Troubleshooting

### No Staged Changes

**Problem:** `⚠ No staged changes found`

**Solution:**
```bash
# Stage your changes first
git add .
# or
git add <specific-files>
```

### Connection Failed

**Problem:** `✗ Failed to connect to Ollama server`

**Solution:**
```bash
# Test connection
commit-by-lee test-connection

# Check your internet connection
# Verify Ollama server is accessible
```

### Poor Quality Messages

**Problem:** Generated message doesn't make sense

**Solutions:**
1. Add more context in code comments
2. Stage related changes together
3. Try regenerating: commit-by-lee generate
4. Manually edit the message if needed

## Integration with Git Hooks (Coming Soon)

Automate commit message generation:

```bash
# Setup git hook (future feature)
commit-by-lee setup-hook
```

This will automatically trigger when you run `git commit`.

## Video Tutorial

Coming soon! 🎥

---

Need more help? Check the [Configuration Guide](configuration.md) or [open an issue](https://github.com/lee/commit-by-lee/issues).
