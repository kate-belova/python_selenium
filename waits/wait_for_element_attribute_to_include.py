from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.6.4/index.html')

    booking_number_locator = ('css selector', '#booking-number')

    wait = WebDriverWait(browser, 20)
    wait.until(
        ec.element_attribute_to_include(booking_number_locator, 'confirmed')
    )

    booking_number_element = browser.find_element(*booking_number_locator)
    booking_number = booking_number_element.text.strip()

    booking_input = browser.find_element('css selector', '#booking-input')
    booking_input.send_keys(booking_number)

    check_status_button = browser.find_element('css selector', '#check-button')
    check_status_button.click()

    password_element = browser.find_element('css selector', '.password-value')
    browser.execute_script(
        'return arguments[0].scrollIntoView(true);', password_element
    )

    password = password_element.text.strip()
    print(password)
