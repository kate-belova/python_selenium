from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.4.2/index.html')

    start_button = browser.find_element('css selector', '#startButton')
    start_button.click()

    wait = WebDriverWait(browser, 5)

    numbers = []
    while not 'index_2' in browser.current_url:
        try:
            if wait.until(ec.url_matches(
                # fmt: off
                r'^https://parsinger\.ru/selenium/9/9\.4\.2/ok/ok_\d+\.html$')
            ):
                # fmt: on
                number_element =browser.find_element(
                    'css selector', '.number')
                number = number_element.text
                numbers.append(int(number))

                wait.until(ec.staleness_of(number_element))
        except TimeoutException:
            break

    input_field = browser.find_element('css selector', '#sumInput')
    input_field.send_keys(sum(numbers))

    check_button = browser.find_element('css selector', '#checkButton')
    check_button.click()

    password_element = browser.find_element('css selector', '#result')
    password = password_element.text.split(':')[1].strip()
    print(password)
