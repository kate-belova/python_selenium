from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.5/1/1.html')

    fields_locator = ('css selector', 'input[type="text"]')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.presence_of_all_elements_located(fields_locator))

    fields = browser.find_elements(*fields_locator)
    for field in fields:
        field.clear()

    check_button = browser.find_element('css selector', '#checkButton')
    browser.execute_script('arguments[0].scrollIntoView();', check_button)
    check_button.click()

    alert = browser.switch_to.alert
    result = alert.text
    alert.accept()
    print(result)
