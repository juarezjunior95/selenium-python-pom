import self as self

import conftest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button =  (By.ID, "login-button")
        self.error_message_login= (By.XPATH, "//button[contains(@class,'error-button')]")


    def fazer_login(self, usuario, senha):
        #self.driver.find_element(*self.username_field).send_keys(usuario)
        #self.driver.find_element(*self.password_field).send_keys(senha)
        #self.driver.find_element(*self.login_button).click()
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.click(self.login_button)

    def verify_message_error_login_exist(self):
        self.verify_if_there_element(self.error_message_login)


    def  verify_message_text_error_login(self,text_expected):
        text_found = self.get_element_text(self.error_message_login)
        assert text_found == text_expected, f"O texto encontrado foi '{text_found}', mas o espera o texto {text_expected}"
