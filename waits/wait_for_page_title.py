from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.2.1/index.html')

    initiate_scan_button = browser.find_element('css selector', '#startScan')
    initiate_scan_button.click()

    wait = WebDriverWait(browser, 25)
    wait.until(ec.title_is('Access Granted'))

    password_element = browser.find_element('css selector', '#passwordValue')
    password = password_element.text.split(':')[1].strip()
    print(password)
