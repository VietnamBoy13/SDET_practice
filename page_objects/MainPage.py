from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.button_add_customer = (
            By.XPATH,
            "//button[contains(text(), 'Add Customer')]"
        )
        self.button_customers = (
            By.XPATH,
            "//button[contains(text(), 'Customers')]"
        )

    @allure.step('Найти кнопку (Add Customer) и нажать на нее')
    def click_button_add_customer(self) -> None:
        self.click_element(self.button_add_customer)

    @allure.step('Найти кнопку (Customers) и нажать на нее ')
    def click_button_customers(self) -> None:
        self.click_element(self.button_customers)


