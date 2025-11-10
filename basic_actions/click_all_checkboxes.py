from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/4/4.html')

    checkboxes_locator = ('css selector', 'input[type="checkbox"]')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.presence_of_all_elements_located(checkboxes_locator))

    checkboxes = browser.find_elements(*checkboxes_locator)
    for checkbox in checkboxes:
        checkbox.click()

    send_button = browser.find_element('css selector', 'input[type="button"]')
    send_button.click()

    code_element = browser.find_element('css selector', '#result')
    browser.execute_script('arguments[0].scrollIntoView();', code_element)
    code = code_element.text.strip()
    print(code)
