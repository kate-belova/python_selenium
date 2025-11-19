from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/7/7.5/index.html')

    container = browser.find_element('css selector', '#container')
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

    numbers = []

    cards_locator = ('css selector', '.card')
    wait.until(ec.presence_of_all_elements_located(cards_locator))
    cards = container.find_elements(*cards_locator)

    for card in cards:
        browser.execute_script(
            'return arguments[0].scrollIntoView(true);', card
        )
        like_button = card.find_element('css selector', '.like-btn')
        like_button.click()

        number = card.find_element('css selector', '.big-number')
        wait.until(ec.visibility_of(number))
        numbers.append(int(number.text))

    print(sum(numbers))
