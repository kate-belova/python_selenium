from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/infiniti_scroll_3/')
    numbers = []
    wait = WebDriverWait(browser, 2)

    for i in range(1, 6):
        container = browser.find_element(
            'css selector', f'#scroll-container_{i}'
        )

        last_height = browser.execute_script(
            'return arguments[0].scrollHeight', container
        )

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

        spans = container.find_elements('css selector', 'span')
        nums = [
            int(span.text.strip()) for span in spans if span.text.isdigit()
        ]
        numbers.extend(nums)

    print(sum(numbers))
