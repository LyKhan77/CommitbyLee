import * as vscode from 'vscode';
import { CommitMessage } from '../src/types';
import { CommitMessageFormatter } from '../src/utils/commitMessageFormatter';

export class CommitPreviewPanel {
  private static currentPanel: CommitPreviewPanel | undefined;
  private readonly panel: vscode.WebviewPanel;
  private disposables: vscode.Disposable[] = [];

  private constructor(
    panel: vscode.WebviewPanel,
    private readonly commitMessage: CommitMessage,
    private readonly style: 'conventional' | 'emoji' | 'simple',
    private readonly onAccept: (message: string) => void,
    private readonly onEdit: (message: string) => void
  ) {
    this.panel = panel;
    this.panel.onDidDispose(() => this.dispose(), null, this.disposables);
    this.panel.webview.onDidReceiveMessage(
      message => {
        switch (message.command) {
          case 'accept':
            this.onAccept(this.getFormattedMessage());
            return;
          case 'edit':
            this.onEdit(this.getFormattedMessage());
            return;
          case 'cancel':
            this.panel.dispose();
            return;
        }
      },
      null,
      this.disposables
    );
    this.update();
  }

  public static show(
    extensionUri: vscode.Uri,
    commitMessage: CommitMessage,
    style: 'conventional' | 'emoji' | 'simple',
    onAccept: (message: string) => void,
    onEdit: (message: string) => void
  ) {
    const column = vscode.window.activeTextEditor
      ? vscode.window.activeTextEditor.viewColumn
      : undefined;

    if (CommitPreviewPanel.currentPanel) {
      CommitPreviewPanel.currentPanel.panel.reveal(column);
      return;
    }

    const panel = vscode.window.createWebviewPanel(
      'commitbylee.preview',
      'Commit Message Preview',
      column || vscode.ViewColumn.One,
      {
        enableScripts: true,
        localResourceRoots: [extensionUri]
      }
    );

    CommitPreviewPanel.currentPanel = new CommitPreviewPanel(
      panel,
      commitMessage,
      style,
      onAccept,
      onEdit
    );
  }

  private getFormattedMessage(): string {
    switch (this.style) {
      case 'conventional':
        return CommitMessageFormatter.formatConventional(this.commitMessage);
      case 'emoji':
        return CommitMessageFormatter.formatEmoji(this.commitMessage);
      case 'simple':
        return CommitMessageFormatter.formatSimple(this.commitMessage);
    }
  }

  private update() {
    const webview = this.panel.webview;
    const message = this.getFormattedMessage();

    webview.html = this.getHtmlContent(message);
  }

  private getHtmlContent(message: string): string {
    return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Commit Message Preview</title>
  <style>
    body {
      font-family: var(--vscode-font-family);
      font-size: var(--vscode-font-size);
      font-weight: var(--vscode-font-weight);
      color: var(--vscode-foreground);
      background-color: var(--vscode-editor-background);
      padding: 20px;
    }
    .container {
      max-width: 800px;
      margin: 0 auto;
    }
    h1 {
      color: var(--vscode-textLink-foreground);
      margin-bottom: 20px;
    }
    .message-box {
      background-color: var(--vscode-editor-selectionBackground);
      border: 1px solid var(--vscode-panel-border);
      border-radius: 4px;
      padding: 16px;
      margin-bottom: 20px;
      white-space: pre-wrap;
      word-wrap: break-word;
      font-family: var(--vscode-editor-font-family);
      font-size: var(--vscode-editor-font-size);
      line-height: 1.5;
    }
    .buttons {
      display: flex;
      gap: 10px;
    }
    button {
      padding: 8px 16px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 14px;
      font-weight: 500;
    }
    .accept {
      background-color: var(--vscode-button-background);
      color: var(--vscode-button-foreground);
    }
    .accept:hover {
      background-color: var(--vscode-button-hoverBackground);
    }
    .edit {
      background-color: var(--vscode-button-secondaryBackground);
      color: var(--vscode-button-secondaryForeground);
    }
    .edit:hover {
      background-color: var(--vscode-button-secondaryHoverBackground);
    }
    .cancel {
      background-color: var(--vscode-errorBackground);
      color: var(--vscode-errorForeground);
    }
    .cancel:hover {
      background-color: var(--vscode-button-hoverBackground);
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>🤖 Commit Message Preview</h1>
    <div class="message-box">${this.escapeHtml(message)}</div>
    <div class="buttons">
      <button class="accept" onclick="postMessage('accept')">✓ Accept</button>
      <button class="edit" onclick="postMessage('edit')">✎ Edit</button>
      <button class="cancel" onclick="postMessage('cancel')">✗ Cancel</button>
    </div>
  </div>
  <script>
    const vscode = acquireVsCodeApi();
    function postMessage(command) {
      vscode.postMessage({ command });
    }
  </script>
</body>
</html>`;
  }

  private escapeHtml(text: string): string {
    const map: { [key: string]: string } = {
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
  }

  public dispose() {
    CommitPreviewPanel.currentPanel = undefined;
    this.panel.dispose();
    while (this.disposables.length) {
      const disposable = this.disposables.pop();
      if (disposable) {
        disposable.dispose();
      }
    }
  }
}
