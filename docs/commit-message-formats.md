# Format Hasil Generate Commit by Lee

## Jawaban Singkat
**Tidak!** Hasil generate bisa multi-line dengan Conventional Commits format.

---

## 📝 3 Style Commit Message

### 1. Conventional Commits (Default) - Multi-Line

**Format**:
```
type(scope): subject

body
```

**Contoh Hasil Generate**:
```
feat(auth): tambahkan autentikasi pengguna

Implement OAuth2 login flow dengan Google provider untuk
memudahkan user login tanpa perlu remember password.
```

**Struktur**:
- **Line 1**: `type(scope): subject`
- **Line 2**: (Empty)
- **Line 3+**: Body (penjelasan detail)

### 2. Emoji Style - Multi-Line

**Format**:
```
🎉 type: subject

body
```

**Contoh Hasil Generate**:
```
✨ feat: tambahkan autentikasi pengguna

Implement OAuth2 login flow dengan Google provider
```

### 3. Simple Style - One-Line

**Format**:
```
subject only
```

**Contoh Hasil Generate**:
```
Tambahkan fitur autentikasi pengguna dengan OAuth2
```

---

## 🎯 Detail Conventional Commits (Default)

### Components:

1. **Type**: Kategori perubahan
   - `feat` - Fitur baru
   - `fix` - Bug fix
   - `docs` - Documentation
   - `style` - Format code
   - `refactor` - Refactor code
   - `test` - Test
   - `chore` - Maintenance

2. **Scope** (Opsional): Area yang diubah
   - `(auth)` - Authentication
   - `(api)` - API
   - `(ui)` - User Interface
   - `(db)` - Database

3. **Subject**: Deskripsi singkat (max 50 karakter)
   - Tidak diakhiri titik
   - Menggunakan imperative mood

4. **Body** (Opsional): Penjelasan detail
   - Apa yang diubah dan mengapa
   - Bisa multi-paragraph
   - Gunakan bullet points jika perlu

---

## 📋 Contoh Real-World Hasil Generate

### Example 1: Fitur Baru (Multi-Line)

```
feat(api): tambahkan endpoint user registration

Membuat endpoint POST /api/users/register untuk registrasi
pengguna baru dengan validasi email dan password.

Validasi:
- Email harus unique
- Password minimal 8 karakter
- Confirm password harus match
```

### Example 2: Bug Fix (Multi-Line)

```
fix(auth): perbaiki validasi token expired

Token JWT kadang tidak terdeteksi expired karena timezone
issue. Sekarang menggunakan UTC untuk semua perbandingan waktu.

Changes:
- Convert semua datetime ke UTC
- Tambah buffer time 5 detik
- Fix test cases
```

### Example 3: Refactor (Multi-Line)

```
refactor(api): optimasi query database

- Reduce query count dari 5 ke 2
- Add caching untuk frequently accessed data
- Improve response time dari 500ms ke 150ms
```

### Example 4: Documentation (Multi-Line)

```
docs(api): update API documentation

Menambahkan dokumentasi untuk endpoint baru:
- POST /api/users/register
- POST /api/users/login
- GET /api/users/profile

Serta update examples dan error codes.
```

### Example 5: Simple (One-Line)

```
Update copyright year di semua files
```

---

## 🎨 Cara Setting Style

### Via Command Line:

```bash
# Conventional commits (default, multi-line)
commit-by-lee generate --style conventional

# Emoji style (multi-line dengan emoji)
commit-by-lee generate --style emoji

# Simple style (one-line only)
commit-by-lee generate --style simple
```

### Via VSCode Extension:

1. Buka Settings (`Cmd + ,`)
2. Search: `commitbylee.style`
3. Pilih:
   - `conventional` - Multi-line dengan format
   - `emoji` - Multi-line dengan emoji
   - `simple` - One-line saja

---

## 🤖 Kenapa Multi-Line Lebih Baik?

### Advantages:

1. **Lebih Informatif**
   - Subject untuk quick glance
   - Body untuk penjelasan detail

2. **Follow Best Practice**
   - Conventional Commits standard
   - Diadopsi banyak project besar
   - Compatible dengan semantic versioning

3. **Better Git History**
   - `git log` lebih readable
   - Mudah search dengan `git log --grep`
   - Bisa generate changelog otomatis

4. **Team Collaboration**
   - Standard format
   - Mudah dipahami
   - Clear intent

### Contoh Git Log dengan Multi-Line:

```bash
$ git log --format="%h %s%n%b" -3

feat(api): tambahkan endpoint user registration

Membuat endpoint POST /api/users/register untuk registrasi
pengguna baru.

fix(auth): perbaiki validasi token expired

Token JWT kadang tidak terdeteksi expired karena timezone issue.

docs(api): update API documentation

Menambahkan dokumentasi untuk endpoint baru.
```

---

## 📊 Perbandingan Style

| Style | Lines | Format | Use Case |
|-------|-------|--------|----------|
| **Conventional** | Multi | `type(scope): subject\n\nbody` | Production, team projects |
| **Emoji** | Multi | `✨ type: subject\n\nbody` | Personal projects, fun |
| **Simple** | Single | `subject only` | Quick/ trivial changes |

---

## 💡 Tips

1. **Default adalah Conventional** (multi-line)
   - Paling fleksibel
   - Best practice
   - Recommended untuk production

2. **Gunakan Simple** untuk:
   - Trivial changes
   - Update documentation
   - Minor fixes

3. **Gunakan Emoji** untuk:
   - Personal projects
   - Fun projects
   - Lebih visual

4. **Subject Line** (line 1):
   - Maksimal 50 karakter
   - Tidak pakai titik
   - Imperative mood ("add" bukan "added")

5. **Body** (line 3+):
   - Jelaskan "apa" dan "mengapa"
   - Bukan "bagaimana"
   - Bisa pakai bullet points

---

## ✅ Summary

| Pertanyaan | Jawaban |
|------------|---------|
| Apakah hanya one-line? | ❌ Tidak, bisa multi-line |
| Default format apa? | Conventional Commits (multi-line) |
| Bisa pilih style? | ✅ Ya, 3 pilihan style |
| Bisa custom? | ✅ Ya, di settings |

---

**Kesimpulan**: Commit by Lee generate **multi-line commit messages** secara default dengan Conventional Commits format, bukan one-line saja! 🎉
