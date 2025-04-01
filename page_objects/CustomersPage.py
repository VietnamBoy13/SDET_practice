import random
import allure
from selenium.webdriver.common.by import By
from conftest import driver
from page_objects.BasePage import BasePage

class CustomersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.input_locator = (By.XPATH, "//input[@placeholder='Search Customer']")

    @allure.step("Получает список имен клиентов из таблицы Customers")
    def first_name_search(self):
        self.find_element(By.XPATH, "//button[contains(text(),'Customers')]").click()
        rows = self.find_elements(By.XPATH, "//table/tbody/tr")
        name_list = [row.find_element(By.XPATH, "./td[1]").text for row in rows]
        return name_list

    @allure.step("Ввод 'Fist name' клиента в список")
    def input_customer(self):
        name_list = self.first_name_search()
        selected_customer = random.choice(name_list)
        self.enter_text(self.input_locator, selected_customer)

    @allure.step("Проверяет наличие клиента в списке")
    def checking_customer(self):
        search_input = self.get_text(self.input_locator)
        table = self.find_element(By.XPATH, "//table")
        assert search_input in table.text


    @staticmethod
    @allure.step("Находит имя, длина которого ближе всего к среднему арифметической длине всех имен.")
    def find_closest_to_average(name_list):
        name_lengths = [len(name) for name in name_list]
        avg_length = sum(name_lengths) / len(name_lengths)
        # Определяем имя, длина которого ближе всего к среднему арифметическому
        closest_name = min(name_list, key=lambda name: abs(len(name) - avg_length))
        return closest_name

    @allure.step("Удаляет клиента с именем, наиболее близким к среднему арифметическому")
    def delete_customer(self):
        name_list = self.first_name_search()
        closest_name = self.find_closest_to_average(name_list)
        # Ищем строку с этим клиентом и нажимаем кнопку "Delete"
        rows = self.find_elements(By.XPATH, "//table/tbody/tr")
        for row in rows:
            name = row.find_element(By.XPATH, "./td[1]").text
            if name == closest_name:
                row.find_element(By.XPATH, ".//button[contains(text(),'Delete')]").click()
                break