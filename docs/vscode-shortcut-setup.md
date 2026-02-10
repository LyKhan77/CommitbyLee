# Cara Setting Keyboard Shortcut Commit by Lee di VSCode

## Masalah
`Cmd + Shift + G` di macOS sudah dipakai oleh KiloCode (atau aplikasi lain)

## Solusi: Override Shortcut di VSCode

### Method 1: Via Keyboard Shortcuts UI (Paling Mudah)

#### Di macOS:

1. **Buka Keyboard Shortcuts**:
   - Tekan: `Cmd + K` lalu `Cmd + S`
   - Atau: Menu bar → `Code` → `Preferences` → `Keyboard Shortcuts`
   - Atau: `Cmd + Shift + P` → ketik "keyboard shortcuts"

2. **Cari Command Commit by Lee**:
   - Di search box, ketik: `commitbylee`
   - Atau ketik: `generate commit`

3. **Edit Shortcut**:
   - Cari: `Commit by Lee: Generate Commit Message`
   - Klik icon ✏️ (pencil) di sebelah shortcutnya
   - Tekan shortcut baru yang kamu mau, misalnya:
     - `Cmd + Alt + G`
     - `Cmd + Shift + C`
     - `Ctrl + Shift + G` (jika mau pakai Ctrl)

4. **Save**:
   - Setelah tekan, VSCode akan otomatis save
   - Kamu akan lihat shortcut baru di situ

5. **Test**:
   - Tekan shortcut yang baru di-set
   - Extension akan berjalan!

---

### Method 2: Edit keybindings.json Langsung

1. **Buka keybindings.json**:
   - `Cmd + Shift + P`
   - Ketik: `preferences: open keyboard shortcuts (json)`
   - Enter

2. **Tambahkan konfigurasi**:
   ```json
   [
     {
       "key": "cmd+alt+g",
       "command": "commitbylee.generate",
       "when": "editorTextFocus || !editorTextFocus"
     }
   ]
   ```

3. **Simpan dan test**:
   - Save file (Cmd + S)
   - Tekan `Cmd + Alt + G`
   - Extension berjalan!

---

## 💡 Rekomendasi Shortcut yang Aman

### Untuk macOS:

| Shortcut | Status | Catatan |
|----------|--------|---------|
| `Cmd + Alt + G` | ✅ Aman | Tidak konflik dengan default macOS |
| `Cmd + Shift + C` | ✅ Aman | "C" untuk Commit |
| `Cmd + Shift + A` | ✅ Aman | "A" untuk AI |
| `Ctrl + Shift + G` | ✅ Aman | Beda dari Cmd |

### Untuk Windows/Linux:

| Shortcut | Status | Catatan |
|----------|--------|---------|
| `Ctrl + Alt + G` | ✅ Aman | Tidak konflik |
| `Ctrl + Shift + C` | ✅ Aman | "C" untuk Commit |
| `Ctrl + Shift + A` | ✅ Aman | "A" untuk AI |

---

## 🔍 Cek Shortcut yang Konflik

### Di VSCode:

1. Buka Keyboard Shortcuts (`Cmd + K`, `Cmd + S`)
2. Cari shortcut yang mau dipakai
3. Lihat apakah sudah dipakai command lain
4. Jika sudah, pilih shortcut lain

### Shortcut yang Sering Konflik di macOS:

- ❌ `Cmd + Shift + G` - KiloCode, Quick Find
- ❌ `Cmd + G` - Find Next
- ❌ `Cmd + Shift + F` - Find in Files
- ❌ `Cmd + P` - Quick Open

### Shortcut yang Aman:

- ✅ `Cmd + Alt + G`
- ✅ `Cmd + Alt + C`
- ✅ `Cmd + Shift + C`
- ✅ `Ctrl + Shift + G` (beda tombol)

---

## 🎯 Cara Paling Mudah (Saya Sarankan)

### Pakai Command Palette Saja:

1. **Stage changes**:
   ```bash
   git add .
   ```

2. **Buka Command Palette**:
   - Tekan: `Cmd + Shift + P`
   
3. **Ketik**: `generate`

4. **Pilih**: `Commit by Lee: Generate Commit Message`

5. **Enter** dan selesai!

**Kelebihan**:
- ✅ Tidak perlu setting shortcut
- ✅ Tidak ada konflik
- ✅ Works di semua OS
- ✅ Mudah diingat

---

## 🔧 Tips

### 1. Buat Shortcut yang Mudah Diingat
- `Cmd + Alt + G` → **G**enerate
- `Cmd + Shift + C` → **C**ommit
- `Cmd + Alt + C` → **C**ommit

### 2. Cek Shortcuts yang Sudah Di-set:
```
Cmd + Shift + P → "key shortcuts"
Lihat semua shortcuts yang sudah di-custom
```

### 3. Reset ke Default:
Jika salah set:
- Buka Keyboard Shortcuts UI
- Cari command
- Klik "Reset" (ikon ↺)

---

## ✅ Quick Test

Setelah set shortcut:

1. Stage changes:
   ```bash
   git add .
   ```

2. Tekan shortcut baru (misal `Cmd + Alt + G`)

3. Preview panel muncul!

4. ✅ Success!

---

## 📖 Referensi

- [VSCode Keyboard Shortcuts](https://code.visualstudio.com/docs/getstarted/keybindings)
- [VSCode Command Palette](https://code.visualstudio.com/docs/getstarted/tips-and-tricks#_command-palette)

---

**Rekomendasi**: Pakai Command Palette (`Cmd + Shift + P` → "generate") tanpa perlu setting shortcut khusus.
