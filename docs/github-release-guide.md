# Cara Membuat GitHub Release dengan File VSIX

## Status: ✅ Code sudah ter-push ke GitHub!

Repository: https://github.com/LyKhan77/CommitbyLee
Branch: main
Latest commit: 88cbefa

## 📦 Membuat GitHub Release (Manual)

### Option 1: Melalui GitHub Website (Paling Mudah)

1. **Buka repository di GitHub**:
   ```
   https://github.com/LyKhan77/CommitbyLee
   ```

2. **Klik "Releases"** di sidebar kanan

3. **Klik "Create a new release"** atau "Draft a new release"

4. **Isi detail release**:
   - **Tag version**: `v0.1.0` (klik "Add new tag")
   - **Target**: `main`
   - **Title**: `🚀 Commit by Lee v0.1.0 - VSCode Extension`
   - **Description**:
     ```markdown
     # 🎉 First VSCode Extension Release!

     ## ✨ Features

     - AI-powered commit message generation using Ollama + Qwen3:4B
     - Interactive webview panel for commit preview
     - Git integration via VSCode Git Extension API
     - Multilingual support (Indonesian & English)
     - Multiple commit styles (Conventional, Emoji, Simple)
     - Test Ollama connection command
     - Configurable settings via VSCode settings
     - Keyboard shortcut (Ctrl+Shift+G)

     ## 📦 Installation

     1. Download `commit-by-lee-0.1.0.vsix` dari release ini
     2. Buka VSCode
     3. Extensions (Ctrl+Shift+X)
     4. Menu "..." → "Install from VSIX..."
     5. Pilih file yang didownload

     ## ⚙️ Configuration

     Setelah install, buka Settings (Ctrl+,) dan cari "commitbylee":

     ```json
     {
       "commitbylee.ollamaHost": "https://ollama.iotech.my.id",
       "commitbylee.ollamaModel": "qwen3:4b",
       "commitbylee.language": "id",
       "commitbylee.style": "conventional"
     }
     ```

     ## 🚀 Usage

     1. Stage changes: `git add .`
     2. Press `Ctrl+Shift+G`
     3. Preview dan accept commit message!

     ## 📖 Documentation

     - [Installation Guide](https://github.com/LyKhan77/CommitbyLee/blob/main/vscode-extension/INSTALL.md)
     - [Usage Guide](https://github.com/LyKhan77/CommitbyLee/blob/main/docs/usage.md)
     - [Deployment Guide](https://github.com/LyKhan77/CommitbyLee/blob/main/docs/deployment-guide.md)

     ## 🙏 Credits

     Built with ❤️ using Ollama and Qwen3:4B

     ---
     **Full Changelog**: https://github.com/LyKhan77/CommitbyLee/compare/v0.0.1...v0.1.0
     ```

5. **Attach binary file**:
   - Klik "Attach binary" atau "Choose files"
   - Pilih file: `vscode-extension/commit-by-lee-0.1.0.vsix`
   - Tunggu upload selesai

6. **Pilih visibility**:
   - ✅ "Set as a pre-release" (untuk testing)
   - Atau biarkan unchecked untuk release stabil

7. **Klik "Publish release"**

### Option 2: Menggunakan GitHub CLI (Jika terinstall)

Jika kamu punya GH CLI:

```bash
# Install GH CLI dulu (jika belum)
# Download dari: https://cli.github.com/

# Login ke GitHub
gh auth login

# Buat release
cd D:\Occupation\Lee\Lee-AI\commit-by-lee
gh release create v0.1.0 vscode-extension/commit-by-lee-0.1.0.vsix \
  --title "🚀 Commit by Lee v0.1.0 - VSCode Extension" \
  --notes "AI-powered commit message generator untuk VSCode"
```

## 🔗 Link Release Setelah Dibuat

Setelah release dipublish, user bisa download dari:
```
https://github.com/LyKhan77/CommitbyLee/releases/download/v0.1.0/commit-by-lee-0.1.0.vsix
```

## 📋 Checklist Setelah Release

- [ ] Release published di GitHub
- [ ] File VSIX terupload dan bisa didownload
- [ ] Test download dan install dari link release
- [ ] Share link ke team/user
- [ ] Update README dengan link download

## 🎯 Next Steps

Setelah release pertama:

1. **Beritau team**:
   - Share link release
   - Kirim file INSTALL_INSTRUCTIONS.txt
   - Demo cara install dan pakai

2. **Collect feedback**:
   - Minta user test dan report bugs
   - Buat issues di GitHub untuk feature requests

3. **Release berikutnya**:
   - Fix bugs → v0.1.1
   - Add features → v0.2.0
   - Major changes → v1.0.0

## 📊 Versioning

Gunakan Semantic Versioning:
- **MAJOR.MINOR.PATCH**
- v0.1.0 (initial release)
- v0.1.1 (bug fixes)
- v0.2.0 (new features)
- v1.0.0 (stable, production-ready)

---

## 💡 Tips

1. **Jadwal Release**:
   - Initial: v0.1.0 (sekarang)
   - Bug fixes: v0.1.1, v0.1.2
   - Features: v0.2.0, v0.3.0
   - Stable: v1.0.0

2. **Changelog**:
   - Selalu update CHANGELOG.md
   - Document breaking changes
   - Mention new features

3. **Pre-release**:
   - Gunakan "pre-release" untuk testing
   - Setelah matang, buat release stabil

---

**Sudah Ready!** Code sudah ter-push, tinggal buat release di GitHub website! 🚀
