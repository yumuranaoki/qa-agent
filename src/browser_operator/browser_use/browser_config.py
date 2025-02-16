from browser_use import Browser, BrowserContextConfig
from browser_use.browser.context import BrowserContext


def get_browser_context(
    allowed_domains: list[str] | None = None,
    save_recording_path: str | None = "logs",
) -> BrowserContext:
    browser = Browser()

    config = BrowserContextConfig(
        allowed_domains=allowed_domains,
        save_recording_path=save_recording_path,
    )

    return BrowserContext(browser=browser, config=config)
