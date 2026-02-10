import * as vscode from 'vscode';
import { exec } from 'child_process';
import { promisify } from 'util';
import { GitDiffStats, GitFileChange } from '../types';

const execAsync = promisify(exec);

export class GitClient {
  private gitApi: any | null = null;
  private useCommandLine = false;

  constructor() {
    this.detectGitMethod();
  }

  private detectGitMethod() {
    const extension = vscode.extensions.getExtension('vscode.git');
    if (!extension) {
      this.useCommandLine = true;
      return;
    }
  }

  private async getGitApi(): Promise<any> {
    if (this.useCommandLine) {
      return null;
    }
    
    if (!this.gitApi) {
      const extension = vscode.extensions.getExtension('vscode.git');
      if (!extension) {
        this.useCommandLine = true;
        return null;
      }
      
      try {
        await extension.activate();
        this.gitApi = extension.exports;
        
        // Check if we have repositories
        if (!this.gitApi.repositories || this.gitApi.repositories.length === 0) {
          this.useCommandLine = true;
          return null;
        }
      } catch (error) {
        this.useCommandLine = true;
        return null;
      }
    }
    
    return this.gitApi;
  }

  async getRepository(): Promise<any> {
    const api = await this.getGitApi();
    
    if (this.useCommandLine || !api) {
      return null; // Will use command line fallback
    }
    
    const repositories = api.repositories;
    
    if (!repositories || repositories.length === 0) {
      this.useCommandLine = true;
      return null;
    }
    
    return repositories[0];
  }

  private async execGit(command: string): Promise<string> {
    try {
      const workspaceFolder = vscode.workspace.workspaceFolders?.[0];
      if (!workspaceFolder) {
        throw new Error('No workspace folder found');
      }

      const { stdout } = await execAsync(`git ${command}`, {
        cwd: workspaceFolder.uri.fsPath,
        env: { ...process.env }
      });
      
      return stdout.trim();
    } catch (error: any) {
      throw new Error(`Git command failed: ${error.message}`);
    }
  }

  async getStagedDiff(): Promise<string> {
    if (this.useCommandLine) {
      return await this.execGit('diff --cached');
    }

    const repo = await this.getRepository();
    
    if (!repo) {
      // Fallback to command line
      this.useCommandLine = true;
      return await this.getStagedDiff();
    }
    
    return new Promise((resolve, reject) => {
      repo.diff(true).then((diff: string) => {
        resolve(diff);
      }, (error: any) => {
        // Fallback to command line on error
        this.useCommandLine = true;
        this.getStagedDiff().then(resolve).catch(reject);
      });
    });
  }

  async getChanges(): Promise<GitFileChange[]> {
    try {
      const output = await this.execGit('diff --cached --name-status');
      const changes: GitFileChange[] = [];
      
      const lines = output.split('\n');
      for (const line of lines) {
        if (!line.trim()) continue;
        
        const parts = line.split('\t');
        if (parts.length >= 2) {
          changes.push({
            path: parts[1],
            status: parts[0]
          });
        }
      }
      
      return changes;
    } catch (error) {
      return [];
    }
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
    if (this.useCommandLine) {
      await this.execGit(`commit -m ${JSON.stringify(message)}`);
      return;
    }

    const repo = await this.getRepository();
    
    if (!repo) {
      // Fallback to command line
      this.useCommandLine = true;
      await this.commit(message);
      return;
    }
    
    try {
      await repo.commit(message);
    } catch (error) {
      // Fallback to command line on error
      this.useCommandLine = true;
      await this.commit(message);
    }
  }

  async hasStagedChanges(): Promise<boolean> {
    try {
      const output = await this.execGit('diff --cached');
      return output.trim().length > 0;
    } catch (error) {
      return false;
    }
  }
}
