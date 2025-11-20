from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/window_size/1/')

    window_size = browser.get_window_size()
    width_border = window_size['width'] - browser.execute_script(
        'return window.innerWidth'
    )
    height_border = window_size['height'] - browser.execute_script(
        'return window.innerHeight'
    )

    browser.set_window_size(555 + width_border, 555 + height_border)

    wait = WebDriverWait(browser, 5)

    code_element = browser.find_element('css selector', '#result')
    wait.until(lambda _: bool(code_element.text.strip()))
    code = code_element.text.strip()
    print(code)
