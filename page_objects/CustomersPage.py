import random
import time
import allure
from selenium.webdriver.common.by import By
from conftest import driver
from page_objects.BasePage import BasePage

class CustomersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.tabel = (By.XPATH, "//table")
        self.input_locator = (By.XPATH, "//input[@placeholder='Search Customer']")
        self.rows_tabel = (By.XPATH, "//table/tbody/tr")
        self.first_column_locator = (By.XPATH, "./td[1]")
        self.button_delete = (By.XPATH, ".//button[contains(text(),'Delete')]")

    @allure.step("Получает список имен клиентов из таблицы Customers")
    def first_name_search(self):
        rows = self.find_elements(*self.rows_tabel)  # Получаем все строки таблицы
        name_list = [self.get_row_text(row, self.first_column_locator) for row in rows]
        return name_list

    @allure.step("Ввод 'Fist name' клиента в список")
    def input_customer(self):
        name_list = self.first_name_search()
        selected_customer = random.choice(name_list)
        self.enter_text(self.input_locator, selected_customer)

    @allure.step("Проверяет наличие клиента в списке")
    def checking_customer(self):
        search_input = self.get_text(self.input_locator)
        table = self.find_element(*self.tabel)
        assert search_input in table.text, f"Клиент '{search_input}' не найден в таблице!"


    @staticmethod
    @allure.step("Находит имя, длина которого ближе всего к среднему арифметической длине всех имен.")
    def find_closest_to_average(name_list):
        name_lengths = [len(name) for name in name_list]
        avg_length = sum(name_lengths) / len(name_lengths)
        closest_name = min(name_list, key=lambda name: abs(len(name) - avg_length))
        return closest_name

    @allure.step("Удаляет клиента с именем, наиболее близким к среднему арифметическому")
    def delete_customer(self):
        name_list = self.first_name_search()
        closest_name = self.find_closest_to_average(name_list)
        # Ищем строку с этим клиентом и нажимаем кнопку "Delete"
        rows = self.find_elements(*self.rows_tabel)
        for row in rows:
            name = self.get_row_text(row, self.first_column_locator)
            if name == closest_name:
                self.click_element_in_row(row, self.button_delete)
                break
        time.sleep(2)

        assert closest_name not in self.first_name_search(), f"Клиент {closest_name} не был удален"