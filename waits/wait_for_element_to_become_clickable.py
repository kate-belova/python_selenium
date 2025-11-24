from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.9/2/index.html')

    magic_block_locator = ('css selector', '#qQm9y1rk')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.element_to_be_clickable(magic_block_locator))

    magic_block = browser.find_element(*magic_block_locator)
    magic_block.click()

    alert = browser.switch_to.alert
    code = alert.text
    alert.accept()
    print(code)
