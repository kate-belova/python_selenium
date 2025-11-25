from selenium.webdriver import ActionChains

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/draganddrop/1/index.html')

    red = browser.find_element('css selector', '#field1')
    gray = browser.find_element('css selector', '#field2')

    action = ActionChains(browser)
    action.drag_and_drop(red, gray).perform()

    token_element = browser.find_element('css selector', '#result')
    token = token_element.text.strip()
    print(token)
