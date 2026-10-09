from openrouter import OpenRouter

from src.llm_client.config import config

model = OpenRouter(
    api_key=config.llm_api_key,
    timeout_ms=config.llm_timeout_seconds * 1000,
)
