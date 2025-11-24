from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.6.3/index.html')

    wait = WebDriverWait(browser, 20)

    costume_locator = ('css selector', '#main-image')
    wait.until(
        ec.text_to_be_present_in_element_attribute(
            costume_locator, 'src', 'success'
        )
    )

    costume_element = browser.find_element(*costume_locator)
    costume_element.click()

    code_element_locator = ('css selector', '#password')
    wait.until(ec.visibility_of_element_located(code_element_locator))

    code_element = browser.find_element(*code_element_locator)
    code = code_element.text.strip()
    print(code)
