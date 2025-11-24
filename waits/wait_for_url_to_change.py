from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.4.4/index.html')

    start_button = browser.find_element('css selector', '.btn')
    start_button.click()

    current_url = browser.current_url
    wait = WebDriverWait(browser, 5)
    wait.until(ec.url_changes(current_url))

    password_element = browser.find_element('css selector', '#password')
    password = password_element.text.split(':')[1].strip()
    print(password)
