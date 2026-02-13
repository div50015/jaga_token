import time
from selene import browser, have, be, command, query
import os
from selene import command

def test_jaga_login():
    browser.open('')
    # уменьшение размера изображения в 0.8 раза
    # browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.8)"')
    # ожидание в течение 10 секунд 3х реклпмных банеров и их удаление (вторая строка)
    # browser.all('[id^google_ads][id$=container__]').with_(timeout=10).wait_until(have.size_less_than_or_equal(3))
    # browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    # time.sleep(1)
    browser.element('#email').type('igor.degtyarenko@south.rt.ru')
    # time.sleep(1)
    browser.element('#password').type('Bc:$hsn8KY')
    # time.sleep(1)
    browser.element('#kc-login').click()
    time.sleep(10)
    print(browser.driver.get_cookies())
    print(browser.driver.get_cookie('accessToken'))
    time.sleep(10)
    # browser.element('#userNumber').type('79287777777')
    # browser.element('#dateOfBirthInput').click()
    # browser.element('.react-datepicker__year-select').type('1999')
    # browser.element('.react-datepicker__month-select').type('August')
    # browser.element('.react-datepicker__day--009').click()
    # browser.element('#subjectsInput').type('Biology').press_enter()
    # browser.element('[for="hobbies-checkbox-1"]').click()
    # browser.element("#uploadPicture").send_keys(os.path.abspath('files/ball.jpg'))
    # browser.element('#currentAddress').type('Russia Moscow')
    # browser.element('#react-select-3-input').type('NCR').press_enter()
    # browser.element('#react-select-4-input').type('Noida').press_enter()
    # browser.element('#submit').click()
    # time.sleep(10)
    # browser.element('.table').all('tr td:nth-child(2)').should(have.exact_texts(
    #     'Ivan Petrov',
    #     'petrov@mail.ru',
    #     'Male',
    #     '7928777777',
    #     '09 August,1999',
    #     'Biology',
    #     'Sports',
    #     'ball.jpg',
    #     'Russia Moscow',
    #     'NCR Noida'))