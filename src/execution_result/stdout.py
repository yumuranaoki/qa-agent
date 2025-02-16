import textwrap

from execution_result.execution_result import ExecutionResult
from logger import logger


def write(execution_result: ExecutionResult):
    content = textwrap.dedent(f"""
            📄 Execution Result by QA Agent
            is_success: {execution_result.is_success}
            usability_feedback: {execution_result.usability_feedback}
        """)
    logger.info(content)
