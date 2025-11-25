from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.10/8/index.html')
    balls = [
        browser.find_element('css selector', f'#piece_{i}')
        for i in range(100, 801, 100)
    ]
    containers = [
        browser.find_element('css selector', f'#range_{i}')
        for i in range(100, 801, 100)
    ]

    actions = ActionChains(browser)
    for ball, container in zip(balls, containers):
        actions.drag_and_drop(ball, container).perform()

    wait = WebDriverWait(browser, 5)

    code_locator = ('css selector', '#message')
    wait.until(ec.visibility_of_element_located(code_locator))

    code_element = browser.find_element(*code_locator)
    code = code_element.text.strip()
    print(code)
