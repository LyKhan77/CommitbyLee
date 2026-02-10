# Cara Cek Log Commit Git

## Di Terminal / Command Line

### 1. Log Dasar (Cek Semua Commit)

```bash
git log
```

**Output**:
```
commit bce8596... (HEAD -> main)
Author: Lee
Date:   Mon Feb 10 09:30:00 2026

    docs: add git fix troubleshooting guide

commit addc7ae...
Author: Lee
Date:   Mon Feb 10 09:15:00 2026

    fix: add command-line git fallback for better repository detection
```

### 2. Log Singkat (Satu Baris per Commit)

```bash
git log --oneline
```

**Output**:
```
bce8596 docs: add git fix troubleshooting guide
addc7ae fix: add command-line git fallback
451a0ee feat: add bear logo and mask Ollama host configuration
f405995 docs: add GitHub release guide and release notes
88cbefa feat: add VSCode extension for AI-powered commit message generation
```

### 3. Log dengan Graf (Lebih Visual)

```bash
git log --graph --oneline --all
```

**Output**:
```
* bce8596 (HEAD -> main, origin/main) docs: add git fix troubleshooting guide
* addc7ae fix: add command-line git fallback
* 451a0ee feat: add bear logo and mask Ollama host configuration
* f405995 docs: add GitHub release guide and release notes
* 88cbefa feat: add VSCode extension for AI-powered commit message generation
```

### 4. Log dengan Detail (N Committee Terakhir)

```bash
# Lihat 5 commit terakhir
git log -5

# Lihat 3 commit terakhir, singkat
git log --oneline -3
```

### 5. Log dengan Format Kustom

```bash
git log --pretty=format:"%h - %an, %ar : %s"
```

**Output**:
```
bce8596 - Lee, 5 minutes ago : docs: add git fix troubleshooting guide
addc7ae - Lee, 20 minutes ago : fix: add command-line git fallback
451a0ee - Lee, 1 hour ago : feat: add bear logo and mask Ollama host configuration
```

**Legend**:
- `%h` - Short commit hash
- `%an` - Author name
- `%ar` - Author date (relative)
- `%s` - Subject (commit message)

### 6. Cek Commit Tertentu

```bash
# Lihat detail commit tertentu
git show <commit-hash>

# Contoh:
git show bce8596
```

**Output**:
```
commit bce8596...
Author: Lee <lee@example.com>
Date:   Mon Feb 10 09:30:00 2026

    docs: add git fix troubleshooting guide

    Comprehensive guide for troubleshooting...

diff --git a/docs/git-fix-guide.md b/docs/git-fix-guide.md
new file mode 100644
index 0000000..1234567
--- /dev/null
+++ b/docs/git-fix-guide.md
@@ -0,0 +1,279 @@
+# ✅ Perbaikan Masalah "No Git repository found"
```

### 7. Filter Log Berdasarkan Author

```bash
# Lihat commit dari author tertentu
git log --author="Lee"

# Lihat commit kamu sendiri
git log --author="$(git config user.name)"
```

### 8. Filter Log Berdasarkan Pesan

```bash
# Cari commit dengan kata tertentu
git log --grep="extension"

# Cari commit dengan kata "fix"
git log --grep="fix" --oneline
```

**Output**:
```
addc7ae fix: add command-line git fallback
```

### 9. Log per File

```bash
# Lihat history file tertentu
git log -- <file-path>

# Contoh:
git log -- package.json

# Lihat file yang berubah di commit
git log --name-only
```

### 10. Log Statistik

```bash
# Lihat statistik perubahan
git log --stat

# Lihat ringkasan grafik
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
```

---

## Di VSCode

### Method 1: Source Control Panel

1. **Buka Source Control**:
   - Tekan: `Cmd + Shift + G` (macOS) atau `Ctrl + Shift + G` (Windows/Linux)
   - Atau klik icon branch di sidebar (pojok kiri bawah)

2. **Lihat History**:
   - Klik menu "..." (tiga titik) di Source Control panel
   - Pilih: "Show Git History"
   - Atau: "View → Open View → Git History"

3. **Navigate**:
   - Klik commit untuk melihat detail
   - Klik kanan untuk options (Copy ID, Create Branch, dll)

### Method 2: Git Graph Extension

1. **Install Extension**:
   - `Cmd + Shift + X` (Extensions)
   - Search: "Git Graph"
   - Install

2. **Buka Git Graph**:
   - `Cmd + Shift + P`
   - Ketik: "git graph"
   - Pilih: "Git Graph: Show Graph"

3. **Lihat Visual Graph**:
   - Timeline visual
   - Branch visualization
   - Commit details
   - Diff viewer

---

## GitHub Website

### Cek Log di GitHub:

1. **Buka Repository**:
   ```
   https://github.com/LyKhan77/CommitbyLee
   ```

2. **Click "Commits"**:
   - Di atas code, klik "commits" (sebelah "Add file")
   - Atau: https://github.com/LyKhan77/CommitbyLee/commits/main

3. **Lihat History**:
   - Scroll untuk melihat semua commits
   - Klik commit untuk detail
   - Lihat diff changes

---

## Tips & Tricks

### 1. Cek Commit Hari Ini
```bash
git log --since="today" --oneline
```

### 2. Cek Commit Minggu Ini
```bash
git log --since="1 week ago" --oneline
```

### 3. Cek Commit antara Dua Tag
```bash
git log v0.0.1..v0.1.0 --oneline
```

### 4. Search di Semua Commit Messages
```bash
git log --all --grep="keyword"
```

### 5. Cek Commit yang Mengubah File Tertentu
```bash
git log --follow -- <file-path>
```

### 6. Lihat Commit dengan Nice Format
```bash
git log --pretty=format:"%C(yellow)%h%Cred%d\\ %Creset%s%Cblue\\ [%cn]" --decorate --date=short
```

### 7. Lihat siapa yang paling banyak commit
```bash
git shortlog -sn
```

**Output**:
```
  5  Lee
  2  factory-droid[bot]
```

---

## Quick Reference

| Command | Deskripsi |
|---------|-----------|
| `git log` | Log lengkap |
| `git log --oneline` | Satu baris per commit |
| `git log -5` | 5 commit terakhir |
| `git log --graph` | Visual graph |
| `git show <hash>` | Detail commit |
| `git log --author="name"` | Filter author |
| `git log --grep="text"` | Search pesan |
| `git log --stat` | Dengan statistik |

---

## Contoh Use Cases

### Cek Apakah Extension Extension Sudah Ter-commit:
```bash
cd D:\Occupation\Lee\Lee-AI\commit-by-lee
git log --oneline --grep="extension"
```

### Cek Commit Terakhir:
```bash
git log -1 --stat
```

### Cek Apakah VSIX File Sudah Ter-commit:
```bash
git log --all --full-history -- vscode-extension/commit-by-lee-0.1.0.vsix
```

### Lihat Semua Commit di Branch Main:
```bash
git log main --oneline
```

---

## Di Commit by Lee Project Kamu

Untuk cek log project ini:

```bash
# Masuk ke folder project
cd D:\Occupation\Lee\Lee-AI\commit-by-lee

# Lihat semua commit (singkat)
git log --oneline

# Lihat 10 commit terakhir
git log --oneline -10

# Lihat graf
git log --graph --oneline --all

# Lihat commit terakhir dengan detail
git log -1 --stat
```

---

**Gunakan `git log --oneline` untuk quick check!** 🚀
