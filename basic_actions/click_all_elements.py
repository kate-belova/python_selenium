from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.2/index.html')

    blocks_locator = ('css selector', '.block')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.presence_of_all_elements_located(blocks_locator))

    blocks = browser.find_elements(*blocks_locator)
    for block in blocks:
        click_button = block.find_element('css selector', 'button')
        click_button.click()

    password_element = browser.find_element('css selector', 'password')
    password = password_element.text.strip()
    print(password)
