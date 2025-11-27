import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.scrapping import setup, get_years_select, get_vaccines_select
from src.utils.functions import save_file
from src.logging import logger

if __name__ == "__main__":
    try:
        driver = setup()
        logger.info("Setting up driver.")

        driver.find_element(By.ID, "aba2-tab").click()

        years = get_years_select(driver)
        years_options = [op.text for op in years.options][1:]

        for year in years_options:
            years.select_by_visible_text(year)
            time.sleep(2)

            vaccines = get_vaccines_select(driver)
            
            values = [op.text for op in vaccines.options][1:]

            for vaccine in values:

                vaccines.select_by_visible_text(vaccine)
                logger.info(f"Vaccine {vaccine} selected for year {year}")

                errors = [NoSuchElementException, ElementNotInteractableException]
                wait = WebDriverWait(
                    driver, timeout=30, poll_frequency=0.2, ignored_exceptions=errors
                )
                wait.until(EC.element_to_be_clickable((By.ID, "exportar-dados-QV1-06")))

                button = driver.find_element(By.ID, "exportar-dados-QV1-06")
                driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", button
                )
                driver.execute_script("arguments[0].click();", button)

                save_file(vaccine, year)
                vaccines = get_vaccines_select(driver)

            years = get_years_select(driver)

    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        # Close the browser
        logger.info("Closing browser.")
        driver.quit()
