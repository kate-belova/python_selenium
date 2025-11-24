from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.3.1/index.html')

    start_button_locator = ('css selector', '#startButton')
    dynamic_button_locator = ('css selector', '#dynamicButton')

    wait = WebDriverWait(browser, 5)

    wait.until(ec.presence_of_element_located(start_button_locator))
    start_button = browser.find_element('css selector', '#startButton')
    wait.until(ec.element_to_be_clickable(start_button))
    start_button.click()

    for _ in range(5):
        wait.until(ec.presence_of_element_located(dynamic_button_locator))
        dynamic_button = browser.find_element(*dynamic_button_locator)

        wait.until(ec.element_to_be_clickable(dynamic_button))
        dynamic_button.click()

    password_element = browser.find_element('css selector', '#secretPassword')
    password = password_element.text.split()[1].strip()
    print(password)
