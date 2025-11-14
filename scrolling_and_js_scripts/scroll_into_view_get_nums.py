from browser_setup import browser
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

with browser:
    browser.get('https://parsinger.ru/scroll/4/index.html')

    buttons_locator = ('css selector', 'button.btn')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.presence_of_all_elements_located(buttons_locator))

    buttons = browser.find_elements(*buttons_locator)
    numbers = []

    for button in buttons:
        browser.execute_script(
            'return arguments[0].scrollIntoView(true);', button
        )
        button.click()
        num_element = browser.find_element('css selector', 'p#result')
        num = int(num_element.text.strip())
        numbers.append(num)

    print(sum(numbers))
