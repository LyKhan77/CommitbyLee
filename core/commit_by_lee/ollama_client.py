"""Ollama API client for Qwen3:4B integration"""

import requests
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)


class OllamaClient:
    """
    Ollama API Client for Qwen3:4B model

    Handles communication with remote Ollama server
    """

    def __init__(
        self,
        host: str = "https://ollama.iotech.my.id",
        model: str = "qwen3:4b",
        timeout: int = 30
    ):
        """
        Initialize Ollama client

        Args:
            host: Ollama server URL
            model: Model name (default: qwen3:4b)
            timeout: Request timeout in seconds
        """
        self.host = host.rstrip("/")
        self.model = model
        self.timeout = timeout
        self.api_base = f"{self.host}/api"

    def generate(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 500,
        **kwargs
    ) -> str:
        """
        Generate commit message from diff using Qwen3:4B

        Args:
            prompt: Input prompt with git diff
            temperature: Sampling temperature (0.0 - 1.0)
            max_tokens: Maximum tokens to generate
            **kwargs: Additional parameters

        Returns:
            Generated commit message

        Raises:
            requests.RequestException: If API request fails
        """
        url = f"{self.api_base}/generate"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens,
                "num_ctx": 4096,  # Context window
                "top_k": 20,
                "top_p": 0.9,
                "repeat_penalty": 1.1,
            }
        }

        try:
            logger.info(f"Sending request to {url} with model {self.model}")
            logger.debug(f"Prompt length: {len(prompt)} characters")
            logger.debug(f"Prompt preview (first 200 chars): {prompt[:200]}...")

            response = requests.post(
                url,
                json=payload,
                timeout=self.timeout
            )
            response.raise_for_status()

            result = response.json()
            generated_text = result.get("response", "")

            # If response is empty but thinking exists, try to extract from thinking
            if not generated_text and result.get("thinking"):
                logger.warning("Response is empty, but thinking field exists")
                logger.debug(f"Thinking preview: {result.get('thinking')[:300]}...")
                logger.debug(f"Done reason: {result.get('done_reason')}")
                logger.debug(f"Eval count: {result.get('eval_count')}")
                # The model thought about it but didn't output - try again with different params
                # For now, return empty and let the generator handle fallback
                pass

            logger.info(f"Generated {len(generated_text)} characters")

            if not generated_text:
                logger.warning("Empty response from Ollama")
                logger.debug(f"Full response keys: {result.keys()}")
                logger.debug(f"Response field: '{result.get('response')}'")
                logger.debug(f"Done: {result.get('done')}")
                logger.debug(f"Done reason: {result.get('done_reason')}")

            return generated_text.strip()

        except requests.exceptions.Timeout:
            logger.error(f"Request timeout after {self.timeout}s")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise

    def check_connection(self) -> bool:
        """
        Test connection to Ollama server and verify Qwen3:4B availability

        Returns:
            True if connection successful and Qwen3:4B is available
        """
        try:
            url = f"{self.api_base}/tags"
            logger.info(f"Checking connection to {url}")

            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()
            models = data.get("models", [])

            # Check if qwen3:4b is available
            model_names = [m.get("name", "") for m in models]
            qwen_available = any("qwen3:4b" in name for name in model_names)

            if qwen_available:
                logger.info("[OK] Connection successful! Qwen3:4B is available")
            else:
                logger.warning(f"[OK] Connected but Qwen3:4B not found. Available models: {model_names}")

            return qwen_available

        except requests.exceptions.RequestException as e:
            logger.error(f"[X] Connection failed: {e}")
            return False
        except Exception as e:
            logger.error(f"[X] Unexpected error: {e}")
            return False

    def list_models(self) -> list:
        """
        List all available models on the server

        Returns:
            List of model dictionaries
        """
        try:
            url = f"{self.api_base}/tags"
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()
            return data.get("models", [])

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to list models: {e}")
            return []
