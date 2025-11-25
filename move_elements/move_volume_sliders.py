from selenium.webdriver import Keys

from browser_setup import browser
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

with browser:
    browser.get('https://parsinger.ru/selenium/5.10/6/index.html')

    wait = WebDriverWait(browser, 10)

    sliders_locator = ('css selector', '.volume-slider')
    target_values_locator = ('css selector', '.target-value')

    wait.until(
        ec.all_of(
            ec.visibility_of_all_elements_located(sliders_locator),
            ec.visibility_of_all_elements_located(target_values_locator),
        )
    )

    sliders = browser.find_elements(*sliders_locator)
    target_values = browser.find_elements(*target_values_locator)

    for slider, target_value in zip(sliders, target_values):
        current_value = int(slider.get_attribute('value'))
        target_value = int(target_value.text)

        while current_value != target_value:
            if current_value < target_value:
                slider.send_keys(Keys.ARROW_RIGHT)
                current_value += 1
            elif current_value > target_value:
                slider.send_keys(Keys.ARROW_LEFT)
                current_value -= 1

    code_locator = ('css selector', '#message')
    wait.until(ec.visibility_of_element_located(code_locator))

    code_element = browser.find_element('css selector', '#message')
    code = code_element.text.strip()
    print(code)
