from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, Field


class Config(BaseSettings):
    """Configuration settings for LLM client"""
    llm_api_key: str = Field(..., env="LLM_API_KEY", description="OpenRouter API key")
    llm_model: str = Field(..., env="LLM_MODEL", description="OpenRouter model name")
    llm_timeout_seconds: int = Field(..., env="LLM_TIMEOUT_SECONDS", description="OpenRouter API timeout")
    llm_max_retries: int = Field(..., env="LLM_MAX_RETRIES", description="OpenRouter API retries")

    model_config = SettingsConfigDict(
        env_file=".env",
    )

config = Config()
