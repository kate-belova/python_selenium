from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.1/index.html')

    parent_element_locator = ('css selector', '#parent_id')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.presence_of_element_located(parent_element_locator))

    child_elements = browser.find_elements('css selector', '.child_class')
    first_child_element = child_elements[0]

    first_child_element.click()
    password = first_child_element.get_attribute('password')
    print(password)
