from selenium.webdriver.common.by import By


class MainPage:

    def findElementById(self, element):
        return self.driver.find_element(By.ID, element)

    def findElementByXPATH(self, elementt):
        return self.driver.find_element(By.XPATH, elementt)

    def __init__(self, driver):
        self.driver = driver
