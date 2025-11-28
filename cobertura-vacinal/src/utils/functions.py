import os
import time
import requests
from selenium.webdriver.common.by import By
from src.utils.constants import DOWNLOAD_PATH
from src.logging import logger


def wait_for_selenium():
    while True:
        try:
            res = requests.get("http://chromeNode:4444/wd/hub/status")
            if res.status_code == 200 and res.json()["value"]["ready"] == True:
                logger.info("Selenium is ready!")
                return
        except:
            pass
        logger.info("Waiting for Selenium...")
        time.sleep(1)


def save_file(name: str, year: str):
    logger.info(f"Checking for new files in {DOWNLOAD_PATH}")
    files_before = set(os.listdir(DOWNLOAD_PATH))

    # Wait for download to start by detecting a new file
    temp_file_path = None
    final_file_path = None

    for _ in range(15):  # wait up to 15 seconds for download to start
        files_after = set(os.listdir(DOWNLOAD_PATH))
        new_files = files_after - files_before
        if new_files:
            filename = new_files.pop()
            path = os.path.join(DOWNLOAD_PATH, filename)
            if filename.endswith(".crdownload"):
                logger.info("Download started, temporary file found.")
                temp_file_path = path
                break
            else:
                logger.info("Download started and finished quickly.")
                final_file_path = path
                break
        time.sleep(2)

    if temp_file_path:
        # Now wait for the .crdownload file to be removed (i.e., download is complete)
        for _ in range(30):  # wait up to 30 more seconds
            time.sleep(1)
            if not os.path.exists(temp_file_path):
                # Temp file is gone, so the real file should be there.
                final_filename = os.path.basename(temp_file_path).replace(
                    ".crdownload", ""
                )
                path = os.path.join(DOWNLOAD_PATH, final_filename)
                # It can take a moment for the final file to be available
                for __ in range(5):
                    if os.path.exists(path):
                        logger.info("Download completed.")
                        final_file_path = path
                        break
                    time.sleep(1)
                if final_file_path:
                    break

    if final_file_path:
        downloaded_filename = os.path.basename(final_file_path)

        # Sanitize name for filename
        sanitized_name = (
            "".join(c for c in name if c.isalnum() or c in (" ", "-"))
            .rstrip()
            .replace(" ", "_")
        )
        new_filename = f"{year}-{sanitized_name}.xlsx"
        new_filepath = os.path.join(DOWNLOAD_PATH, new_filename)

        # Ensure the old file exists before trying to rename
        if os.path.exists(final_file_path):

            # If a file with the new name already exists, remove it
            if os.path.exists(new_filepath):
                logger.warning(f"File {new_filename} already exists. Overwriting.")
                os.remove(new_filepath)
            os.rename(final_file_path, new_filepath)
            logger.info(f"Renamed '{downloaded_filename}' to '{new_filename}'")
        else:
            logger.error(
                f"Downloaded file '{downloaded_filename}' not found for renaming."
            )
    else:
        logger.warning(
            f"Download did not start or complete in time for vaccine: {name}"
        )
