import os
import time
from utils.constants import CHROME_DRIVER_PATH, DOWNLOAD_PATH
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


def setup():
    service = Service(executable_path=CHROME_DRIVER_PATH)

    options = webdriver.ChromeOptions()

    os.makedirs(DOWNLOAD_PATH, exist_ok=True)

    prefs = {
        "download.prompt_for_download": False,
        "download.default_directory": DOWNLOAD_PATH,
        "safebrowsing.enabled": True,
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options, service=service)

    driver.get(
        "https://infoms.saude.gov.br/extensions/SEIDIGI_DEMAS_VACINACAO_CALENDARIO_NACIONAL_COBERTURA_OCORRENCIA/SEIDIGI_DEMAS_VACINACAO_CALENDARIO_NACIONAL_COBERTURA_OCORRENCIA.html"
    )

    errors = [NoSuchElementException, ElementNotInteractableException]
    wait = WebDriverWait(
        driver, timeout=30, poll_frequency=0.2, ignored_exceptions=errors
    )
    
    wait.until(
        EC.all_of(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "dropdownsel.lui-select")
            ),
            EC.presence_of_all_elements_located((By.ID, "aba2-tab")),
            EC.element_to_be_clickable((By.ID, "aba2-tab")),
        )
    )
    time.sleep(2)

    return driver
