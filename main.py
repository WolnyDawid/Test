from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import main_page


driver = webdriver.Chrome(service=Service('C:\TestingFiles\chromedriver.exe'))
driver.get('https://my.clippings.io/login')
driver.implicitly_wait(3)
main_page = main_page.MainPage(driver)

username_input = main_page.findElementById("__BVID__25")
password_input = main_page.findElementById("txtPassword")

username_input.send_keys("Login")
password_input.send_keys("Password")

button_clicker = driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']")

driver.close()
