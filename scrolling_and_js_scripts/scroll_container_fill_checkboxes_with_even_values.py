from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.7/4/index.html')

    container = browser.find_element('css selector', '#main_container')
    last_height = browser.execute_script(
        'return arguments[0].scrollHeight', container
    )

    wait = WebDriverWait(browser, 2)

    while True:
        browser.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollHeight', container
        )

        try:
            wait.until(
                lambda _: browser.execute_script(
                    'return arguments[0].scrollHeight', container
                )
                > last_height
            )
            last_height = browser.execute_script(
                'return arguments[0].scrollHeight', container
            )
        except TimeoutException:
            break

    checkboxes_locator = ('css selector', '.child_container input')
    wait.until(ec.presence_of_all_elements_located(checkboxes_locator))
    checkboxes = browser.find_elements(*checkboxes_locator)

    for checkbox in checkboxes:
        value = int(checkbox.get_attribute('value'))
        if value % 2 == 0:
            checkbox.click()

    button = browser.find_element('css selector', '.alert_button')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()

    alert = browser.switch_to.alert
    result = alert.text
    alert.accept()
    print(result)
