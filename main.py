from selenium import webdriver
from pathlib import Path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import datetime

script_directory = Path(__file__).resolve().parent


print("This script will automatically fetch your attendance info from ERP website.")
USERNAME = input("Enter Username: ")
PASSWORD = input("Enter Password: ")

driver_path = script_directory / "chromedriver-win64" / "chromedriver.exe"

service = Service(driver_path)

debugging = False
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
if debugging:
    chrome_options.add_experimental_option("detach", True)
else:
    chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://erp.rajalakshmi.org/")


username_input = driver.find_element(By.ID, "txt_username")
password_input = driver.find_element(By.ID, "txt_password")
captcha_element = driver.find_element(By.ID, "txtcaptcha")
data_captcha_value = captcha_element.get_attribute("data-captcha")
login_button = driver.find_element(By.ID, "btnLogin")

if username_input:
    username_input.send_keys(USERNAME)
if password_input:
    password_input.send_keys(PASSWORD)
if captcha_element:
    captcha_element.send_keys(data_captcha_value)
if login_button:
    login_button.click()

time.sleep(5)
att_button = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnLoadAttend")
if att_button:
    att_button.click()
time.sleep(1)

att_box = driver.find_element(By.ID, "tbodyAtten")
print(datetime.datetime.now())
print("SUBJECT LECTURES PERCENT")
print(att_box.text)

if not debugging:
    driver.quit()
