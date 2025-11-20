from browser_setup import browser
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

with browser:
    browser.get('https://parsinger.ru/selenium/5.8/1/index.html')

    buttons_locator = ('css selector', 'input')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.presence_of_all_elements_located(buttons_locator))

    buttons = browser.find_elements(*buttons_locator)
    for button in buttons:
        button.click()
        alert = browser.switch_to.alert
        alert.accept()

        code_element = browser.find_element('css selector', 'p#result')
        code = code_element.text.strip()
        if code:
            print(code)
            break
