import os
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from src.utils.constants import DOWNLOAD_PATH
from src.utils.functions import wait_for_selenium


def get_default_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    prefs = {
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "download.default_directory": "/data",
        "safebrowsing.enabled": True,
    }
    options.add_experimental_option("prefs", prefs)

    return options


def setup():

    options = webdriver.ChromeOptions()

    os.makedirs(DOWNLOAD_PATH, exist_ok=True)

    options = get_default_chrome_options()
    wait_for_selenium()
    driver = webdriver.Remote(
        command_executor="http://chromeNode:4444/wd/hub", options=options
    )
    print(driver)
    # driver = webdriver.Chrome(options=options, service=service)
    driver.execute_cdp_cmd(
        "Page.setDownloadBehavior", {"behavior": "allow", "downloadPath": "/data"}
    )

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


def get_years_select(driver):
    return Select(driver.find_elements(By.CLASS_NAME, "dropdownsel.lui-select")[0])


def get_vaccines_select(driver):
    return Select(driver.find_elements(By.CLASS_NAME, "dropdownsel.lui-select")[1])
