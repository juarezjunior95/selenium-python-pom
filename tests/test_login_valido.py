import time
import pytest

from selenium.webdriver.common.by import By

import conftest
from pages.login_page import  LoginPage
from pages.home_page import   HomePage





@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.addcarrinho
class TestCT01:
    def test_login_valido(self):
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()

        login_page.fazer_login("standard_user" , "secret_sauce")
        home_page.verify_sucess_login()

        #Add um produto no carrinho
        driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()


        #Ir para carrinho de compras
        driver.find_element(By.XPATH,"//a[contains(@class,'shopping_cart_link')]").click()

        #Validando que produto foi add no carrinho
        assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name'][contains(.,'Sauce Labs Backpack')]").is_displayed()
        ##Fazer checkout e preencher os dados e clicar no botao continue para tela de checkout

        driver.find_element(By.ID,"checkout").click()

        driver.find_element(By.ID, "first-name").send_keys('Juarez cruz')
        driver.find_element(By.ID, "last-name").send_keys("Sobrenome aleatorio")
        driver.find_element(By.ID, "postal-code").send_keys("42803169")

        element = driver.find_element(By.ID, "continue")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.find_element(By.ID ,"continue").click()

        ##Validar o total da compra e finalizar compra

        driver.find_element(By.XPATH, "//div[@class='summary_info_label summary_total_label']").is_displayed()
        driver.find_element(By.ID, "finish").click()

        ##validar menssagem de compra feita com sucesso

        driver.find_element(By.XPATH,"//h2[contains(.,'Thank you for your order!')]").is_displayed()


        time.sleep(2)

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.todologout
class TestCT02:
    def test_login_valido(self):
            driver = conftest.driver
            login_page = LoginPage()
            home_page = HomePage()

            login_page.fazer_login("standard_user", "secret_sauce")
            home_page.verify_sucess_login()


            driver.find_element(By.XPATH, "//div[@class='app_logo'][contains(.,'Swag Labs')]").is_displayed()
            time.sleep(2)
            driver.find_element(By.XPATH, "//button[contains(.,'Open Menu')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH ,"//a[contains(.,'Logout')]").click()
            time.sleep(2)

            driver.find_element(By.XPATH,"//div[@class='login_logo'][contains(.,'Swag Labs')]").is_displayed()


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.higherprice
class TestCT03:
    def test_login_valido(self):
            driver = conftest.driver
            login_page = LoginPage()
            home_page = HomePage()

            login_page.fazer_login("standard_user", "secret_sauce")
            home_page.verify_sucess_login()

            driver.find_element(By.XPATH , "//select[contains(@class,'product_sort_container')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//option[@value='lohi']").click()
            time.sleep(2)
