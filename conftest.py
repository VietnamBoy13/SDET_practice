import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_objects.Data import Urls

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--enable-javascript')
    _driver = webdriver.Chrome(options=options)
    _driver.get(Urls.BankManager)
    yield _driver
    _driver.quit()