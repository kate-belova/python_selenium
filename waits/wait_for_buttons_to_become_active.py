from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.1.1/index.html')

    wait = WebDriverWait(browser, 15)

    buttons_locator = ('css selector', '.button-container button')
    wait.until(ec.presence_of_all_elements_located(buttons_locator))
    buttons = browser.find_elements(*buttons_locator)

    for button in buttons:
        wait.until(ec.element_to_be_clickable(button))
        button.click()

    password_element = browser.find_element('css selector', '#message')
    password = password_element.text.split(':')[1].strip()
    print(password)
