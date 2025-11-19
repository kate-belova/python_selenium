from browser_setup import browser
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

with browser:
    browser.get('https://parsinger.ru/scroll/2/index.html')

    items_locator = ('css selector', 'div.item')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.presence_of_all_elements_located(items_locator))

    items = browser.find_elements(*items_locator)

    numbers = []
    for item in items:
        checkbox = item.find_element('css selector', 'input[type="checkbox"]')
        checkbox.click()
        span_element = item.find_element('css selector', 'span')
        span_text = span_element.text.strip()
        if span_text.isdigit():
            numbers.append(int(span_text))

    print(sum(numbers))
