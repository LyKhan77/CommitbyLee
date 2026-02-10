import * as vscode from 'vscode';
import { OllamaClient } from '../client/ollama';
import { ConfigManager } from '../config/schema';

export async function testConnection() {
  const outputChannel = vscode.window.createOutputChannel('Commit by Lee - Connection Test');
  
  try {
    outputChannel.appendLine('============================================================');
    outputChannel.appendLine('Testing Ollama Connection');
    outputChannel.appendLine('============================================================');
    outputChannel.appendLine('');
    
    const config = ConfigManager.getConfig();
    const ollamaClient = new OllamaClient(config.ollama.host);
    
    outputChannel.appendLine(`Host: ${config.ollama.host}`);
    outputChannel.appendLine(`Model: ${config.ollama.model}`);
    outputChannel.appendLine('');
    
    outputChannel.appendLine('Testing connection...');
    
    const isConnected = await ollamaClient.checkConnection();
    
    if (isConnected) {
      outputChannel.appendLine('[OK] Connection successful!');
      outputChannel.appendLine('');
      
      const models = await ollamaClient.listModels();
      outputChannel.appendLine(`Found ${models.length} model(s):`);
      for (const model of models) {
        const sizeMB = (model.size / 1024 / 1024).toFixed(1);
        outputChannel.appendLine(`  • ${model.name} (${sizeMB} MB)`);
      }
      
      vscode.window.showInformationMessage('✓ Successfully connected to Ollama server!');
    } else {
      outputChannel.appendLine('[ERROR] Connection failed!');
      outputChannel.appendLine('');
      outputChannel.appendLine('Possible solutions:');
      outputChannel.appendLine('1. Check if Ollama server is running');
      outputChannel.appendLine('2. Verify the host URL in settings');
      outputChannel.appendLine('3. Check your internet connection');
      
      vscode.window.showErrorMessage('Failed to connect to Ollama server');
    }
    
    outputChannel.show(true);
    
  } catch (error: any) {
    outputChannel.appendLine(`[ERROR] ${error.message}`);
    outputChannel.show(true);
    vscode.window.showErrorMessage(`Error: ${error.message}`);
  }
}
