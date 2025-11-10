from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.3/index.html')

    links_locator = ('css selector', 'a')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.presence_of_all_elements_located(links_locator))

    links = browser.find_elements(*links_locator)

    stormtrooper_attributes = [
        link.get_attribute('stormtrooper') for link in links
    ]
    sum_digital_stormtroopers = sum(
        int(attribute)
        for attribute in stormtrooper_attributes
        if attribute.isdigit()
    )

    input_field = browser.find_element('css selector', '#inputNumber')
    input_field.send_keys(sum_digital_stormtroopers)

    check_button = browser.find_element('css selector', '#checkBtn')
    check_button.click()

    code_element = browser.find_element('css selector', '#feedbackMessage')
    code = code_element.text.split(':')[1].strip()
    print(code)
