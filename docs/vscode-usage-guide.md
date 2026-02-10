# Cara Menggunakan Commit by Lee Extension di VSCode

## ⚠️ Masalah yang Kamu Alami

Error: `zsh: command not found: Commit`

**Penyebab**: Kamu menjalankan command di terminal zsh, bukan di VSCode Command Palette.

---

## ✅ Cara Penggunaan yang Benar

### Method 1: Menggunakan Keyboard Shortcut (Paling Mudah)

1. **Stage changes dulu**:
   ```bash
   git add .
   ```
   atau gunakan VSCode Source Control panel

2. **Tekan keyboard shortcut**:
   - macOS: `Cmd + Shift + G`
   - Windows/Linux: `Ctrl + Shift + G`

3. Extension akan:
   - Mengecek koneksi Ollama
   - Menganalisa staged changes
   - Generate commit message
   - Menampilkan preview panel

4. Pilih aksi:
   - **Accept** - Commit dengan message tersebut
   - **Edit** - Edit message sebelum commit
   - **Cancel** - Batalkan

---

### Method 2: Menggunakan Command Palette

1. **Stage changes dulu**:
   ```bash
   git add .
   ```

2. **Buka Command Palette**:
   - macOS: Tekan `Cmd + Shift + P`
   - Windows/Linux: Tekan `Ctrl + Shift + P`

3. **Ketik**: `Commit by Lee`

4. **Pilih command**:
   - `Commit by Lee: Generate Commit Message`
   - Atau `Commit by Lee: Test Ollama Connection`
   - Atau `Commit by Lee: Open Configuration`

5. Extension akan berjalan

---

## ⚙️ Konfigurasi Pertama Kali

Sebelum menggunakan, kamu perlu konfigurasi Ollama server:

### 1. Buka Settings

- macOS: `Cmd + ,`
- Windows/Linux: `Ctrl + ,`

### 2. Search "commitbylee"

### 3. Configure settings:

```
commitbylee.ollamaHost: http://localhost:11434
commitbylee.ollamaModel: qwen3:4b
commitbylee.language: id (atau en)
commitbylee.style: conventional
commitbylee.autoCommit: false
```

### 4. Jika punya Ollama server sendiri:

```
commitbylee.ollamaHost: http://your-server.com:port
```

---

## 🔍 Test Koneksi Dulu

Sebelum generate commit message, test koneksi dulu:

1. **Buka Command Palette** (`Cmd/Ctrl + Shift + P`)

2. **Ketik**: `test connection`

3. **Pilih**: `Commit by Lee: Test Ollama Connection`

4. **Lihat output** di panel "Commit by Lee - Connection Test"

5. Jika sukses:
   ```
   [OK] Connection successful!
   Found X model(s):
     • qwen3:4b
   ```

6. Jika gagal:
   - Cek URL Ollama di settings
   - Pastikan Ollama server running
   - Cek koneksi internet

---

## 📝 Workflow Lengkap

### Step 1: Buat Changes
Edit file-file di project kamu

### Step 2: Stage Changes
```bash
# Stage semua changes
git add .

# Atau stage file tertentu
git add file1.ts file2.ts
```

### Step 3: Generate Commit Message
**Tekan**: `Cmd + Shift + G` (macOS)

### Step 4: Preview
Extension akan menampilkan panel preview dengan:
- Generated commit message
- Files changed summary
- Insertions/deletions count

### Step 5: Pilih Aksi
- **Accept**: Langsung commit
- **Edit**: Edit message dulu, then commit
- **Cancel**: Batalkan

---

## 🎯 Command List

| Command | Shortcut | Description |
|---------|----------|-------------|
| Generate Commit Message | `Cmd/Ctrl + Shift + G` | Generate & preview commit message |
| Test Ollama Connection | - | Test koneksi ke Ollama server |
| Open Configuration | - | Buka settings extension |

---

## 🔧 Troubleshooting

### Problem 1: "Command not found"

**Cause**: Menjalankan command di terminal zsh

**Solution**:
- ❌ Jangan jalankan di terminal
- ✅ Gunakan Command Palette atau keyboard shortcut

### Problem 2: "No staged changes found"

**Solution**:
- Stage changes dulu: `git add .`
- Atau gunakan Source Control panel

### Problem 3: "Connection failed"

**Solution**:
1. Cek settings Ollama host
2. Test connection dulu
3. Pastikan Ollama server running
4. Cek koneksi internet

### Problem 4: Extension tidak muncul

**Solution**:
1. Reload VSCode: `Cmd/Ctrl + Shift + P` → "Reload Window"
2. Check Extensions panel (Cmd/Ctrl + Shift + X)
3. Cari "Commit by Lee"
4. Pastikan extension enabled

---

## 💡 Tips

1. **Test connection dulu** sebelum generate commit
2. **Stage related changes together** untuk commit yang lebih baik
3. **Review message** di preview panel sebelum accept
4. **Edit jika perlu** untuk menyesuaikan dengan style tim kamu
5. **Enable auto-commit** di settings jika ingin skip preview

---

## 🎓 Quick Reference

### Generate Commit Message
```
1. git add .
2. Cmd + Shift + G (macOS)
3. Preview & Accept
```

### Test Connection
```
1. Cmd + Shift + P
2. Ketik: "test connection"
3. Enter
```

### Open Settings
```
1. Cmd + ,
2. Search: "commitbylee"
3. Configure
```

---

## ✅ Checklist Sebelum Menggunakan

- [ ] Extension sudah terinstall
- [ ] Ollama host sudah di-konfigurasi di settings
- [ ] Test connection berhasil
- [ ] Ada staged changes (`git add .`)
- [ ] Menjalankan command dari Command Palette atau keyboard shortcut, bukan dari terminal

---

**Selamat menggunakan Commit by Lee!** 🚀

Jika ada masalah, cek Output panel di VSCode:
`View` → `Output` → Pilih "Commit by Lee" dari dropdown
