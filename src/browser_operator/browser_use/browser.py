import platform
from contextlib import asynccontextmanager

from browser_use import Browser, BrowserConfig, BrowserContextConfig
from browser_use.browser.context import BrowserContext


@asynccontextmanager
async def browser_manager(initiate_session: bool):
    config = BrowserConfig(
        chrome_instance_path=__chrome_instance_path(initiate_session=initiate_session),
    )
    browser = Browser(config=config)

    try:
        yield browser
    finally:
        await browser.close()


def get_browser_context(
    browser: Browser,
    allowed_domains: list[str] | None = None,
    save_recording_path: str | None = None,
) -> BrowserContext:
    config = BrowserContextConfig(
        allowed_domains=allowed_domains,
        save_recording_path=save_recording_path,
    )

    return BrowserContext(browser=browser, config=config)


def __chrome_instance_path(initiate_session: bool = True) -> str | None:
    if initiate_session:
        return None

    system = platform.system()
    match system:
        case "Windows":
            return r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        case "Linux":
            return "/usr/bin/google-chrome"
        case "Darwin":
            return "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        case _:
            raise ValueError(f"Unsupported system: {system}")
