from browser_setup import browser
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

with browser:
    browser.get('https://parsinger.ru/selenium/6/6.3.2/index.html')
    browser.delete_all_cookies()

    password_element_locator = ('css selector', '#password')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.visibility_of_element_located(password_element_locator))

    password_element = browser.find_element(*password_element_locator)
    password = password_element.text.split()[1].strip()
    print(password)
