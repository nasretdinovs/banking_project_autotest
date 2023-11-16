import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base import BasePage
from pages.transactions import TransactionsPage


class Banking(BasePage):
    """Класс, представляющий страницу банковских операций."""

    @allure.step('Вносим средства на счёт')
    def make_deposit(self, amount: int) -> 'Banking':
        """Метод для внесения средств на счёт."""

        deposit_button = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[ng-click="deposit()"]'
        )
        deposit_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, 'div.form-group > label'),
                'Amount to be Deposited :'
            )
        )
        deposit_input = self.driver.find_element(
            By.CSS_SELECTOR,
            'input[ng-model="amount"]'
        )
        deposit_input.send_keys(str(amount))

        deposit_button = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[type="submit"]'
        )
        deposit_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, 'span.error.ng-binding'),
                'Deposit Successful'
            )
        )
        return self

    @allure.step('Списываем средства со счёта')
    def make_withdrawal(self, amount: int) -> 'TransactionsPage':
        """Метод для списания средств со счёта."""

        withdrawal_button = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[ng-click="withdrawl()"]'
        )
        withdrawal_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, 'div.form-group > label'),
                'Amount to be Withdrawn :'
            )
        )

        withdrawal_input = self.driver.find_element(
            By.CSS_SELECTOR,
            'input[ng-model="amount"]'
        )
        withdrawal_input.send_keys(str(amount))

        withdrawal_button = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[type="submit"]'
        )
        withdrawal_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, 'span.error.ng-binding'),
                'Transaction successful'
            )
        )
        return TransactionsPage(self.driver)

    @allure.step('Проверяем баланс')
    def check_balance(self) -> int:
        """Метод для проверки баланса на счёте."""

        balance_element = self.driver.find_element(
            By.XPATH,
            '//div[@ng-hide="noAccount"]/strong[2]'
        )
        balance = int(balance_element.text)
        return balance
