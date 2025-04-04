import allure
from conftest import driver
from selenium.common.exceptions import NoAlertPresentException

from page_objects.CustomersPage import CustomersPage
from page_objects.MainPage import MainPage
from page_objects.AddCustomerPage import AddCustomerPage
from helpers.DataHelpers import generate_post_code
from helpers.StringHelpers import convert_to_name


@allure.title("Проверка создания нового клиента")
@allure.description(
    """
    Шаги:
    1. Нажать на кнопку "Add Customer".
    2. Ввести случайное значение в поле "First Name" 
       (сгенерированное из Post Code).
    3. Ввести случайное значение в поле "Last Name".
    4. Сгенерировать 10-значный Post Code и ввести в соответствующее поле.
    5. Нажать кнопку "Add Customer" для завершения.
    6. Закрытие всплывающего алерта.
    7. Перейти в список клиентов.
    8. Найти клиента в списке.
    9. Проверить, что клиент отображается в списке.
    """
)
def test_add_customer(driver):
    """Тест на добавление нового клиента."""
    main_page = MainPage(driver)

    with allure.step("Нажать кнопку 'Add Customer'"):
        main_page.click_button_add_customer()

    add_customer_page = AddCustomerPage(driver)
    post_code = generate_post_code()
    first_name = convert_to_name(post_code)
    last_name = "Doe"

    with allure.step("Заполнить форму нового клиента"):
        add_customer_page.add_customer(first_name, last_name, post_code)

    with allure.step("Нажать кнопку 'Add Customer' для завершения"):
        add_customer_page.click_button_add_customer()

    # Ожидание алерта и его закрытие
    with allure.step("Закрытие всплывающего алерта"):
        try:
            alert = driver.switch_to.alert
            allure.attach(alert.text, name="Alert Text", attachment_type=allure.attachment_type.TEXT)
            alert.accept()
        except NoAlertPresentException:
            print("No alert detected.")

    # Переход к списку клиентов
    with allure.step("Перейти в список клиентов"):
        main_page.click_button_customers()

    customers_page = CustomersPage(driver)

    with allure.step("Найти клиента в списке"):
        customers_page.input_customer(first_name)

    with allure.step("Проверить, что клиент отображается в списке"):
        customers_page.checking_customer()


@allure.title('Проверка сортировки клиентов по имени')
@allure.description('''
Шаги:
1. Перейти на страницу "Customers".
2. Нажать на ссылку для сортировки клиентов по имени.
3. Проверить, что клиенты отсортированы в алфавитном порядке.
''')
def test_checking_customer(driver):
    """Тест на проверку сортировки клиентов по имени."""
    main_page = MainPage(driver)

    # Шаг 1: Перейти на страницу "Customers"
    with allure.step('Перейти на страницу "Customers"'):
        main_page.click_button_customers()

    customers_page = CustomersPage(driver)

    # Шаг 2: Нажать на ссылку для сортировки клиентов по имени
    with allure.step('Нажать на ссылку для сортировки клиентов по имени'):
        customers_page.click_link_category_fist_name()

    # Шаг 3: Проверить, что клиенты отсортированы в алфавитном порядке
    with allure.step('Проверить, что клиенты отсортированы по имени'):
        customers_page.examination_category_first_name()


@allure.title("Проверка удаления клиента")
@allure.description(
    """
    Шаги:
    1. Нажать на кнопку "Customers".
    2. Найти имя, длина которого ближе всего к 
       среднему арифметическому длине всех имен.
    3. Найти строку с этим клиентом и нажать кнопку "Delete".
    """
)
def test_delete_customer(driver):
    """Тест на удаление клиента."""
    main_page = MainPage(driver)

    with allure.step("Перейти в список клиентов"):
        main_page.click_button_customers()

    customers_page = CustomersPage(driver)

    with allure.step("Удалить клиента"):
        customers_page.delete_customer()
