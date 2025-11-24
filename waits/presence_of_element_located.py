from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.5.1/index.html')

    order_locator = ('css selector', '#order-number')

    wait = WebDriverWait(browser, 15)
    wait.until(ec.presence_of_element_located(order_locator))

    order = browser.find_element(*order_locator)
    code = order.text.strip()
    print(code)
