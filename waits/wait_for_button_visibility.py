from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.5.2/index.html')

    show_pass_button_locator = ('css selector', '#ghost-button')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.visibility_of_element_located(show_pass_button_locator))

    show_pass_button = browser.find_element(*show_pass_button_locator)
    show_pass_button.click()

    password_element = browser.find_element(
        'css selector', '#password-display'
    )
    password = password_element.text.split()[1].strip()
    print(password)
