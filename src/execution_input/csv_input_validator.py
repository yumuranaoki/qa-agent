import csv
import sys

from execution_input.execution_input import ExecutionInput
from logger import logger


def validate_input(uri):
    try:
        with open(uri, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            return [ExecutionInput.model_validate(row) for row in reader]
    except Exception as e:
        logger.error(f"Unexpected error parsing csv files: {e}")
        sys.exit(1)
