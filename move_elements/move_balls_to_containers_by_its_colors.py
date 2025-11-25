from selenium.webdriver import ActionChains

from browser_setup import browser
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

with browser:
    browser.get('https://parsinger.ru/selenium/5.10/4/index.html')

    balls_locator = ('css selector', '.ball_color')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.presence_of_all_elements_located(balls_locator))

    balls = browser.find_elements('css selector', '.ball_color')
    for ball in balls:
        color = (
            ball.get_attribute('class').split('_ball')[0].split()[1].strip()
        )
        basket = browser.find_element('css selector', f'.basket_color.{color}')

        actions = ActionChains(browser)
        actions.drag_and_drop(ball, basket).perform()

    code_locator = ('css selector', '.message')
    wait.until(ec.visibility_of_element_located(code_locator))

    code_element = browser.find_element(*code_locator)
    code = code_element.text.strip()
    print(code)
