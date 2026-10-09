import logging

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("cli").setLevel(logging.WARNING)
logging.getLogger("client").setLevel(logging.WARNING)

logger = logging.getLogger("llm_client")
logger.setLevel(logging.DEBUG)
