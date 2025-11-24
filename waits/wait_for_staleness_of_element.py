from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.7.2/index.html')

    search_input = browser.find_element('css selector', 'input.search-box')
    search_input.send_keys('Selenium')

    search_button = browser.find_element('css selector', '#search-button')
    search_button.click()

    old_result = browser.find_element('css selector', '#old-result')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.staleness_of(old_result))

    show_secret_button = browser.find_element('css selector', '#secret-button')
    show_secret_button.click()

    password_element = browser.find_element('css selector', '#result')
    password = password_element.text.strip()
    print(password)
