from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.title_page = (By.XPATH, "//span[@class='title'][contains(.,'Products')]")


    def verify_sucess_login(self):
        self.verify_if_there_element(self.title_page)


