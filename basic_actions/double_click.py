from selenium.webdriver import ActionChains

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/7/7.3.2/index.html')

    element = browser.find_element('css selector', '#dblclick-area')

    action = ActionChains(browser)
    action.double_click(element).perform()

    password_element = browser.find_element('css selector', '#password')
    password = password_element.text.strip()
    print(password)
