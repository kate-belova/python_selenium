from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.6.2/index.html')

    ask_jaskier_button = browser.find_element('css selector', '#ask-jaskier')
    ask_jaskier_button.click()

    wait = WebDriverWait(browser, 15)

    recipe_field_locator = ('css selector', '#recipe_field')
    wait.until(
        ec.text_to_be_present_in_element_value(
            recipe_field_locator, 'Селениумий'
        )
    )

    password_element_locator = ('css selector', '#password')
    wait.until(ec.visibility_of_element_located(password_element_locator))

    password_element = browser.find_element(*password_element_locator)
    browser.execute_script(
        'return arguments[0].scrollIntoView(true);', password_element
    )

    password = password_element.text.strip()
    print(password)
