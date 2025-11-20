from browser_setup import browser
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

with browser:
    browser.get('https://parsinger.ru/selenium/8/8.3.1/index.html')

    alert_button = browser.find_element('css selector', '#alertButton')
    alert_button.click()
    browser.switch_to.alert.accept()

    prompt_button = browser.find_element('css selector', '#promptButton')
    prompt_button.click()
    prompt = browser.switch_to.alert
    prompt.send_keys('Alert')
    prompt.accept()

    confirm_button = browser.find_element('css selector', '#confirmButton')
    confirm_button.click()
    browser.switch_to.alert.accept()

    password_locator = ('css selector', '#secretKey')
    wait = WebDriverWait(browser, 5)
    wait.until(ec.visibility_of_element_located(password_locator))

    password_element = browser.find_element(*password_locator)
    password = password_element.text.split()[1].strip()
    print(password)
