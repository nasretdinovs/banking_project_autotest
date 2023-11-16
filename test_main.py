import csv
import time
from typing import Generator, Tuple
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options

from constants import ACCOUNT_URL, SELENIUM_SERVER_URL, TRANSACTIONS_URL, USER
from pages.login import LoginPage
from utils import fibonacci_for_date


@pytest.fixture
def driver_options() -> Generator[Tuple[Remote, LoginPage], None, None]:
    """Фикстура для создания Selenium драйвера с заданными опциями и
    открытия страницы входа.
    """

    options = Options()
    options.set_capability('browserName', 'chrome')

    driver = Remote(command_executor=SELENIUM_SERVER_URL, options=options)
    login_page = LoginPage(driver)
    login_page.open_page()

    yield driver, login_page

    driver.quit()


@allure.description('Тестирование входа пользователя')
@allure.feature('Banking Project')
@allure.story('Тест страницы Login')
def test_login(driver_options: Tuple[Remote, LoginPage]) -> None:
    """Тестирование входа пользователя."""

    driver, login_page = driver_options
    customer_page = login_page.click_customer()
    customer_page.select_customer(USER)
    customer_page.click_login()

    assert 'XYZ Bank' in driver.title
    assert driver.current_url == ACCOUNT_URL, (
        f'Ожидаемый URL: {ACCOUNT_URL}, а фактический: {driver.current_url}')


@allure.description('Тестирование операций пополнения и снятия средств')
@allure.feature('Banking Project')
@allure.story('Тест пополнения и снятия средств со счёта')
def test_deposit_withdraw(driver_options: Tuple[Remote, LoginPage]) -> None:
    """Тестирование операций пополнения и снятия средств."""

    driver, login_page = driver_options
    customer_page = login_page.click_customer()
    customer_page.select_customer(USER)
    bank_operations = customer_page.click_login()
    amount = fibonacci_for_date()
    bank_operations.make_deposit(amount)
    bank_operations.make_withdrawal(amount)

    assert 'XYZ Bank' in driver.title
    assert bank_operations.check_balance() == 0, (
        f'Ожидаемый баланс после вывода средств: 0, '
        f'а фактический: {bank_operations.check_balance()}'
    )


@allure.description('Проверка на наличие списка транзакций')
@allure.feature('Banking Project')
@allure.story('Тест наличия выполненных транзакций')
def test_transactions(driver_options: Tuple[Remote, LoginPage]) -> None:
    """Проверка наличия списка транзакций."""

    driver, login_page = driver_options
    customer_page = login_page.click_customer()
    customer_page.select_customer(USER)
    bank_operations = customer_page.click_login()
    amount = fibonacci_for_date()
    bank_operations.make_deposit(amount)
    transaction_page = bank_operations.make_withdrawal(amount)
    time.sleep(3)

    transaction_page.open_transactions()

    transaction_elements = transaction_page.check_transactions()
    num_transactions = len(transaction_elements)
    assert num_transactions == 2, (
        f'Ожидаемое количество транзакций: 2, '
        f'а фактическое: {num_transactions}'
    )
    assert driver.current_url == TRANSACTIONS_URL, (
        f'Ожидаемый URL: {TRANSACTIONS_URL}, '
        f'а фактический: {driver.current_url}'
    )

    transaction_data = transaction_page.get_transaction_data()

    with open(
        'report_transactions.csv',
        'w',
        newline='',
        encoding='utf-8'
    ) as file:
        writer = csv.writer(file)
        writer.writerows(transaction_data)

    allure.attach.file(
        'report_transactions.csv',
        name='report_transactions',
        attachment_type=AttachmentType.CSV
    )
