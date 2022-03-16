from selenium import webdriver
from selenium.webdriver.common.by import By
import os

browser = webdriver.Firefox(executable_path = os.path.join(os.getcwd(), "geckodriver.exe"))
browser.get('https://deerwalk.edu.np/')

alllinks = browser.find_elements(By.TAG_NAME, 'a')

list = []
for link in alllinks:
    list.append(link.get_attribute('href'))
    print(link.get_attribute('href'))

browser.close()
for x in list:
    file = open('link.txt', 'w')
    file.write(f'{x}')
    file.close()
