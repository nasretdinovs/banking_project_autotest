import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from pages.base import BasePage


class CustomerPage(BasePage):
    @allure.step("Выбираем пользователя из списка")
    def select_customer(self, customer_name):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, 'label'),
                'Your Name :'
            )
        )
        select = Select(self.driver.find_element(By.ID, 'userSelect'))
        select.select_by_visible_text(customer_name)
        return self

    @allure.step("Нажимаем кнопку Login")
    def click_login(self):
        login_button = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[type="submit"]'
        )
        login_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'button[ng-click="deposit()"]')
            )
        )
        return self
