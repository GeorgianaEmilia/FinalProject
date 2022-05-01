from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import BasePage

class Sign_in_page(BasePage):
    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Enter your email"]')
    PASS_INPUT = (By.XPATH, '//input[@placeholder="Enter your password"]')
    LOGIN_BUTTON = (By.XPATH, '//span[text()="Log in"]/parent::button')
    FORGOT_PSWD_LINK = (By.XPATH, '//a[text()="Forgot password?"]')

    def navigate_to_sign_in_page(self):
        self.driver.get('https://jules.app/sign-in')
    # step (cea mai mica actiune ce poate sa  faca un utilizator pe o pagina)

    def set_email(self, email):
        print("test2")
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_pass(self, pswd):
        self.driver.find_element(*self.PASS_INPUT).send_keys(pswd)

    def click_login_btn(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
    # step definition ( o agregare de pasi mici care au logica sa fie sub o singura umbrela/functie)
    def user_login(self, email, pswd):
        self.set_email(email)
        self.set_pass(pswd)
        self.click_login_btn()

    def click_forgot_pswd_link(self):
        self.driver.find_element(*self.FORGOT_PSWD_LINK).click()
