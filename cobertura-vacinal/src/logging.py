import os
import logging
from src.utils.constants import LOGS_PATH, ColorFormatter


def setup_looging():

    log_dir = os.path.join(LOGS_PATH, "logs")
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Console handler
    console = logging.StreamHandler()
    console.setFormatter(ColorFormatter("%(asctime)s %(levelname)s - %(message)s"))

    # File handler
    file_handler = logging.FileHandler(
        os.path.join(log_dir, "cobertura-vacinal.txt")
    )
    file_handler.setLevel(logging.INFO)

    # Formatters
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] - %(message)s")

    file_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(console)
    logger.addHandler(file_handler)
    return logger


logger = setup_looging()
