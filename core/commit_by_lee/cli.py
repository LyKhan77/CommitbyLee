"""CLI commands for Commit by Lee"""

import click
import logging
import time
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm
from rich.syntax import Syntax
from rich.text import Text

from .ollama_client import OllamaClient
from .diff_analyzer import DiffAnalyzer
from .llm_generator import CommitMessageGenerator
from .config import Config
from .formatters import format_commit_message
from .models.schemas import Language, CommitStyle
from .utils import clean_diff

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)
logger = logging.getLogger(__name__)

# Rich console
console = Console()

# ASCII Art Banner (ASCII-only for Windows compatibility)
BANNER = """
 ::::::::  ::::::    ::    ::    :::::: :::::
::     ::::  ::  ::::  :::::: ::    ::
::::: ::::   ::  ::::  ::::  ::::   :::::
                                         
::::: :::: ::   ::     ::::::: :::::::
::  :::: ::   ::     ::  ::  ::::
::   ::: ::     :::::: ::  :::: ::::
"""


@click.group()
@click.version_option(version='0.1.0', prog_name='commit-by-lee')
def cli():
    """Commit by Lee - AI-powered Git Commit Message Generator
    
    Generate better commit messages using Ollama and Qwen3:4B model.
    """
    pass


@cli.command()
@click.option('--language', '-l', type=click.Choice(['en', 'id']), default='en',
              help='Output language (en=id, id=Indonesian)')
@click.option('--style', '-s', type=click.Choice(['conventional', 'simple', 'emoji']), default='conventional',
              help='Commit message style')
@click.option('--max-files', type=int, default=5,
              help='Maximum number of files to include in analysis')
def generate(language, style, max_files):
    """Generate commit message from current git changes"""
    try:
        # Display banner
        console.print(Panel.fit(BANNER, style="bold blue"))
        console.print()
        
        # Load config
        config = Config()
        
        # Initialize clients
        ollama = OllamaClient(config.config.ollama_host)
        analyzer = DiffAnalyzer()
        generator = CommitMessageGenerator(ollama, config)
        
        # Get language enum
        lang = Language.INDONESIAN if language == 'id' else Language.ENGLISH
        commit_style = CommitStyle(style)
        
        # Display progress
        with console.status("[bold yellow]Analyzing changes...") as status:
            # Get git diff
            diff_result = analyzer.get_diff(max_files=max_files)
            
            if not diff_result['diff']:
                console.print("[yellow]No changes detected to commit.[/yellow]")
                return
            
            # Display analysis
            console.print(f"[green][OK][/green] Found {diff_result['stats']['files_changed']} file(s) changed")
            console.print(f"   [dim]+{diff_result['stats']['insertions']} -{diff_result['stats']['deletions']}[/dim]")
            console.print()
            
            # Generate commit message
            status.update("[bold yellow]Generating commit message...]")
            
            result = generator.generate(
                diff=diff_result['diff'],
                language=lang,
                style=commit_style
            )
        
        # Display result
        console.print(Panel(
            result.message,
            title="[bold green]Generated Commit Message[/bold green]",
            border_style="green"
        ))
        
        # Ask to apply
        if Confirm.ask("[bold yellow]Apply this commit message?[/bold yellow]", default=False):
            # Apply commit
            import subprocess
            subprocess.run(['git', 'commit', '-m', result.message], check=True)
            console.print("[green][OK] Commit created successfully![/green]")
        
    except Exception as e:
        console.print(f"[red][ERROR] {str(e)}[/red]")
        raise click.ClickException(str(e))


@cli.command()
def test_connection():
    """Test connection to Ollama server"""
    try:
        # Display banner
        console.print(Panel.fit(BANNER, style="bold blue"))
        console.print()
        
        console.print("[bold yellow]Testing Ollama connection...[/bold yellow]")
        
        config = Config()
        ollama = OllamaClient(config.config.ollama_host)
        
        # Test connection
        if ollama.check_connection():
            console.print(f"[green][OK] Connected to {config.config.ollama_host}[/green]")
            
            # List models
            models = ollama.list_models()
            console.print(f"[green][OK] Available models:[/green]")
            for model in models:
                console.print(f"   - [dim]{model}[/dim]")
        else:
            console.print(f"[red][ERROR] Cannot connect to {config.base_url}[/red]")
            raise click.ClickException("Connection failed")
            
    except Exception as e:
        console.print(f"[red][ERROR] {str(e)}[/red]")
        raise click.ClickException(str(e))


@cli.command()
@click.option('--base-url', help='Ollama base URL')
@click.option('--model', help='Ollama model name')
def config(base_url, model):
    """Manage configuration"""
    try:
        # Display banner
        console.print(Panel.fit(BANNER, style="bold blue"))
        console.print()
        
        cfg = Config()
        
        if base_url:
            cfg.update(ollama_host=base_url)
            console.print(f"[green][OK] Base URL set to: {base_url}[/green]")
        
        if model:
            cfg.update(ollama_model=model)
            console.print(f"[green][OK] Model set to: {model}[/green]")
        
        # Display current config
        console.print("[bold]Current Configuration:[/bold]")
        console.print(f"  Base URL: [dim]{cfg.config.ollama_host}[/dim]")
        console.print(f"  Model: [dim]{cfg.config.ollama_model}[/dim]")
        
    except Exception as e:
        console.print(f"[red][ERROR] {str(e)}[/red]")
        raise click.ClickException(str(e))


if __name__ == '__main__':
    cli()
