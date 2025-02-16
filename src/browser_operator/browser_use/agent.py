import textwrap

from browser_use import Agent, Controller
from langchain_core.language_models.chat_models import BaseChatModel

from execution_input.execution_input import ExecutionInput
from execution_result.execution_result import ExecutionResult

from .browser_config import get_browser_context


async def execute(
    llm: BaseChatModel,
    input: ExecutionInput,
    initial_url: str | None = None,
    allowed_domains: list[str] | None = None,
    language: str = "en",
):
    if initial_url:
        initial_actions = [{"open_tab": {"url": initial_url}}]
    else:
        initial_actions = []

    browser_context = get_browser_context(allowed_domains=allowed_domains)

    agent = Agent(
        task=textwrap.dedent(f"""
            Please follow the preparation and execution steps in order, then verify whether the expected result has been achieved.
            If you have any usability-related feedback during the process, please provide it in {language}.

            [Preparation]
            {input.preparation}

            [Execution Steps]
            {input.steps}

            [Expected Result]
            {input.expected_result}
        """),
        llm=llm,
        browser_context=browser_context,
        initial_actions=initial_actions,
        controller=Controller(output_model=ExecutionResult),
        max_actions_per_step=5,
        max_failures=5,
    )
    history = await agent.run()
    result = history.final_result()
    return ExecutionResult.model_validate_json(result)
