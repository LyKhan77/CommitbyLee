import { GitDiffStats } from '../types';

export class PromptGenerator {
  static generateCommitPrompt(
    diff: string,
    stats: GitDiffStats,
    language: 'id' | 'en'
  ): string {
    const langText = language === 'id' 
      ? 'Bahasa Indonesia'
      : 'English';
    
    const introText = language === 'id'
      ? `Analisa diff berikut dan buat commit message yang deskriptif dalam Bahasa Indonesia.`
      : `Analyze the following diff and create a descriptive commit message in English.`;

    return `
${introText}

Git Diff:
${diff}

Summary:
- Files changed: ${stats.filesChanged}
- Insertions: +${stats.insertions}
- Deletions: -${stats.deletions}

Format output sebagai Conventional Commits:
type(scope): subject

body

Examples:
feat(api): tambahkan endpoint user registration

Membuat endpoint POST /api/users/register untuk registrasi pengguna baru dengan validasi email

OR:

fix(auth): perbaiki validasi password

- Tambah minimum length check
- Perbaiki error message

Rules:
1. Gunakan type yang sesuai: feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert
2. Subject harus singkat dan jelas
3. Body jelaskan "apa" dan "mengapa", bukan "bagaimana"
4. Output HANYA commit message, tanpa penjelasan tambahan

Commit message:
`;
  }
}
