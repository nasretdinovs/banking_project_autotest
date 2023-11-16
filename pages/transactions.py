import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base import BasePage
from utils import date_converter


class TransactionsPage(BasePage):
    @allure.step("Открываем раздел Transactions")
    def open_transactions(self):
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

    @allure.step("Находим все транзакции")
    def check_transactions(self):
        transactions_elements = self.driver.find_elements(
            By.CSS_SELECTOR,
            'tbody tr'
        )
        return transactions_elements

    @allure.step("Извлекаем данные обо всех транзакциях")
    def get_transaction_data(self):
        transactions_elements = self.driver.find_elements(
            By.XPATH,
            '//tbody/tr'
        )
        transactions = []
        for transaction_element in transactions_elements:
            date_string = transaction_element.find_element(
                By.XPATH,
                './td[1]'
            ).text
            date = date_converter(date_string)
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
