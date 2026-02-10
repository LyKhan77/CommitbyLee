import * as vscode from 'vscode';
import { GitDiffStats, GitFileChange } from '../types';

export class GitClient {
  private gitApi: any;

  constructor() {
    const extension = vscode.extensions.getExtension('vscode.git');
    if (!extension) {
      throw new Error('Git extension not found');
    }
  }

  private async getGitApi(): Promise<any> {
    if (!this.gitApi) {
      const extension = vscode.extensions.getExtension('vscode.git');
      if (!extension) {
        throw new Error('Git extension not available');
      }
      await extension.activate();
      this.gitApi = extension.exports;
    }
    return this.gitApi;
  }

  async getRepository(): Promise<any> {
    const api = await this.getGitApi();
    const repositories = api.repositories;
    
    if (!repositories || repositories.length === 0) {
      throw new Error('No git repository found');
    }
    
    return repositories[0];
  }

  async getStagedDiff(): Promise<string> {
    const repo = await this.getRepository();
    
    return new Promise((resolve, reject) => {
      repo.diff(true).then((diff: string) => {
        resolve(diff);
      }, (error: any) => {
        reject(error);
      });
    });
  }

  async getChanges(): Promise<GitFileChange[]> {
    const repo = await this.getRepository();
    const changes = repo.state.indexChanges;
    
    return changes.map((change: any) => ({
      path: change.path,
      status: change.status
    }));
  }

  async getDiffStats(): Promise<GitDiffStats> {
    const diff = await this.getStagedDiff();
    
    const stats: GitDiffStats = {
      filesChanged: 0,
      insertions: 0,
      deletions: 0
    };

    const lines = diff.split('\n');
    for (const line of lines) {
      if (line.startsWith('+++') || line.startsWith('---')) {
        stats.filesChanged++;
      } else if (line.startsWith('+') && !line.startsWith('+++')) {
        stats.insertions++;
      } else if (line.startsWith('-') && !line.startsWith('---')) {
        stats.deletions++;
      }
    }

    stats.filesChanged = Math.floor(stats.filesChanged / 2);
    
    return stats;
  }

  async commit(message: string): Promise<void> {
    const repo = await this.getRepository();
    await repo.commit(message);
  }
}
