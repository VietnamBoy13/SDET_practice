import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.BasePage import BasePage
from helpers.AverageNameHelpers import NameHelpers


class CustomersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.table = (By.XPATH, "//table")
        self.input_locator = (By.XPATH, "//input[@placeholder='Search Customer']")
        self.rows_table = (By.XPATH, "//table/tbody/tr")
        self.first_column_locator = (By.XPATH, "./td[1]")
        self.button_delete = (By.XPATH, ".//button[contains(text(),'Delete')]")
        self.link_category_fist_name = (By.XPATH, ".//a[contains(text(), 'First Name')]")

    @allure.step("Получает список имен клиентов из таблицы Customers")
    def first_name_search(self):
        """Возвращает список имен клиентов из таблицы."""
        rows = self.find_elements(*self.rows_table)
        return [self.get_row_text(row, self.first_column_locator) for row in rows]

    @allure.step("Вводит 'First name' клиента в поле поиска")
    def input_customer(self, first_name: str):
        """Выбирает случайного клиента из списка и вводит его имя в поле поиска."""
        self.enter_text(self.input_locator, first_name)

    @allure.step("Проверяет наличие клиента в списке")
    def checking_customer(self):
        """Проверяет, что введенный в поиск клиент отображается в таблице."""
        search_input = self.get_text(self.input_locator)
        table = self.find_element(*self.table)
        assert search_input in table.text, f"Клиент '{search_input}' не найден в таблице!"

    def click_link_category_fist_name(self):
        self.click_element(self.link_category_fist_name)

    def examination_category_first_name(self):
        """
        Проверяет, что имена клиентов в списке находятся в правильном алфавитном порядке.
        """
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(self.rows_table)  # Ожидаем появления всех строк таблицы
        )

        name_list = self.first_name_search()

        # Проверка, что список отсортирован в алфавитном порядке
        assert name_list == sorted(name_list), "Список не находится в правильном алфавитном порядке"

    @allure.step("Удаляет клиента с именем, наиболее близким к среднему арифметическому")
    def delete_customer(self):
        """Удаляет клиента с именем, наиболее близким к среднему арифметическому."""
        name_list = self.first_name_search()
        closest_name = NameHelpers.find_closest_to_average(name_list)

        rows = self.find_elements(*self.rows_table)
        for row in rows:
            name = self.get_row_text(row, self.first_column_locator)
            if name == closest_name:
                self.click_element_in_row(row, self.button_delete)
                break

        # Ожидание, пока таблица обновится после удаления клиента
        WebDriverWait(self.driver, self.timeout).until(
            EC.staleness_of(self.find_element(*self.rows_table))  # Ожидаем исчезновение старой строки
        )

        # После обновления DOM проверяем, что клиента больше нет в таблице
        assert closest_name not in self.first_name_search(), f"Клиент {closest_name} не был удален"
