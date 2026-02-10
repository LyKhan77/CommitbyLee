import * as vscode from 'vscode';
import { ConfigManager } from '../config/schema';

export function openConfig() {
  ConfigManager.openSettings();
}
