import random
import string
import allure


@allure.step("Генерирует случайный почтовый код из {length} цифр")
def generate_post_code(length: int = 10) -> str:
    """
    Генерирует случайный почтовый код из цифр.

    :param length: Длина почтового кода (по умолчанию 10)
    :return: Строка, содержащая случайный набор цифр
    """
    return ''.join(random.choices(string.digits, k=length))
