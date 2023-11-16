![Python](https://img.shields.io/badge/Python-3.11.5-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.15.2-brightgreen)
![Allure](https://img.shields.io/badge/Allure-reporting-brightgreen)

# Тестирование XYZ Bank
Тестирование сайта с помощью Selenium


## Настройка Selenium Grid

1. Запустите Selenium Grid Hub из корневой папки проекта командой:
    ```bash
    java -jar grid/selenium-server-4.15.0.jar hub
    ```

2. Запустите Selenium Grid Node из корневой папки проекта командой:
    ```bash
    java -jar grid/selenium-server-4.15.0.jar node --detect-drivers true --grid-url http://192.168.1.136:4444
    ```
URL адрес будет отличаться, необходимо подставить свой из терминала, 
где запустили Selenium Grid Hub.
Также этот URL необходимо внести в SELENIUM_SERVER_URL в constants.py

## Установка тестов

1. Скачайте репозиторий:
    ```bash
    git clone https://github.com/nasretdinovs/banking_project_autotest.git
    ```

2. Перейдите в папку с проектом:
    ```bash
    cd banking_project_autotest
    ```

3. Установите необходимые зависимости:
    ```bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

## Запуск тестов

1. Запустите тесты с ключем --alluredir для сохранения результатов 
в формате, понимаемом Allure:
    ```bash
    pytest --alluredir=./allure_results test_main.py
    ```

2. Сгенерируйте отчет Allure с помощью следующей команды:
    ```bash
    allure serve ./allure_results
    ```
