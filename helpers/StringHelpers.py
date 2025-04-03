import string
import allure


@allure.step("Преобразует почтовый код в строку (имя) по заданной логике")
def convert_to_name(post_code: str) -> str:
    """
    Преобразует числовой почтовый код в строку (имя).

    Логика: каждые две цифры интерпретируются как число,
    берется остаток от деления на 26 и сопоставляется с буквой латинского алфавита.

    :param post_code: Почтовый код в виде строки из цифр
    :return: Сгенерированное имя в формате строки
    """
    name = ""
    for i in range(0, len(post_code), 2):
        num = int(post_code[i:i + 2]) % 26  # Приводим к диапазону 0-25
        letter = string.ascii_lowercase[num]
        name += letter
    return name.capitalize()
