from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import BasePage
class Secure_page(BasePage):
    LOGOUT_BTN = (By.XPATH, '//*[@id="content"]/div/a/i')
    SUCCESSFULLY_MESSAGE=(By.ID,'flash')

    def navigate_to_secure_page(self):
        self.driver.get('https://the-internet.herokuapp.com/secure')

    def successfully_message(self):
        actual=self.driver.find_element(*self.SUCCESSFULLY_MESSAGE).text
        expected='You logged into a secure area!'
        self.assertEqual(expected, actual, 'Pagina de SECURE nu contine mesajul de succes')

    def text_displayed(self):
        actual=self.driver.find_elements(*self.SUCCESSFULLY_MESSAGE)
        self.assertTrue(len(actual) == 1, 'Textul nu este displayed')

    def click_logout(self):
        self.driver.find_element(*self.LOGOUT_BTN).click()
