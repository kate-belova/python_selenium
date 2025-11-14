from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/6/6.2/index.html')

    go_to_next_page_button_locator = ('css selector', 'a[href]')

    wait = WebDriverWait(browser, 5)

    wait.until(ec.element_to_be_clickable(go_to_next_page_button_locator))
    go_to_next_page_button = browser.find_element(
        *go_to_next_page_button_locator
    )
    go_to_next_page_button.click()

    wait.until(ec.element_to_be_clickable(go_to_next_page_button_locator))
    go_to_next_page_button = browser.find_element(
        *go_to_next_page_button_locator
    )
    go_to_next_page_button.click()

    browser.back()
    browser.back()

    show_code_button = browser.find_element('css selector', '#getPasswordBtn')
    show_code_button.click()

    alert = browser.switch_to.alert
    code = alert.text.split(':')[1].strip()
    alert.accept()
    print(code)
