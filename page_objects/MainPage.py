import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class MainPage(BasePage):
    """Главная страница с кнопками управления клиентами."""

    def __init__(self, driver):
        """Инициализирует локаторы и вызывает конструктор родителя."""
        super().__init__(driver, timeout=60)
        self.button_add_customer = (
            By.XPATH,
            "//button[contains(text(), 'Add Customer')]"
        )
        self.button_customers = (
            By.XPATH,
            "//button[contains(text(), 'Customers')]"
        )

    @allure.step('Найти кнопку "Add Customer" и нажать на нее')
    def click_button_add_customer(self) -> None:
        """Нажимает кнопку 'Add Customer'."""
        self.click_element(self.button_add_customer)

    @allure.step('Найти кнопку "Customers" и нажать на нее')
    def click_button_customers(self) -> None:
        """Нажимает кнопку 'Customers'."""
        self.click_element(self.button_customers)
