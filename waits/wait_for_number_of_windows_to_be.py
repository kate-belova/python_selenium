from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.7.3/index.html')

    summon_page_button = browser.find_element('css selector', '#summonBtn')
    summon_page_button.click()

    wait = WebDriverWait(browser, 10)
    wait.until(ec.number_of_windows_to_be(5))

    windows = browser.window_handles
    browser.switch_to.window(windows[0])

    show_password_button = browser.find_element('css selector', '#passwordBtn')
    show_password_button.click()

    wait.until(ec.alert_is_present())
    alert = browser.switch_to.alert

    password = alert.text.split(':')[1].strip()
    alert.accept()
    print(password)
