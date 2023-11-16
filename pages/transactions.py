import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base import BasePage
from utils import date_converter
from typing import List
from selenium.webdriver.remote.webelement import WebElement

class TransactionsPage(BasePage):
    """Класс, представляющий страницу транзакций в приложении."""

    @allure.step('Открываем раздел Transactions')
    def open_transactions(self) -> 'TransactionsPage':
        """Метод для открытия раздела транзакций."""

        transaction_button = self.driver.find_element(
            By.CSS_SELECTOR, 'button[ng-click="transactions()"]'
        )
        transaction_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                'table.table.table-bordered.table-striped'
            ))
        )
        return self

    @allure.step('Находим все транзакции')
    def check_transactions(self) -> List[WebElement]:
        """Метод для поиска всех элементов транзакций на странице."""

        transactions_elements = self.driver.find_elements(
            By.CSS_SELECTOR,
            'tbody tr'
        )
        return transactions_elements

    @allure.step('Извлекаем данные обо всех транзакциях')
    def get_transaction_data(self) -> List[List[str]]:
        """Метод для извлечения данных обо всех транзакциях."""

        transactions_elements = self.driver.find_elements(
            By.XPATH,
            '//tbody/tr'
        )
        transactions = []
        for transaction_element in transactions_elements:
            date_raw = transaction_element.find_element(
                By.XPATH,
                './td[1]'
            ).text
            date = date_converter(date_raw)
            amount = transaction_element.find_element(
                By.XPATH,
                './td[2]'
            ).text
            transaction_type = transaction_element.find_element(
                By.XPATH,
                './td[3]'
            ).text
            transactions.append([date, amount, transaction_type])
        return transactions
