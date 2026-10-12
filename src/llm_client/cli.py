import sys

from typing import List, Tuple
from src.llm_client.config import config
from src.llm_client.logging_setup import logger
from src.llm_client.client import Client
from src.llm_client.models import ModelResponse, Answer


def parse_args(args: List[str]) -> Tuple[bool, str]:
    """Parse command line arguments"""
    verbose = False
    request = None

    for arg in args[1:]:
        if arg == "--verbose":
            verbose = True
        if not arg.startswith('--') and request is None:
            request = arg

    if request is None:
        raise Exception('No request argument. Please keep format "python -m src.llm_client.cli "User request"')
    if request == '':
        raise Exception("Empty request")
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

    if verbose:
        answer = ModelResponse(
            response=result['response'].choices[0].message.content,
            model=result['response'].model,
            input_tokens=result['response'].usage.prompt_tokens,
            output_tokens=result['response'].usage.completion_tokens,
            duration_ms=result['duration'],
            request_id=result['response'].id,
        ).model_dump()
    else:
        answer = result['response'].choices[0].message.content

    print(answer)


if __name__ == "__main__":
    main(sys.argv)
