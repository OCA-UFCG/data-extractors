import logging
import os
from dotenv import load_dotenv
load_dotenv()


LOGS_PATH = os.getenv("LOGS_PATH")

# The directory where downloaded data from cobertura-vacinal is stored.
DOWNLOAD_PATH = os.getenv("DOWNLOAD_PATH")

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
