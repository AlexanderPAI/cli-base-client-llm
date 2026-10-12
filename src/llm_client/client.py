from datetime import datetime
from typing import Dict

from openrouter import OpenRouter
from openrouter.components import ChatResult

from src.llm_client.config import config
from src.llm_client.models import Answer


class Client:

    def __init__(self, model: OpenRouter = None, model_ref: str = None) -> None:
        self.model = model if model is not None else OpenRouter(
            api_key=config.llm_api_key,
            timeout_ms=config.llm_timeout_seconds * 1000
        )
        self.model_ref = model_ref if model_ref is not None else config.llm_model

    def generate(
            self,
            system_prompt: Dict[str, str],
            user_prompt: Dict[str, str],
    ) -> Dict[str, ChatResult | int]:
        """Generate the chat."""
        start = datetime.now()
        with self.model:
            response = self.model.chat.send(
                model=self.model_ref,
                messages=[system_prompt, user_prompt],
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "answer",
                        "strict": True,
                        "schema": Answer.model_json_schema()
                    }
                }
            )
        end = datetime.now()
        duration = end - start

        return {
            "response": response,
            "duration": round(duration.total_seconds() * 1000),
        }
