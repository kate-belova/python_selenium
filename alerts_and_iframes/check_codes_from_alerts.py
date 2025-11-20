from browser_setup import browser
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

with browser:
    browser.get('https://parsinger.ru/selenium/5.8/2/index.html')

    buttons = browser.find_elements('css selector', 'input.buttons')
    input_field = browser.find_element('css selector', '#input')
    check_button = browser.find_element('css selector', '#check')

    wait = WebDriverWait(browser, 5)

    for button in buttons:
        wait.until(ec.element_to_be_clickable(button))
        button.click()

        alert = browser.switch_to.alert
        alert_text = alert.text.strip()
        alert.accept()

        input_field.send_keys(alert_text)
        check_button.click()

        code_element = browser.find_element('css selector', '#result')
        code = code_element.text.strip()
        if code != 'Неверный пин-код':
            print(code)
            break
