import sys

from typing import List, Tuple
from src.llm_client.config import config
from src.llm_client.logging_setup import logger
from src.llm_client.client import Client


def parse_args(args: List[str]) -> Tuple[bool, str]:
    verbose = False
    request = None

    for arg in args[1:]:
        if arg == "--verbose":
            verbose = True
        if not arg.startswith('--') and request is None:
            request = arg

    if request is None:
        raise Exception('No request argument. Please keep format "python -m src.llm_client.cli "User request""')
    return verbose, request


def main(sys_args: List[str]) -> None:
    verbose, request = parse_args(sys_args)

    user_prompt = {
        "role": "user",
        "content": request,
    }

    system_prompt = {
        "role": "system",
        "content": "Ты умный помощник по программированию на Python",
    }

    client = Client()

    result = client.generate(system_prompt, user_prompt)
    answer = result['response'].choices[0].message.content

    print(answer)


if __name__ == "__main__":
    main(sys.argv)
