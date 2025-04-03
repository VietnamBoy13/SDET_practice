import allure
from page_objects.BasePage import BasePage


class NameHelpers(BasePage):

    @staticmethod
    @allure.step("Находит имя, длина которого ближе всего к среднему арифметическому всех имен")
    def find_closest_to_average(name_list):
        """Находит имя, длина которого ближе всего к среднему арифметическому всех имен."""
        name_lengths = [len(name) for name in name_list]
        avg_length = sum(name_lengths) / len(name_lengths)
        return min(name_list, key=lambda name: abs(len(name) - avg_length))
