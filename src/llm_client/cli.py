from src.llm_client.config import config
from src.llm_client.logging_setup import logger
from src.llm_client.client import Client
from src.llm_client.models import model

if __name__ == "__main__":

    request = "Объясни понятие API тремя короткими предложениями."

    client = Client(
        model=model,
        model_ref=config.llm_model,
    )

    print(client.chat(request))
