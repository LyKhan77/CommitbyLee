export interface OllamaConfig {
  host: string;
  model: string;
  temperature: number;
}

export interface AppConfig {
  language: 'id' | 'en';
  style: 'conventional' | 'emoji' | 'simple';
  autoCommit: boolean;
}

export interface Config {
  ollama: OllamaConfig;
  app: AppConfig;
}

export interface GitDiffStats {
  filesChanged: number;
  insertions: number;
  deletions: number;
}

export interface GitFileChange {
  path: string;
  status: string;
}

export interface CommitMessage {
  type: string;
  scope?: string;
  subject: string;
  body?: string;
}

export interface OllamaModel {
  name: string;
  size: number;
}

export interface OllamaGenerateResponse {
  model: string;
  response: string;
  done: boolean;
}
