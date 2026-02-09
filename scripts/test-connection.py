#!/usr/bin/env python3
"""
Test connection to Ollama server

This script tests the connection to the Ollama server and verifies
that Qwen3:4B model is available.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "core"))

from commit_by_lee.ollama_client import OllamaClient
from commit_by_lee.config import Config


def test_connection():
    """Test connection to Ollama server"""
    try:
        print("=" * 60)
        print("Testing Ollama Connection")
        print("=" * 60)
        print()

        # Load config
        config = Config()
        print(f"Host: {config.config.ollama_host}")
        print(f"Model: {config.config.ollama_model}")
        print()

        # Initialize client
        client = OllamaClient(
            host=config.config.ollama_host,
            model=config.config.ollama_model
        )

        # Test connection
        print("Testing connection...")
        if client.check_connection():
            print("[OK] Connection successful!")
            print()

            # List available models
            models = client.list_models()
            if models:
                print(f"Found {len(models)} model(s):")
                for model in models:
                    name = model.get('name', 'unknown')
                    size = model.get('size', 0)
                    size_mb = size / (1024 * 1024) if size else 0
                    print(f"  • {name} ({size_mb:.1f} MB)")
                print()

            # Test generation
            print("Testing commit message generation...")
            test_diff = """
+ function hello() {
+   return "Hello, World!";
+ }
"""

            prompt = f"""Generate a commit message for this diff:

{test_diff}

Respond only with the commit message in Conventional Commits format."""

            response = client.generate(prompt)
            print(f"Generated: {response}")
            print()

            return 0
        else:
            print("[ERROR] Connection failed!")
            print()
            print("Troubleshooting:")
            print("1. Check if Ollama server is running")
            print(f"2. Verify the host: {config.config.ollama_host}")
            print(f"3. Ensure Qwen3:4B model is pulled on the server")
            return 1

    except Exception as e:
        print(f"[ERROR] Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(test_connection())
