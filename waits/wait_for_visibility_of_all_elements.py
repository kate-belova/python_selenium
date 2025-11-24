from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/9/9.5.3/index.html')

    load_projects_button = browser.find_element(
        'css selector', '#showProducts'
    )
    load_projects_button.click()

    products_locator = ('css selector', '.product')

    wait = WebDriverWait(browser, 10)
    wait.until(ec.visibility_of_all_elements_located(products_locator))

    products = browser.find_element(*products_locator)

    prices_elements = browser.find_elements('css selector', '.price')
    prices_lst = []
    for price_el in prices_elements:
        browser.execute_script(
            'return arguments[0].scrollIntoView(true);', price_el
        )
        price = int(price_el.text.strip('$'))
        prices_lst.append(price)

    input_field = browser.find_element('css selector', '#sumInput')
    browser.execute_script(
        'return arguments[0].scrollIntoView(true);', input_field
    )
    input_field.send_keys(sum(prices_lst))

    check_button = browser.find_element('css selector', '#checkSum')
    check_button.click()

    password_element_locator = ('css selector', '#secretMessage')
    wait.until(ec.visibility_of_element_located(password_element_locator))

    password_element = browser.find_element(*password_element_locator)
    password = password_element.text
    print(password)
