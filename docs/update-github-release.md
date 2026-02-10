# 🚀 Update GitHub Release dengan Preview Panel Fix

## Status: Perlu Update!

**Kenapa harus update?**
- ✅ Ada fix penting: Preview panel sekarang menampilkan full commit message dengan body
- ✅ Git detection fix untuk macOS
- ✅ Better error messages
- ❌ Release di GitHub masih versi lama (tanpa fix ini)

---

## 📋 Cara Update GitHub Release

### Quick Steps (5 Menit)

1. **Buka GitHub Release**:
   ```
   https://github.com/LyKhan77/CommitbyLee/releases/tag/v0.1.0
   ```

2. **Edit Release**:
   - Klik "Edit release" (pojok kanan atas)
   
3. **Ganti File VSIX**:
   - Scroll ke "Assets"
   - Delete file `commit-by-lee-0.1.0.vsix` yang lama
   - Upload file baru: `vscode-extension/commit-by-lee-0.1.0.vsix`
   - Size: 52.7 KB

4. **Update Release Notes**:
   Tambahkan di description:
   ```markdown
   ## What's Included
   
   ### Features
   - ✅ AI-powered commit message generation (Ollama + Qwen3:4B)
   - ✅ Multi-line commit messages (Conventional Commits)
   - ✅ Interactive preview panel
   - ✅ Git integration with command-line fallback
   - ✅ Multilingual (Indonesian & English)
   - ✅ Multiple commit styles
   - ✅ Configurable settings
   
   ### Latest Fixes (v0.1.0 - Updated)
   - ✅ Preview panel now shows full commit message with body
   - ✅ Git repository detection with command-line fallback
   - ✅ Better error messages with helpful tips
   - ✅ Workspace folder validation
   - ✅ Improved reliability across different git setups
   
   ### Installation
   1. Download `commit-by-lee-0.1.0.vsix` from this release
   2. Install in VSCode: Extensions → "..." → "Install from VSIX..."
   3. Reload VSCode
   4. Configure Ollama host in Settings
   5. Stage changes: `git add .`
   6. Generate: `Cmd + Shift + P` → "generate"
   ```

5. **Update Release Title**:
   ```
   🚀 Commit by Lee v0.1.0 - VSCode Extension (Updated)
   
   AI-powered commit message generator with full preview panel,
   git detection fixes, and multi-line commit messages.
   ```

6. **Save**:
   - Klik "Update release"

7. **Done!** ✅

---

## 📝 Changelog Summary

### Versi Sebelumnya (di GitHub):
- ❌ Preview panel hanya menampilkan subject line
- ❌ Git detection error di beberapa environment
- ❌ Error messages kurang jelas

### Versi Terbaru (perlu di-upload):
- ✅ Preview panel menampilkan full commit message dengan body
- ✅ Git detection dengan command-line fallback (works di semua environment)
- ✅ Better error messages dengan helpful tips
- ✅ Workspace validation
- ✅ Bear logo icon

---

## 🔍 Timeline Perubahan

| Commit | Description |
|--------|-------------|
| `88cbefa` | Initial VSCode extension |
| `f405995` | Add GitHub release guide |
| `451a0ee` | Add bear logo & mask Ollama host |
| `addc7ae` | Git detection fallback fix |
| `bce8596` | Git fix troubleshooting guide |
| `bdef3cd` | Preview panel full body fix ⭐ |

**Latest commit**: `bdef3cd` - Ini yang ada di VSIX terbaru!

---

## 🎯 Apa yang User Dapat

### Setelah Update Release:

User yang download dari GitHub akan dapat:

1. **Full Commit Message Preview**
   - Subject line
   - Body text
   - Multi-line format

2. **Git Detection yang Lebih Baik**
   - Works di macOS, Windows, Linux
   - Fallback ke command-line git
   - Tidak error "No Git repository found"

3. **Better Error Messages**
   - Helpful tips
   - Clear instructions
   - Troubleshooting guide

4. **Complete Documentation**
   - Installation guide
   - Usage guide
   - Format guide
   - Git log guide

---

## 📦 File yang Di-Upload

**File**: `commit-by-lee-0.1.0.vsix`
**Location**: `vscode-extension/commit-by-lee-0.1.0.vsix`
**Size**: 52.7 KB
**Includes**:
- bear.png icon
- All fixes (git detection, preview panel)
- Complete documentation
- Ready to install

---

## 🚀 Alternative: Buat Release Baru (v0.1.1)

Jika mau buat versi baru daripada update v0.1.0:

### Steps:

1. **Buat tag baru**:
   ```bash
   cd D:\Occupation\Lee\Lee-AI\commit-by-lee
   git tag v0.1.1
   git push origin v0.1.1
   ```

2. **Buat release baru** di GitHub:
   - Go to: https://github.com/LyKhan77/CommitbyLee/releases
   - Click "Draft a new release"
   - Tag: `v0.1.1`
   - Title: `v0.1.1 - Preview Panel Fix & Git Detection`
   - Upload VSIX terbaru
   - Publish

### Kelebihan:
- ✅ Ada version history
- ✅ User bisa see progress
- ✅ Bisa roll back jika perlu

### Kekurangan:
- ❌ Perlu buat tag baru
- ❌ Link download beda
- ❌ Lebih banyak steps

---

## 💡 Rekomendasi

**Option 1: Update v0.1.0** (Recommended)
- ✅ Lebih cepat
- ✅ Link download tetap sama
- ✅ Tidak perlu buat tag baru
- ✅ Tidak membingungkan user

**Option 2: Buat v0.1.1**
- ✅ Ada versioning
- ✅ Better history
- ❌ Link download berubah

**Saran**: Pakai Option 1 (Update v0.1.0) sekarang untuk quick fix.

---

## ✅ Checklist Update Release

### Sebelum Update:
- [ ] Fix sudah di-test
- [ ] Extension sudah rebuilt
- [ ] VSIX file siap (52.7 KB)
- [ ] Commit sudah push ke GitHub

### Saat Update:
- [ ] Buka release v0.1.0
- [ ] Delete VSIX lama
- [ ] Upload VSIX baru
- [ ] Update description
- [ ] Update title
- [ ] Save changes

### Setelah Update:
- [ ] Test download dari GitHub
- [ ] Install di VSCode
- [ ] Test generate commit
- [ ] Verify preview panel shows body
- [ ] Beritau user untuk re-download

---

## 🔗 Link Penting

**Release URL**:
```
https://github.com/LyKhan77/CommitbyLee/releases/tag/v0.1.0
```

**Download URL** (setelah update):
```
https://github.com/LyKhan77/CommitbyLee/releases/download/v0.1.0/commit-by-lee-0.1.0.vsix
```

**Edit Release**:
```
https://github.com/LyKhan77/CommitbyLee/releases/edit/v0.1.0
```

---

## 📝 Template Release Notes

Copy-paste ini ke GitHub Release:

```markdown
# 🚀 Commit by Lee v0.1.0 - VSCode Extension (Updated)

AI-powered commit message generator for VSCode using Ollama and Qwen3:4B.

## ✨ Features

- 🤖 **AI-Powered** - Generate commit messages with Ollama + Qwen3:4B
- 🌍 **Multilingual** - Support Indonesian & English
- 🎨 **Multiple Styles** - Conventional, Emoji, Simple
- 📝 **Multi-line Messages** - Full commit messages with body
- 🔧 **Git Integration** - Works with any git setup
- ⚙️ **Configurable** - Customize in VSCode settings

## 🛠️ What's Fixed (Latest Update)

### Preview Panel Fix
- ✅ Now displays full commit message with body text
- ✅ Preview matches actual commit message
- ✅ Better informed decision before committing

### Git Detection Fix
- ✅ Command-line git fallback for reliability
- ✅ Works on macOS, Windows, Linux
- ✅ No more "No Git repository found" errors

### Better UX
- ✅ Improved error messages with helpful tips
- ✅ Workspace folder validation
- ✅ Detailed output logs

## 📦 Installation

1. Download `commit-by-lee-0.1.0.vsix` below
2. Open VSCode
3. Go to Extensions (Ctrl/Cmd + Shift + X)
4. Click "..." → "Install from VSIX..."
5. Select the downloaded file
6. Reload VSCode

## ⚙️ Configuration

After installation, open Settings (Ctrl/Cmd + ,) and configure:

```json
{
  "commitbylee.ollamaHost": "http://localhost:11434",
  "commitbylee.ollamaModel": "qwen3:4b",
  "commitbylee.language": "id",
  "commitbylee.style": "conventional"
}
```

## 🚀 Usage

1. Stage changes: `git add .`
2. Open Command Palette: `Cmd/Ctrl + Shift + P`
3. Type "generate"
4. Select "Commit by Lee: Generate Commit Message"
5. Preview and accept the generated message!

## 📖 Documentation

- [Installation Guide](https://github.com/LyKhan77/CommitbyLee/blob/main/vscode-extension/INSTALL.md)
- [Usage Guide](https://github.com/LyKhan77/CommitbyLee/blob/main/docs/usage.md)
- [Commit Format Guide](https://github.com/LyKhan77/CommitbyLee/blob/main/docs/commit-message-formats.md)
- [Git Log Guide](https://github.com/LyKhan77/CommitbyLee/blob/main/docs/git-log-guide.md)

## 🙏 Credits

Built with ❤️ using:
- Ollama
- Qwen3:4B by Alibaba
- VSCode Extension API

---

**Note**: If you previously installed version 0.1.0, please reinstall to get the latest fixes!
```

---

## ⚡ Quick Action

Sekarang langsung update:

1. Buka: https://github.com/LyKhan77/CommitbyLee/releases/tag/v0.1.0
2. Click "Edit release"
3. Replace VSIX file
4. Update notes
5. Save

**5 menit selesai!** 🚀
