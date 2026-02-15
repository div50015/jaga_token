import time
from selene import browser, have, be, command, query
import os
from selene import command
import json
import requests

def test_jaga_login():
    browser.open('')
    # уменьшение размера изображения в 0.8 раза
    # browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.8)"')
    # ожидание в течение 10 секунд 3х реклпмных банеров и их удаление (вторая строка)
    # browser.all('[id^google_ads][id$=container__]').with_(timeout=10).wait_until(have.size_less_than_or_equal(3))
    # browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    time.sleep(1)
    # cookies = browser.driver.get_cookies()
    # with open('cookies1.json', 'w') as file:
    #     json.dump(cookies, file)
    browser.element('#email').type('igor.degtyarenko@south.rt.ru')
    browser.element('#password').type('Bc:$hsn8KY')
    browser.element('#kc-login').click()
    time.sleep(1)
    # print(browser.driver.get_cookies())
    # print(browser.driver.get_cookie('accessToken'))


    token = browser.driver.execute_script("return window.localStorage.getItem('jaga.accessToken');")
    print('token=',token)
    # time.sleep(1)

    # jsession = browser.driver.get_cookie('JSESSIONID')
    # print('  ')
    # print('JSESSION=',jsession['value'])


    browser.open('https://test2-jaga.lukit.ru/esmp-integrator/swagger-ui/index.html')
    time.sleep(1)

    jsession = browser.driver.get_cookie('JSESSIONID')['value']
    print('  ')
    print('JSESSION=',jsession)
    time.sleep(1)

    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': f'Bearer {token}',
        'cache-control': 'no-cache',
        # 'Cookie' : f'JSESSIONID={jsession}',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://test2-jaga.lukit.ru/esmp-integrator/swagger-ui/index.html',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin'
    }
    cookies = {'JSESSIONID': f'{jsession}'}


    response = requests.get('https://test2-jaga.lukit.ru/esmp-integrator/jaga/project/serviceList', headers=headers, cookies=cookies)
    print('  ')
    print('response=',response)
    time.sleep(1)
    time.sleep(1)






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