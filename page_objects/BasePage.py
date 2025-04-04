from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для страниц."""

    def __init__(self, driver, timeout: int = 10):
        """Инициализирует драйвер и ожидания."""
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, by: By, value: str) -> WebElement:
        """Находит один элемент на странице."""
        return self.wait.until(
            EC.visibility_of_element_located((by, value)),
            message=f'Элемент {by, value} не найден'
        )

    def find_elements(self, by: By, value: str) -> List[WebElement]:
        """Находит все элементы, соответствующие локатору, на странице."""
        return self.wait.until(
            EC.visibility_of_all_elements_located((by, value)),
            message=f'Элементы {by, value} не найдены'
        )

    def find_locator(self, locator: tuple) -> WebElement:
        """Находит один элемент на странице по переданному локатору."""
        return self.find_element(*locator)

    def find_locators(self, locator: tuple) -> List[WebElement]:
        """Находит список элементов на странице по переданному локатору."""
        return self.find_elements(*locator)

    def is_element_visible(self, locator: tuple) -> bool:
        """Проверяет, виден ли элемент на странице."""
        try:
            return self.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False

    def click_element(self, locator: tuple) -> None:
        """Кликает по элементу."""
        self.find_element(*locator).click()

    def click_element_in_row(self, row: WebElement, locator: tuple) -> None:
        """Кликает по элементу внутри строки таблицы."""
        row.find_element(*locator).click()

    def get_text(self, locator: tuple) -> str:
        """Получает текст элемента."""
        return self.find_element(*locator).text

    def get_row_text(self, row: WebElement, locator: tuple) -> str:
        """Получает текст элемента внутри строки таблицы."""
        try:
            if not isinstance(locator, tuple):
                raise ValueError(f"Locator должен быть кортежем. Получено: {locator}")
            return row.find_element(*locator).text
        except NoSuchElementException:
            print(f"Элемент по локатору {locator} не найден внутри строки.")
            return ''

    def fill_field(self, locator: tuple, text: str) -> None:
        """Заполняет поле текстом."""
        self.find_element(*locator).send_keys(text)

    def wait_for_element_to_be_visible(self, locator: tuple, timeout: int = 10) -> WebElement:
        """Ожидает, пока элемент станет видимым."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def get_element_text(self, locator: tuple) -> str:
        """Получает текст элемента, ожидая его появления."""
        element = self.wait_for_element_to_be_visible(locator)
        return element.get_attribute('textContent')

    def enter_text(self, locator: tuple, text: str) -> None:
        """Вводит текст в поле."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)
