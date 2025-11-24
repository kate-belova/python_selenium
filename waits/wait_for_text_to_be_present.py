from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.6.1/index.html')

    usd_rate_locator = ('css selector', '#usd-rate')

    wait = WebDriverWait(browser, 40)
    wait.until(ec.text_to_be_present_in_element(usd_rate_locator, '75.50 ₽'))

    secret_code_element_locator = ('css selector', '#secret-code')
    wait.until(ec.visibility_of_element_located(secret_code_element_locator))

    secret_code_element = browser.find_element(*secret_code_element_locator)
    secret_code = secret_code_element.text.strip()
    print(secret_code)
