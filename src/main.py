import argparse
import asyncio
import sys

from browser_operator.browser_use.agent import execute
from execution_input.csv_input_validator import validate_input
from execution_result.stdout import write
from llm import initialize_model
from logger import logger


async def __run(
    uri: str,
    provider: str,
    model: str,
    allowed_domains: list[str],
    initial_url: str | None,
    language: str,
):
    llm = initialize_model(provider=provider, model=model)
    execution_inputs = validate_input(uri=uri)

    for input in execution_inputs:
        try:
            execution_result = await execute(
                llm=llm,
                input=input,
                allowed_domains=allowed_domains,
                initial_url=initial_url,
                language=language,
            )
            write(execution_result)
        except Exception as e:
            logger.error(f"Error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="QA Agent execution script")
    parser.add_argument("--uri", required=True, help="Input URI")
    parser.add_argument("--provider", required=True, help="Provider name")
    parser.add_argument("--model", required=True, help="Model name")
    parser.add_argument(
        "--allowed-domains", nargs="+", default=None, help="List of allowed domains"
    )
    parser.add_argument("--initial-url", help="Initial URL", default=None)
    parser.add_argument(
        "--language",
        help="Feedback language",
        choices=["en", "ja"],
        default="en",
    )
    args = parser.parse_args()

    asyncio.run(
        __run(
            uri=args.uri,
            provider=args.provider,
            model=args.model,
            allowed_domains=args.allowed_domains,
            initial_url=args.initial_url,
            language=args.language,
        )
    )
