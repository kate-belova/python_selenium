from faker import Faker
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

random_generator = Faker()

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.7.1/index.html')

    address_input = browser.find_element('css selector', '#address')
    address_input.send_keys(random_generator.address())

    dropdown = Select(browser.find_element('css selector', 'select'))
    dropdown.select_by_value('card')

    confirm_order_button = browser.find_element(
        'css selector', '#submit-order'
    )
    confirm_order_button.click()

    wait = WebDriverWait(browser, 10)

    spinner_locator = ('css selector', '#spinner')
    wait.until(ec.invisibility_of_element_located(spinner_locator))

    confirm_address_button_locator = ('css selector', '#confirm-address')
    wait.until(ec.element_to_be_clickable(confirm_address_button_locator))
    confirm_address_button = browser.find_element(
        *confirm_address_button_locator
    )
    confirm_address_button.click()

    modal_window_locator = ('css selector', '.modal')
    wait.until(ec.invisibility_of_element_located(modal_window_locator))

    get_code_button_locator = ('css selector', '#get-code')
    wait.until(ec.element_to_be_clickable(get_code_button_locator))
    get_code_button = browser.find_element(*get_code_button_locator)
    get_code_button.click()

    password_element = browser.find_element('css selector', '#result')
    browser.execute_script(
        'return arguments[0].scrollIntoView(true);', password_element
    )
    password = password_element.text.strip()
    print(password)
