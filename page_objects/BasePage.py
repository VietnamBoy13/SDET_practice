from typing import List

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = int(timeout)
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, by: By, value: str) -> WebElement:
        """
        Находит один элемент на странице
        :param by: Способ поиска локаторов
        :param value: Значение локатора
        :return: WebElement
        """
        return self.wait.until(expected_conditions.visibility_of_element_located((by, value)),
                               message=f'Элемент {by, value} не найден')

    def find_elements(self, by: By, value: str) -> List[WebElement]:
        """
        Находит все элементы, соответствующие локатору, на странице
        :param by: Способ поиска локаторов
        :param value: Значение локатора
        :return: Список WebElement
        """

        return self.wait.until(expected_conditions.visibility_of_all_elements_located((by, value)),
                               message=f'Элементы {by, value} не найдены')

    def is_element_visible(self, locator: tuple) -> bool:
        """
        Проверяет, виден ли элемент на странице.
        :param locator: Кортеж, определяющий локатор
        :return: True, если элемент виден; False, если элемент не виден.
        """
        try:
            element = self.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def click_element(self, locator: tuple) -> None:
        """
        Кликает по элементу
        :param locator: Кортеж, определяющий локатор
        """
        self.find_element(*locator).click()

    def get_text(self, locator: tuple) -> str:
        """
        Получает текст элемента
        :param locator: Кортеж, определяющий локатор
        :return: Текст элемента
        """
        return self.find_element(*locator).text

    def fill_field(self, locator: tuple, info: str) -> None:
        """
        Заполняет поле текстом
        :param locator: Кортеж, определяющий локатор
        :param info: Текст для ввода
        """
        self.find_element(*locator).send_keys(info)

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        """Ожидание видимости элемента на странице."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def get_element_text(self, locator) -> str:
        """Получение текста элемента, ожидая его появления."""
        element = self.wait_for_element_to_be_visible(locator)
        return element.get_attribute('textContent')

    def enter_text(self, locator, text):
        """Вводит текст в поле"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

