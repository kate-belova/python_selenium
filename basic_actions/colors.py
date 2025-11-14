from browser_setup import browser
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

with browser:
    browser.get('https://parsinger.ru/selenium/5.5/5/1.html')

    containers_locator = ('css selector', '#main-container>div')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.presence_of_all_elements_located(containers_locator))

    containers = browser.find_elements(*containers_locator)

    for container in containers:
        color_code_element = container.find_element('css selector', 'span')
        color_code = color_code_element.text.strip()

        color_dropdown = container.find_element('css selector', 'select')
        color_dropdown.send_keys(color_code)

        color_button = container.find_element(
            'css selector', f'button[data-hex="{color_code}"]'
        )
        color_button.click()

        checkbox = container.find_element(
            'css selector', 'input[type="checkbox"]'
        )
        checkbox.click()

        text_field = container.find_element(
            'css selector', 'input[type="text"]'
        )
        text_field.send_keys(color_code)

        check_button = container.find_element(
            'xpath', '//button[text()="Проверить"]'
        )
        check_button.click()

    check_all_elements_button = browser.find_element(
        'xpath', '//button[text()="Проверить все элементы"]'
    )
    browser.execute_script(
        'arguments[0].scrollIntoView();', check_all_elements_button
    )
    check_all_elements_button.click()

    alert = browser.switch_to.alert
    result = alert.text
    alert.accept()
    print(result)
