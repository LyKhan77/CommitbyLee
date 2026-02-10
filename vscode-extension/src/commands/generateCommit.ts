import * as vscode from 'vscode';
import { OllamaClient } from '../client/ollama';
import { GitClient } from '../client/git';
import { ConfigManager } from '../config/schema';
import { CommitMessageFormatter } from '../utils/commitMessageFormatter';
import { PromptGenerator } from '../utils/promptGenerator';
import { CommitPreviewPanel } from '../../webview/commitPreview';

export async function generateCommit(context: vscode.ExtensionContext) {
  const outputChannel = vscode.window.createOutputChannel('Commit by Lee');
  
  try {
    outputChannel.appendLine('🤖 Commit by Lee');
    outputChannel.appendLine('');
    
    const config = ConfigManager.getConfig();
    const gitClient = new GitClient();
    const ollamaClient = new OllamaClient(config.ollama.host);
    
    outputChannel.appendLine('🔌 Checking staged changes...');
    
    const diff = await gitClient.getStagedDiff();
    if (!diff || diff.trim().length === 0) {
      vscode.window.showWarningMessage('No staged changes found. Please stage your changes first using git add.');
      return;
    }
    
    const stats = await gitClient.getDiffStats();
    outputChannel.appendLine(`✓ Found ${stats.filesChanged} file(s) changed`);
    outputChannel.appendLine(`  +${stats.insertions} -${stats.deletions}`);
    outputChannel.appendLine('');
    
    outputChannel.appendLine('🧠 Generating commit message...');
    outputChannel.show(true);
    
    const prompt = PromptGenerator.generateCommitPrompt(diff, stats, config.app.language);
    const response = await ollamaClient.generate(config.ollama.model, prompt);
    
    const commitMessage = CommitMessageFormatter.parseCommitMessage(response);
    
    outputChannel.appendLine('✓ Commit message generated!');
    outputChannel.appendLine('');
    outputChannel.appendLine('Generated message:');
    outputChannel.appendLine('---');
    outputChannel.appendLine(response);
    outputChannel.appendLine('---');
    
    if (config.app.autoCommit) {
      const formattedMessage = CommitMessageFormatter.formatConventional(commitMessage);
      await gitClient.commit(formattedMessage);
      vscode.window.showInformationMessage('✓ Commit created successfully!');
      outputChannel.appendLine('✓ Commit created!');
    } else {
      const extensionUri = context.extensionUri;
      CommitPreviewPanel.show(
        extensionUri,
        commitMessage,
        config.app.style,
        async (message: string) => {
          try {
            await gitClient.commit(message);
            vscode.window.showInformationMessage('✓ Commit created successfully!');
            outputChannel.appendLine('✓ Commit created!');
          } catch (error) {
            vscode.window.showErrorMessage(`Failed to create commit: ${error}`);
          }
        },
        async (message: string) => {
          const edited = await vscode.window.showInputBox({
            value: message,
            prompt: 'Edit commit message',
            placeHolder: 'Enter commit message'
          });
          
          if (edited) {
            try {
              await gitClient.commit(edited);
              vscode.window.showInformationMessage('✓ Commit created successfully!');
              outputChannel.appendLine('✓ Commit created!');
            } catch (error) {
              vscode.window.showErrorMessage(`Failed to create commit: ${error}`);
            }
          }
        }
      );
    }
    
  } catch (error: any) {
    vscode.window.showErrorMessage(`Error: ${error.message}`);
    outputChannel.appendLine(`✗ Error: ${error.message}`);
  }
}
