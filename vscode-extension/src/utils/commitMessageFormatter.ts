import { CommitMessage } from '../types';

export class CommitMessageFormatter {
  static formatConventional(commit: CommitMessage): string {
    let message = '';
    
    if (commit.type) {
      message += commit.type;
    }
    
    if (commit.scope) {
      message += `(${commit.scope})`;
    }
    
    if (commit.subject) {
      message += `: ${commit.subject}`;
    }
    
    if (commit.body) {
      message += `\n\n${commit.body}`;
    }
    
    return message;
  }

  static formatEmoji(commit: CommitMessage): string {
    const emojiMap: { [key: string]: string } = {
      feat: '✨',
      fix: '🐛',
      docs: '📝',
      style: '💄',
      refactor: '♻️',
      perf: '⚡',
      test: '✅',
      build: '📦',
      ci: '👷',
      chore: '🔧',
      revert: '⏪'
    };

    let message = '';
    
    if (commit.type) {
      const emoji = emojiMap[commit.type] || '📝';
      message += `${emoji} ${commit.type}`;
    }
    
    if (commit.subject) {
      message += `: ${commit.subject}`;
    }
    
    if (commit.body) {
      message += `\n\n${commit.body}`;
    }
    
    return message;
  }

  static formatSimple(commit: CommitMessage): string {
    let message = commit.subject;
    
    if (commit.body) {
      message += `\n\n${commit.body}`;
    }
    
    return message;
  }

  static parseCommitMessage(rawMessage: string): CommitMessage {
    const lines = rawMessage.split('\n');
    const firstLine = lines[0];
    
    const commit: CommitMessage = {
      type: '',
      subject: ''
    };

    const conventionalMatch = firstLine.match(/^(\w+)(?:\(([^)]+)\))?: (.+)$/);
    if (conventionalMatch) {
      commit.type = conventionalMatch[1];
      commit.scope = conventionalMatch[2];
      commit.subject = conventionalMatch[3];
    } else {
      commit.subject = firstLine;
    }

    if (lines.length > 1) {
      const bodyStart = lines.findIndex(line => line.trim().length > 0);
      if (bodyStart > 0) {
        commit.body = lines.slice(bodyStart).join('\n');
      }
    }

    return commit;
  }
}
