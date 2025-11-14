from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.5/3/1.html')

    pairs_of_elements_locator = ('css selector', '.parent')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.presence_of_element_located(pairs_of_elements_locator))

    pairs_of_elements = browser.find_elements(*pairs_of_elements_locator)
    num_locator = ('css selector', 'textarea')
    checkbox_locator = ('css selector', 'input[type="checkbox"]')

    result = sum(
        [
            int(pair.find_element(*num_locator).get_attribute('value'))
            for pair in pairs_of_elements
            if pair.find_element(*checkbox_locator).is_selected()
        ]
    )
    print(result)
