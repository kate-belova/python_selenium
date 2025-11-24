from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/expectations/6/index.html')

    create_button_locator = ('css selector', '#btn')

    wait = WebDriverWait(browser, 20)
    wait.until(ec.element_to_be_clickable(create_button_locator))

    button = browser.find_element(*create_button_locator)
    button.click()

    num_element_locator = ('css selector', '.BMH21YY')
    wait.until(ec.presence_of_element_located(num_element_locator))

    num_element = browser.find_element(*num_element_locator)
    browser.execute_script(
        'return arguments[0].scrollIntoView(true);', num_element
    )

    number = num_element.text
    print(number)
