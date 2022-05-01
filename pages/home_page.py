from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Home_page(BasePage):
    FORM_AUTHENTICATION=(By.XPATH, '//a[contains(text(), "Form Authentication")]')
    DROP_DOWN=(By.XPATH,'//a[contains(text(),"Dropdown")]')
    REDIRECT_LINK=(By.XPATH,'//a[contains(text(),"Redirect Link")]')

    def navigate_to_home_page(self):
        self.driver.get('https://the-internet.herokuapp.com/')

    def click_form_authentication(self):
        self.driver.find_element(*self.FORM_AUTHENTICATION).click()

    def click_drop_down(self):
        self.driver.find_element(*self.DROP_DOWN).click()

    def click_redirect_link(self):
        self.driver.find_element(*self.REDIRECT_LINK).click()
