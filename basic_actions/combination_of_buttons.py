from selenium.webdriver import ActionChains, Keys

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/7/7.3.3/index.html')

    actions = ActionChains(browser)
    actions.key_down(Keys.CONTROL).key_down(Keys.ALT).key_down(
        Keys.SHIFT
    ).send_keys('T').key_up(Keys.CONTROL).key_up(Keys.ALT).key_up(
        Keys.SHIFT
    ).perform()

    access_code_element = browser.find_element(
        'css selector', '[key="access_code"]'
    )
    access_code = access_code_element.text.strip()
    print(access_code)
