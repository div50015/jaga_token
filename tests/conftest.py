import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://test2-jaga.lukit.ru/'
    browser.config.timeout = 10.0
    browser.config.window_width = 1200
    browser.config.window_height = 800

#    browser.config.type_by_js = True
    # закрытие сообщения о том что браузер запущен в отладочном режиме
    driver_options = webdriver.ChromeOptions()
    driver_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver_options.add_argument('--headless=new')
    browser.config.driver_options = driver_options

    yield

    browser.quit()