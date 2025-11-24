from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.9/7/index.html')

    wait = WebDriverWait(browser, 10)

    checkboxes_locator = ('css selector', 'input[type="checkbox"]')
    buttons_locator = ('css selector', 'button')
    wait.until(
        ec.all_of(
            ec.presence_of_all_elements_located(checkboxes_locator),
            ec.presence_of_all_elements_located(buttons_locator),
        )
    )

    checkboxes = browser.find_elements(*checkboxes_locator)
    buttons = browser.find_elements(*buttons_locator)

    for checkbox, button in zip(checkboxes, buttons):
        browser.execute_script("arguments[0].scrollIntoView();", checkbox)
        wait.until(ec.element_to_be_selected(checkbox))
        button.click()

    code_element_locator = ('css selector', '#result')
    wait.until(ec.visibility_of_element_located(code_element_locator))

    code_element = browser.find_element(*code_element_locator)
    code = code_element.text.strip()
    print(code)
