from openrouter import OpenRouter
from openrouter.components import ChatResult


class Client:

    def __init__(self, model: OpenRouter, model_ref: str) -> None:
        self.model = model
        self.model_ref = model_ref


    def chat(self, message: str) -> ChatResult:
        with self.model:
            return self.model.chat.send(
                model=self.model_ref,
                messages=[
                    {
                        "role": "user",
                        "content": message,
                    }
                ],
            )
