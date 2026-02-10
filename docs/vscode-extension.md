# VSCode Extension Deployment Guide

## Overview

VSCode extension for **Commit by Lee** telah berhasil dibuat dan dikemas! Extension ini memungkinkan kamu menghasilkan commit message secara otomatis menggunakan AI langsung dari VSCode.

## 📦 Package Location

Extension telah dikemas ke dalam file:
```
vscode-extension/commit-by-lee-0.1.0.vsix
```

## 🚀 Cara Install di VSCode

### Method 1: Install dari VSIX File (Disarankan)

1. Buka VSCode
2. Buka panel Extensions (Ctrl+Shift+X)
3. Klik menu "..." (tiga titik) di pojok kanan atas panel Extensions
4. Pilih **"Install from VSIX..."**
5. Pilih file `commit-by-lee-0.1.0.vsix` dari folder `vscode-extension`
6. VSCode akan menginstall extension dan meminta reload

### Method 2: Install dalam Mode Development

Untuk development dan testing:

1. Buka folder extension di VSCode:
   ```bash
   code D:\Occupation\Lee\Lee-AI\commit-by-lee\vscode-extension
   ```

2. Install dependencies (sudah dilakukan sebelumnya):
   ```bash
   npm install
   ```

3. Tekan **F5** untuk membuka Extension Development Host dengan extension ter-load

## ⚙️ Konfigurasi

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

## 🎯 Cara Menggunakan

### Generate Commit Message

1. Buat perubahan pada code kamu
2. Stage perubahan: `git add .` (atau gunakan Source Control panel di VSCode)
3. Tekan **Ctrl+Shift+G** atau buka Command Palette (Ctrl+Shift+P) dan pilih **"Commit by Lee: Generate Commit Message"**
4. Extension akan:
   - Mengecek koneksi Ollama
   - Menganalisa staged changes
   - Generate commit message dengan AI
   - Menampilkan preview panel
5. Pilih **Accept** untuk commit, **Edit** untuk mengubah, atau **Cancel** untuk batalkan

### Test Koneksi Ollama

1. Buka Command Palette (Ctrl+Shift+P)
2. Pilih **"Commit by Lee: Test Ollama Connection"**
3. Cek output channel "Commit by Lee - Connection Test" untuk hasilnya

### Buka Konfigurasi

1. Buka Command Palette (Ctrl+Shift+P)
2. Pilih **"Commit by Lee: Open Configuration"**
3. VSCode akan membuka settings untuk extension

## 📁 Struktur Project

```
vscode-extension/
├── .vscode/              # VSCode config untuk development
├── src/                  # Source code TypeScript
│   ├── client/          # Ollama & Git clients
│   ├── commands/        # Command handlers
│   ├── config/          # Configuration management
│   ├── types/           # TypeScript types
│   └── utils/           # Utility functions
├── webview/             # Webview panel untuk preview
├── out/                 # Compiled JavaScript
├── package.json         # Extension manifest
├── tsconfig.json        # TypeScript config
├── webpack.config.js    # Webpack build config
└── commit-by-lee-0.1.0.vsix  # Package extension
```

## 🔧 Fitur yang Tersedia

### Core Features
- ✅ Generate commit message dari staged changes
- ✅ Interactive preview panel dengan Accept/Edit/Cancel buttons
- ✅ Test koneksi ke Ollama server
- ✅ List available models
- ✅ Multilingual (Bahasa Indonesia & English)
- ✅ Multiple commit styles (Conventional, Emoji, Simple)
- ✅ Configurable settings
- ✅ Keyboard shortcut (Ctrl+Shift+G)
- ✅ Auto-commit option
- ✅ Git integration via VSCode Git Extension API

### Commands
- `commitbylee.generate` - Generate commit message
- `commitbylee.testConnection` - Test Ollama connection
- `commitbylee.openConfig` - Open settings

## 🎨 Gaya Commit Message

### Conventional Commits (Default)
```
feat(api): tambahkan endpoint user registration

Membuat endpoint POST /api/users/register untuk
registrasi pengguna baru dengan validasi email
```

### Emoji Style
```
✨ feat: tambahkan endpoint user registration

Membuat endpoint POST /api/users/register untuk
registrasi pengguna baru dengan validasi email
```

### Simple Style
```
Tambahkan endpoint user registration dengan validasi email
```

## 🔍 Troubleshooting

### Extension Not Activating
- Pastikan VSCode versi 1.85.0 atau lebih baru
- Check Output panel > "Commit by Lee" untuk error messages

### Connection Failed
- Verifikasi Ollama server URL di settings
- Test connection manual: `curl https://ollama.iotech.my.id/api/tags`
- Pastikan server Ollama accessible

### No Staged Changes
- Stage changes dulu: `git add .` atau gunakan Source Control panel
- Pastikan ada perubahan yang di-stage

### Build Issues
```bash
# Clean dan rebuild
cd vscode-extension
rm -rf node_modules out
npm install
npm run compile
vsce package
```

## 🚀 Publish ke Marketplace (Optional)

Untuk mempublish extension ke VSCode Marketplace:

1. Buat account di [marketplace.visualstudio.com](https://marketplace.visualstudio.com)
2. Buat Personal Access Token
3. Login ke vsce:
   ```bash
   vsce login <publisher-name>
   ```
4. Publish:
   ```bash
   vsce publish
   ```

Note: Package.json harus punya `repository` field untuk publish.

## 📝 File Penting

- **package.json** - Extension manifest dengan commands, config, dan metadata
- **src/extension.ts** - Entry point extension, registrasi commands
- **src/commands/generateCommit.ts** - Logic utama generate commit
- **src/client/ollama.ts** - Ollama API client
- **src/client/git.ts** - Git operations wrapper
- **webview/commitPreview.ts** - Interactive preview panel
- **commit-by-lee-0.1.0.vsix** - Installable package

## 🎓 Selanjutnya

1. Install extension di VSCode
2. Configure settings
3. Test connection ke Ollama
4. Generate commit message pertama kamu!
5. Baca [Usage Guide](usage.md) untuk lebih detail

## 💡 Tips

- Gunakan keyboard shortcut `Ctrl+Shift+G` untuk quick access
- Enable `autoCommit` di settings untuk skip confirmation
- Customize commit style sesuai preference tim kamu
- Test connection dulu sebelum generate commit message
- Review commit message di preview panel sebelum accept

---

Extension VSCode untuk Commit by Lee sudah siap digunakan! 🎉

Lihat folder `vscode-extension/` untuk source code lengkap dan dokumentasi tambahan.
