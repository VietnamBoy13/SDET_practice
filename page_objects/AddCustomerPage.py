import random
import string
import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage

@allure.step("Генерирует случайный почтовый код из 10 цифр")
def generate_post_code(length=10):
    return ''.join(random.choices(string.digits, k=length))

@allure.step("Преобразует почтовый код в строку (имя) по заданной логике")
def convert_to_name(post_code):
    name = ""
    for i in range(0, len(post_code), 2):
        num = int(post_code[i:i + 2]) % 26  # Приводим к диапазону 0-25
        letter = string.ascii_lowercase[num]
        name += letter
    return name.capitalize()


class AddCustomerPage(BasePage):
    FIRST_NAME_INPUT = (By.XPATH, "//input[@ng-model='fName']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@ng-model='lName']")
    POST_CODE_INPUT = (By.XPATH, "//input[@ng-model='postCd']")
    SUBMIT_BTN = (By.XPATH, "//button[text()='Add Customer']")

    @allure.step("Заполняет форму нового клиента")
    def add_customer(self, last_name="Doe"):
        post_code = generate_post_code()
        first_name = convert_to_name(post_code)

        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.POST_CODE_INPUT, post_code)

    @allure.step("Отправляет форму нового клиента")
    def click_button_add_customer(self):
        self.click_element(self.SUBMIT_BTN)




