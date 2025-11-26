import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

PATH = "/Users/rodrigoec/cc/oca/data-extractors/cobertura-vacinal/chromedriver/chromedriver"
service = Service(executable_path=PATH)

options = webdriver.ChromeOptions()
prefs = {
    "download.prompt_for_download": False,
    "download.default_directory": "./downloads",
    "safebrowsing.enabled": True
}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)

# driver = webdriver.Chrome(service=service)


# Navigate to a website
driver.get("https://infoms.saude.gov.br/extensions/SEIDIGI_DEMAS_VACINACAO_CALENDARIO_NACIONAL_COBERTURA_OCORRENCIA/SEIDIGI_DEMAS_VACINACAO_CALENDARIO_NACIONAL_COBERTURA_OCORRENCIA.html")

try:
    errors = [NoSuchElementException, ElementNotInteractableException]
    wait = WebDriverWait(driver, timeout=30, poll_frequency=.2, ignored_exceptions=errors)

    # Wait for the select elements to be present
    select_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "dropdownsel.lui-select")))
    
    selects = driver.find_elements(By.CLASS_NAME, "dropdownsel.lui-select")
    # select = Select(selects[1])
    
    # for el in selects:
    #     select = Select(el)
    #     for option in select.options:
    #         print(option.text)
            
    # [yearSelect, vacinaSelect] = selects
    time.sleep(5)
    driver.find_element(By.ID, "aba2-tab").click()        
    
    time.sleep(1)
    # ySel = Select(yearSelect)
    vSel = Select(driver.find_elements(By.CLASS_NAME, "dropdownsel.lui-select")[1])
    time.sleep(2)
    
    for i in range(1, len(vSel.options)):
        # vSel = Select(vacinaSelect)
        vSel = Select(driver.find_elements(By.CLASS_NAME, "dropdownsel.lui-select")[1])
        option = vSel.options[i]
        option.click()
        time.sleep(2)
        
        button = driver.find_element(By.ID, "exportar-dados-QV1-06")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        driver.execute_script("arguments[0].click();", button)
        # link.click()
        time.sleep(3)

        
        
        
    # print(ySel.options)
    # print(selects)
    # time.sleep(2)
    # selects[1].click()
    # select.select_by_index(2)
    time.sleep(5)
    # print(len(select.options))
    # for option in select.options[1:]:
    #     option.click()

    # This selector might need adjustment for the specific page structure.
    # It assumes the options are list items directly following the click.
    # for option in year_select_element.options:
    #     option.click()

    # Close the dropdown by clicking the select element again to be safe
    # year_select_element.click()
    # time.sleep(1)  # a small pause to allow UI to update

    # # Now, iterate through each option by index
    # for i in range(num_options):
    #     print(f"Processing option index: {i}")
    #     try:
    #         # Re-find the select element each time to avoid stale element issues and open it
    #         select_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lui-select")))
    #         year_select_element = select_elements[1]
    #         year_select_element.click()

    #         # Find and click the option by its index
    #         # Re-fetch options every time to avoid staleness
    #         current_options = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.lui-list__item")))
    #         if i < len(current_options):
    #             current_options[i].click()
    #         else:
    #             print(f"Option index {i} out of bounds.")
    #             # close dropdown and continue
    #             year_select_element.click()
    #             continue

    #         # Click the tab
    #         aba2_tab = wait.until(EC.element_to_be_clickable((By.ID, "aba2-tab")))
    #         aba2_tab.click()

    #         # Click the export link
    #         export_link = wait.until(EC.element_to_be_clickable((By.ID, "exportar-dados-QV1-06")))
    #         export_link.click()

    #         # Wait a bit for download to start if needed
    #         time.sleep(2)

    #     except Exception as e:
    #         print(f"Failed to process option index {i}: {e}")
    #         # If something goes wrong, maybe close the dropdown and continue
    #         try:
    #             # try to click body to close any popups/dropdowns
    #             driver.find_element(By.TAG_NAME, 'body').click()
    #         except:
    #             pass  # ignore if it fails
    #         continue

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser
    print("Closing browser.")
    driver.quit()