from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/infiniti_scroll_2/')

    container = browser.find_element('css selector', '#scroll-container')
    last_height = browser.execute_script(
        'return arguments[0].scrollHeight', container
    )

    wait = WebDriverWait(browser, 2)

    while True:
        browser.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollHeight', container
        )

        try:
            wait.until(
                lambda _: browser.execute_script(
                    'return arguments[0].scrollHeight', container
                )
                > last_height
            )
            last_height = browser.execute_script(
                'return arguments[0].scrollHeight', container
            )
        except TimeoutException:
            break

    p_elements_locator = ('css selector', 'p')
    wait.until(ec.presence_of_all_elements_located(p_elements_locator))
    p_elements = browser.find_elements(*p_elements_locator)

    result = sum(
        [int(p.text.strip()) for p in p_elements if p.text.strip().isdigit()]
    )
    print(result)
