import logging
import os

# The root of the data-extractors project.
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

# Path to the chromedriver executable for the cobertura-vacinal extractor.
CHROME_DRIVER_PATH = os.path.join(
    PROJECT_ROOT, "cobertura-vacinal", "chromedriver", "chromedriver"
)

# The directory where downloaded data from cobertura-vacinal is stored.
DOWNLOAD_PATH = os.path.join(PROJECT_ROOT, "cobertura-vacinal", "data")

# ANSI escape sequences
RESET = "\033[0m"
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"


class ColorFormatter(logging.Formatter):
    def format(self, record):
        if record.levelno == logging.ERROR:
            record.levelname = f"{RED}[{record.levelname}]{RESET}"
        elif record.levelno == logging.WARNING:
            record.levelname = f"{YELLOW}[{record.levelname}]{RESET}"
        elif record.levelno == logging.INFO:
            record.levelname = f"{GREEN}[{record.levelname}]{RESET}"
        return super().format(record)
