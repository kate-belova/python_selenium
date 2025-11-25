from selenium.webdriver import ActionChains

from browser_setup import browser
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

with browser:
    browser.get('https://parsinger.ru/draganddrop/2/index.html')

    ball = browser.find_element('css selector', '#draggable')
    blocks_locator = ('css selector', '.box')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.presence_of_all_elements_located(blocks_locator))

    blocks = browser.find_elements(*blocks_locator)
    action = ActionChains(browser)
    for block in blocks:
        action.drag_and_drop(ball, block).perform()

    token_element = browser.find_element('css selector', '#message')
    token = token_element.text.strip()
    print(token)
