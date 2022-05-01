from selenium.common.exceptions import NoSuchElementException

from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import BasePage

class Login_page(BasePage):
    USERNAME_INPUT = (By.XPATH, '//*[@id="username"]')
    PASS_INPUT = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/button/i')
    ERROR_MESSAGE=(By.XPATH, '//*[@id="flash"]')
    BTN_LOGIN=(By.XPATH, '//*[@id="login"]/button')
    LOGIN_H2 = (By.TAG_NAME, 'h2')
    ELEMENTAL_SELENIUM = (By.XPATH, '//a[contains(text(),"Elemental Selenium")]')
    FLASH_SUCCESS = (By.XPATH, '//*[@class="flash success"]')


    def navigate_to_home_page(self):
        self.driver.get('https://the-internet.herokuapp.com/login')

    def set_email(self,user):
        sleep(2)
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(user)

    def set_pass(self, pswd):
        self.driver.find_element(*self.PASS_INPUT).send_keys(pswd)

    def click_login_btn(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def click_logout(self):
        self.driver.find_element(*self.LOGOUT).click()

    def test_url(self):
        actual = self.driver.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        # expected value, actual value, mesaj in caz de fail
        self.assertEqual(expected, actual, 'URL is incorrect')

    def validate_error_message(self,text_error):
        actual=self.driver.find_element(*self.ERROR_MESSAGE).text
        expected=text_error
        self.assertIn(expected,actual,'the error message isn t correct')

    def test_elem_displayed(self):
        sleep(3)
        btn_login = self.driver.find_elements(*self.BTN_LOGIN)
        self.assertTrue(len(btn_login) == 1, 'The login button is not visible')

    def test_page_title(self):
        actual = self.driver.title
        expected = 'The Internet'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    def test_login_pageh2_text(self):
        actual = self.driver.find_element(*self.LOGIN_H2).text
        expected = 'Login Page'
        self.assertEqual(expected, actual, 'Login Page text is incorrect')

    def test_elem_atribute(self):
        actual = self.driver.find_element(*self.ELEMENTAL_SELENIUM).get_attribute('href')
        expected = 'http://elementalselenium.com/'
        self.assertEqual(expected, actual, 'Elemental Selenium href attribute is wrong!')

    def test_error_displayed(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        error = self.driver.find_element(*self.ERROR_MESSAGE)
        self.assertTrue(error.is_displayed(), 'Eroarea nu este afisata!')

    def test_closeerror_correct(self):
        close_error = self.driver.find_element(By.XPATH, '//*[@id="flash"]/a')
        close_error.click()
        try:
            self.driver.find_element(*self.ERROR_MESSAGE)
        except NoSuchElementException:
            pass

    def test_userandpass(self):
        label_list = self.driver.find_elements(By.TAG_NAME, 'label')
        self.assertEqual(label_list[0].text, 'Username', 'error')
        self.assertEqual(label_list[1].text, 'Password', 'error')

    def test_loginpage(self,header_message):
        actual = self.driver.current_url
        self.assertTrue('secure' in actual, 'Secure  is not present in URL')
        # elem gasit
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class="flash success"]')))
        elem = self.driver.find_element(*self.FLASH_SUCCESS)
        self.assertTrue(elem.is_displayed(), 'FLASH SUCCESS is not displayed!')
        self.assertTrue(header_message in elem.text, 'mesajul de pe text nu contine secure area')

    def test_verificareURL(self, current_url):
        actual = WebDriverWait(self.driver, 5).until(EC.url_changes('https://the-internet.herokuapp.com/secure'))
        # WebDriverWait(self.chrome, 5).until(EC.url_contains('/login')) initial am facut asa fara assert si testul a trecut
        expected = WebDriverWait(self.driver, 5).until(EC.url_to_be(current_url))
        self.assertEqual(expected, actual, 'URL is incorrect')

    def test_pass_hacking(self):
        elem_h = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/h4').text
        elem_h_list=elem_h.split()
        for element in elem_h_list:
            self.set_email('tomsmith')
            self.set_pass(element)
            self.click_login_btn()
            actual = self.driver.current_url
            if 'secure' in actual:
                print(f'Parola secreta este {element}')
                break
            else:
                print('Nu   am  reusit  sa gasesc parola')
