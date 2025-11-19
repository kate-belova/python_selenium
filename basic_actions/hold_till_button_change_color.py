from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver import ActionChains

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.7/5/index.html')

    buttons = browser.find_elements('css selector', 'button')
    wait = WebDriverWait(browser, 5)
    actions = ActionChains(browser)

    for button in buttons:
        browser.execute_script(
            'return arguments[0].scrollIntoView(true);', button
        )
        wait.until(ec.element_to_be_clickable(button))

        value = button.get_attribute('value')
        actions.click_and_hold(button).pause(float(value)).release(
            button
        ).perform()

    alert = browser.switch_to.alert
    result = alert.text.strip()
    alert.accept()
    print(result)
