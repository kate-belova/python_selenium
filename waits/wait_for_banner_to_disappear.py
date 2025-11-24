from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.9/4/index.html')

    wait = WebDriverWait(browser, 10)

    close_ad_button = browser.find_element('css selector', '#closeBtn')
    browser.execute_script('arguments[0].scrollIntoView();', close_ad_button)
    wait.until(ec.element_to_be_clickable(close_ad_button))
    close_ad_button.click()

    ad_banner_locator = ('css selector', '#ad')
    wait.until(ec.invisibility_of_element_located(ad_banner_locator))

    click_me_button_locator = ('css selector', 'button')
    wait.until(ec.element_to_be_clickable(click_me_button_locator))
    click_me_button = browser.find_element('css selector', 'button')
    click_me_button.click()

    code_element = browser.find_element('css selector', '#message')
    code = code_element.text.strip()
    print(code)
