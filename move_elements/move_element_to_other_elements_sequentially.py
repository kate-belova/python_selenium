from selenium.webdriver import ActionChains

from browser_setup import browser
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

with browser:
    browser.get('https://parsinger.ru/draganddrop/3/index.html')

    square = browser.find_element('css selector', '#block1')
    points = browser.find_elements('css selector', '.controlPoint')

    actions = ActionChains(browser)

    actions.click_and_hold(square)
    for point in points:
        actions.move_to_element(point)
    actions.move_to_element(points[0]).perform()

    token_locator = ('css selector', '#message')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.visibility_of_element_located(token_locator))

    token_element = browser.find_element(*token_locator)
    token = token_element.text.strip()
    print(token)
