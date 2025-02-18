from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

from logger import logger

load_dotenv()


ALLOWED_PROVIDERS = {
    "openai": ["gpt-4o", "gpt-4o-mini"],
    "gemini": ["gemini-1.5-flash", "gemini-2.0-flash"],
}


def initialize_model(provider: str, model: str):
    if provider not in ALLOWED_PROVIDERS:
        logger.error(f"Specified provider is not allowed: {provider}")
        raise ValueError(f"Allowed providers: {ALLOWED_PROVIDERS.keys()}")

    if model not in ALLOWED_PROVIDERS[provider]:
        logger.error(f"Specified model is not allowed: {model}")
        raise ValueError(
            f"Allowed models for {provider}: {ALLOWED_PROVIDERS[provider]}"
        )

    return __get_llm(provider, model)


def __get_llm(provider: str, model: str):
    match provider:
        case "openai":
            return ChatOpenAI(model=model)
        case "gemini":
            return ChatGoogleGenerativeAI(model=model)
        case _:
            raise ValueError(f"Unexpected provider: {provider}")
