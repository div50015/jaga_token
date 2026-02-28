import time
from selene import browser, have, be, command, query


def get_login_token():
    browser.open('')
    # time.sleep(1)
    browser.element('#email').type('igor.degtyarenko@south.rt.ru')
    browser.element('#password').type('Bc:$hsn8KY')
    browser.element('#kc-login').click()
    time.sleep(2)
    jwt_token = browser.driver.execute_script("return window.localStorage.getItem('jaga.accessToken');")
    jwt_token = jwt_token.strip('"\'')
    return jwt_token

