import logging

from src.llm_client.config import config
from src.llm_client.logging_setup import logger


if __name__ == "__main__":
    logger.info("Starting application")
    logger.debug("Check configuration")
    logger.debug(config.llm_model)
