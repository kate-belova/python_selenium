from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.9/6/index.html')

    checkbox = browser.find_element('css selector', '#myCheckbox')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.element_to_be_selected(checkbox))

    check_button = browser.find_element('css selector', 'button')
    check_button.click()

    code_element = browser.find_element('css selector', '#result')
    code = code_element.text.strip()
    print(code)
