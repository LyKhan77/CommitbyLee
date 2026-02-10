import * as vscode from 'vscode';
import { generateCommit } from './commands/generateCommit';
import { testConnection } from './commands/testConnection';
import { openConfig } from './commands/openConfig';

export function activate(context: vscode.ExtensionContext) {
  console.log('Commit by Lee extension is now active!');
  
  const generateCommand = vscode.commands.registerCommand(
    'commitbylee.generate',
    () => generateCommit(context)
  );
  
  const testConnectionCommand = vscode.commands.registerCommand(
    'commitbylee.testConnection',
    testConnection
  );
  
  const openConfigCommand = vscode.commands.registerCommand(
    'commitbylee.openConfig',
    openConfig
  );
  
  context.subscriptions.push(
    generateCommand,
    testConnectionCommand,
    openConfigCommand
  );
  
  vscode.window.showInformationMessage('Commit by Lee extension activated! Press Ctrl+Shift+G to generate commit messages.');
}

export function deactivate() {
  console.log('Commit by Lee extension is now deactivated.');
}
