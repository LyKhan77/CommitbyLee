import * as vscode from 'vscode';
import { Config } from '../types';

export interface ConfigOptions {
  ollamaHost: string;
  ollamaModel: string;
  temperature: number;
  language: 'id' | 'en';
  style: 'conventional' | 'emoji' | 'simple';
  autoCommit: boolean;
}

export class ConfigManager {
  private static readonly CONFIG_SECTION = 'commitbylee';

  static getConfig(): Config {
    const config = vscode.workspace.getConfiguration(this.CONFIG_SECTION);
    
    return {
      ollama: {
        host: config.get<string>('ollamaHost', 'http://localhost:11434'),
        model: config.get<string>('ollamaModel', 'qwen3:4b'),
        temperature: config.get<number>('temperature', 0.7)
      },
      app: {
        language: config.get<'id' | 'en'>('language', 'id'),
        style: config.get<'conventional' | 'emoji' | 'simple'>('style', 'conventional'),
        autoCommit: config.get<boolean>('autoCommit', false)
      }
    };
  }

  static async updateConfig(key: string, value: any): Promise<void> {
    const config = vscode.workspace.getConfiguration(this.CONFIG_SECTION);
    await config.update(key, value, vscode.ConfigurationTarget.Global);
  }

  static openSettings(): void {
    vscode.commands.executeCommand('workbench.action.openSettings', `@ext:${this.CONFIG_SECTION}`);
  }
}
