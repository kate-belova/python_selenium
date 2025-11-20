from browser_setup import browser
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

with browser:
    browser.get('https://parsinger.ru/selenium/5.8/3/index.html')

    pins_locator = ('css selector', 'span.pin')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.presence_of_all_elements_located(pins_locator))

    pins = browser.find_elements(*pins_locator)
    check_button = browser.find_element('css selector', '#check')

    for pin in pins:
        pin_code = pin.text.strip()

        wait.until(ec.element_to_be_clickable(check_button))
        check_button.click()

        alert = browser.switch_to.alert
        alert.send_keys(pin_code)
        alert.accept()

        result = browser.find_element('css selector', '#result')
        code = result.text.strip()
        if code != 'Неверный пин-код':
            print(code)
            break
