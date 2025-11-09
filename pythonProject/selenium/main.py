from config.settings import GOOGLE_URL, SEARCH_TERM
from utils.driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def run_automation():
    driver = get_driver()
    driver.get(GOOGLE_URL)

    search_box = driver.find_element(By.NAME, "q")

    search_box.send_keys(SEARCH_TERM)

    search_box.send_keys(Keys.RETURN)

    time.sleep(60)
    driver.quit()

if __name__ == "__main__":
    run_automation()