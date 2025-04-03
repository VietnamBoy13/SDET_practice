import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AddCustomerPage(BasePage):
    first_name_input = (By.XPATH, "//input[@ng-model='fName']")
    last_name_input = (By.XPATH, "//input[@ng-model='lName']")
    post_code_input = (By.XPATH, "//input[@ng-model='postCd']")
    submit_button = (By.XPATH, "//button[text()='Add Customer']")

    @allure.step("Заполняет форму нового клиента")
    def add_customer(self, first_name: str, last_name: str, post_code: str):
        self.enter_text(self.first_name_input, first_name)
        self.enter_text(self.last_name_input, last_name)
        self.enter_text(self.post_code_input, post_code)

    @allure.step("Отправляет форму нового клиента")
    def click_button_add_customer(self):
        self.click_element(self.submit_button)
