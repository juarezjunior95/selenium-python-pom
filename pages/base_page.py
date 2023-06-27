import conftest


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)

    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)

    def escrever(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)

    def click(self, locator):
        self.encontrar_elemento(locator).click()


    def verify_if_there_element(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), f"The element '{locator}' not found in the screen."


    def get_element_text(self,locator):
        return self.get_element_text(locator).text
