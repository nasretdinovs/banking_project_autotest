import allure
import pytest
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options

from constants import ACCOUNT_URL, SELENIUM_SERVER_URL, USER
from pages.login import LoginPage


@pytest.fixture
def init_selenium():
    options = Options()
    options.set_capability('browserName', 'chrome')

    driver = Remote(command_executor=SELENIUM_SERVER_URL, options=options)
    login_page = LoginPage(driver)
    login_page.open_page()

    yield driver, login_page

    driver.quit()


@allure.description("Тестирование входа пользователя")
@allure.feature('Banking Project')
@allure.story('Тест страницы Login')
def test_login(init_selenium):
    driver, login_page = init_selenium
    customer_page = login_page.click_customer()
    customer_page.select_customer(USER)
    customer_page.click_login()

    assert "XYZ Bank" in driver.title
    assert driver.current_url == ACCOUNT_URL, \
        f'Ожидался {ACCOUNT_URL}, но получили {driver.current_url}'
