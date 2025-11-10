from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/7/7.html')

    dropdown_values_locator = ('css selector', 'option')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.presence_of_all_elements_located(dropdown_values_locator))

    dropdown_values = browser.find_elements(*dropdown_values_locator)
    sum_dropdown_values = sum(
        [(int(value.text.strip())) for value in dropdown_values]
    )

    input_field = browser.find_element('css selector', 'input[type="text"]')
    input_field.send_keys(sum_dropdown_values)
    send_button = browser.find_element('css selector', 'input[type="button"]')
    send_button.click()

    code_element = browser.find_element('css selector', '#result')
    code = code_element.text.strip()
    print(code)
