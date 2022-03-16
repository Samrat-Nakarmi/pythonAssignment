import os
from selenium.webdriver.common.by import By
from selenium import webdriver
import path, secret
import time

browser = webdriver.Firefox(executable_path = os.path.join(os.getcwd(), "geckodriver.exe"))
browser.get('https://classroom.google.com/u/1/h')

email = browser.find_element(By.XPATH, path.emailpath)
email.send_keys(secret.email)
button = browser.find_element(By.XPATH, path.buttonpath)
button.click()
time.sleep(3)

password = browser.find_element(By.XPATH, path.passwordpath)
password.send_keys(secret.password)
button2 = browser.find_element(By.XPATH, path.button2path)
button2.click()

