from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.4.3/index.html')

    right_way_button = browser.find_element(
        'xpath', '//a[text()="Правильный путь"]'
    )
    right_way_button.click()

    wait = WebDriverWait(browser, 10)
    wait.until(
        ec.url_to_be(
            'https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure'
        )
    )

    password_element = browser.find_element('css selector', '#password')
    password = password_element.text.strip()
    print(password)
