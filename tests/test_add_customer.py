import allure
from conftest import driver
from page_objects.CustomersPage import CustomersPage
from page_objects.MainPage import MainPage
from page_objects.AddCustomerPage import AddCustomerPage


@allure.title('Проверка создания нового клиента')
@allure.description('''
Шаги:
1. Нажать на кнопку "Add Customer".
2. Ввести случайное значение в поле "First Name" (сгенерированное из Post Code).
3. Ввести случайное значение в поле "Last Name".
4. Сгенерировать 10-значный Post Code и ввести в соответствующее поле.
5. Нажать кнопку "Add Customer".
''')
def test_add_customer(driver):
    main_page = MainPage(driver)
    main_page.click_button_add_customer()
    add_customer_page = AddCustomerPage(driver)
    add_customer_page.add_customer()
    add_customer_page.click_button_add_customer()

@allure.title('Проверка наличия добавленного клиента в списке')
@allure.description('''
Шаги:
1. Нажать на кнопку "Customers".
2. В поле поиска ввести "First Name".
3. Проверить, что в таблице отображается созданный клиент с правильными данными.
''')
def test_checking_customer(driver):
    main_page = MainPage(driver)
    main_page.click_button_customers()
    customers_page = CustomersPage(driver)
    customers_page.input_customer()
    customers_page.checking_customer()


@allure.title('Проверка наличия добавленного клиента в списке')
@allure.description('''
Шаги:
1. Нажать на кнопку "Customers".
2. Находим имя, длина которого ближе всего к среднему арифметической длине всех имен.
3. Ищем строку с этим клиентом и нажимаем кнопку "Delete"
''')
def test_delete_customer(driver):
    main_page = MainPage(driver)
    main_page.click_button_customers()
    customers_page = CustomersPage(driver)
    customers_page.delete_customer()
