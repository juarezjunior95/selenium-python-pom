import time
import pytest

from selenium.webdriver.common.by import By

import conftest
from pages.home_page import   HomePage
from pages.login_page import  LoginPage



@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.logininvalido
class TestCT01:

    def test_login_invalido(self):

        error_message_expected = "Epic sadface: Username and password do not match any user in this service"

        ##driver = conftest.driver
        login_page = LoginPage()


        login_page.fazer_login("standard_user" , "errado")


        ##login nao feito e mensagem de erro exibida
        login_page.verify_message_error_login_exist()
        login_page.verify_message_text_error_login(error_message_expected)
        ##assert driver.find_element(By.XPATH ,"//button[contains(@class,'error-button')]").is_displayed()
