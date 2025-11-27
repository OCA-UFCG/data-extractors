import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapping import setup
from utils.functions import save_file

if __name__ == "__main__":
    try:
        driver = setup()

        driver.find_element(By.ID, "aba2-tab").click()        
        
        [years, vaccines] = [Select(tag) for tag in driver.find_elements(By.CLASS_NAME, "dropdownsel.lui-select")]
        time.sleep(2)
        
        for year_i in range(len(years.options) - 1):
            print("year index:", year_i)
            print("Amount of years:", len(years.options))
            
            years.select_by_value(str(year_i))
            year = years.first_selected_option.text
            time.sleep(2)
            
            vaccines = Select(driver.find_elements(By.CLASS_NAME, "dropdownsel.lui-select")[1])
            values = [op.text for op in vaccines.options][1:]
                
            for vaccine in values:
                
                vaccines.select_by_visible_text(vaccine)
                
                errors = [NoSuchElementException, ElementNotInteractableException]
                wait = WebDriverWait(driver, timeout=30, poll_frequency=.2, ignored_exceptions=errors)
                wait.until(EC.presence_of_all_elements_located((By.ID, "exportar-dados-QV1-06")))
                
                button = driver.find_element(By.ID, "exportar-dados-QV1-06")
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                driver.execute_script("arguments[0].click();", button)
                
                # Wait for download to complete
                save_file(vaccine, year)
                vaccines = Select(driver.find_elements(By.CLASS_NAME, "dropdownsel.lui-select")[1])
                
            years = Select(driver.find_elements(By.CLASS_NAME, "dropdownsel.lui-select")[0])

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        print("Closing browser.")
        driver.quit()