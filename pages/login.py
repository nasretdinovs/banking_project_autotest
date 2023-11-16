import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from constants import LOGIN_URL
from pages.base import BasePage
from pages.customer import CustomerPage


class LoginPage(BasePage):
    """Класс, представляющий страницу входа в приложение."""

    @allure.step('Открываем страницу входа')
    def open_page(self) -> 'LoginPage':
        """Метод для открытия страницы входа."""
        self.driver.get(LOGIN_URL)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'button[ng-click="customer()"]')
            )
        )
        return self

    @allure.step('Нажимаем кнопку Customer Login')
    def click_customer(self) -> 'CustomerPage':
        """Метод для нажатия кнопки "Customer Login"."""
        customer_button = self.driver.find_element(
            By.CSS_SELECTOR, 'button[ng-click="customer()"]'
        )
        customer_button.click()
        return CustomerPage(self.driver)
