# Commit by Lee 🚀

**Generate commit messages otomatis dengan AI, 100% lokal & privasi terjaga**

Commit by Lee adalah tool open-source yang menggunakan **Qwen3:4B** melalui Ollama untuk menghasilkan pesan commit yang deskriptif dan mengikuti standar Conventional Commits.

## ✨ Fitur

- 🤖 **AI-Powered** - Menggunakan Qwen3:4B untuk generate commit message berkualitas
- 🌍 **Multilingual** - Support Bahasa Indonesia & English
- 🎨 **Multiple Styles** - Conventional Commits, Emoji, atau Simple
- ⚡ **Cepat** - Generate commit message dalam hitungan detik
- 🔒 **Privasi Terjaga** - Tidak ada kode yang dikirim ke cloud publik
- 🔌 **Ollama Integration** - Terhubung ke Ollama server (https://ollama.iotech.my.id)
- 🖥️ **Cross-Platform** - Windows, macOS, Linux

## 📦 Installation

### Prerequisites

- Python 3.11+
- Git
- Ollama server (atau gunakan https://ollama.iotech.my.id)

### Install from PyPI (coming soon)

```bash
pip install commit-by-lee
```

### Install from Source

```bash
# Clone repository
git clone https://github.com/lee/commit-by-lee.git
cd commit-by-lee/core

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

## 🚀 Usage

### Basic Usage

```bash
# Stage your changes
git add .

# Generate commit message
commit-by-lee generate

# Auto-commit without confirmation
commit-by-lee generate --yes

# Use English
commit-by-lee generate --lang en

# Use emoji style
commit-by-lee generate --style emoji
```

### Test Connection

```bash
# Test connection to Ollama server
commit-by-lee test-connection
```

### Configuration

```bash
# Show current configuration
commit-by-lee config
```

## ⚙️ Configuration

### Environment Variables (.env)

```bash
# Ollama Configuration
OLLAMA_HOST=https://ollama.iotech.my.id
OLLAMA_MODEL=qwen3:4b
OLLAMA_TIMEOUT=30
OLLAMA_TEMPERATURE=0.7

# App Configuration
COMMIT_BY_LEE_LANGUAGE=id  # id or en
COMMIT_BY_LEE_STYLE=conventional
COMMIT_BY_LEE_AUTO_COMMIT=false
```

### Config File (~/.commit-by-lee.yaml)

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
```

### Project Config (.commit-by-lee.yaml)

Override global config for specific project:

```yaml
ollama:
  model: qwen3:4b

app:
  language: en
```

## 🎨 Commit Message Styles

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

## 🌍 Multilingual Support

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

## 🛠️ Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/lee/commit-by-lee.git
cd commit-by-lee/core

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e .
```

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=commit_by_lee
```

### Code Style

```bash
# Format code
black commit_by_lee/

# Lint code
flake8 commit_by_lee/

# Type check
mypy commit_by_lee/
```

## 📚 Documentation

- [Installation Guide](docs/installation.md)
- [Usage Guide](docs/usage.md)
- [Configuration](docs/configuration.md)
- [Development Guide](docs/development.md)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Qwen3:4B** by Alibaba for the excellent multilingual LLM
- **Ollama** for the easy-to-use LLM runtime
- **Conventional Commits** for the commit message standard

## 📧 Contact

Lee - [@lee](https://github.com/lee)

## 🌟 Star History

If you find this project helpful, please consider giving it a star! ⭐

---

Made with ❤️ by Lee
