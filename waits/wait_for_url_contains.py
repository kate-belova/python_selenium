from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get(
        'https://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html'
    )
    while True:
        search_button = browser.find_element('css selector', '#searchLink')
        search_button.click()

        wait = WebDriverWait(browser, 5)

        try:
            wait.until(ec.url_contains('qLChv49'))
            check_button = browser.find_element('css selector', '#checkButton')
            check_button.click()

            password_element = browser.find_element('css selector', 'p')
            password = password_element.text.split(':')[1].strip()
            print(password)
            break
        except TimeoutException:
            continue
