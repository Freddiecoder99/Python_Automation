from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import config

driver = webdriver.Edge()

driver.get(config.URL)
driver.maximize_window()

try:
    WebDriverWait(driver, timeout=10).until(
        EC.presence_of_element_located((By.NAME, "firstname"))
    )

    driver.find_element(By.NAME, value="firstname").send_keys(config.FORM_DATA["first_name"])
    driver.find_element(By.NAME, value="lastname").send_keys(config.FORM_DATA["last_name"])

    if config.FORM_DATA["gender"].lower() == "male":
        driver.find_element(By.ID, value="sex-0").click()
    else:
        driver.find_element(By.ID, value="sex-1").click()

    driver.find_element(By.ID, value=f"exp-{config.FORM_DATA['experience']}").click()

    driver.find_element(By.ID, value="profession-0").click()

    driver.find_element(By.ID, value="tool-2").click()

    driver.find_element(By.ID, value="submit").click()

    time.sleep(10)

except Exception as e:
    print("Error:", e)

driver.quit()
