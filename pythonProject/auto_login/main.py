from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from login_config import URL, USERNAME, PASSWORD
import os
import time

driver = webdriver.Edge()

driver.get(URL)
driver.maximize_window()
time.sleep(5)

username_field = driver.find_element(By.ID, value="username")
password_field = driver.find_element(By.ID, value="password")

username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)

login_button = driver.find_element(By.XPATH, value="//button[@id='submit]")
login_button.click()

time.sleep(30)
driver.quit()