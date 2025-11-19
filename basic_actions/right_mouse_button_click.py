from selenium.webdriver import ActionChains

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/7/7.3.4/index.html')

    element = browser.find_element('css selector', '#context-area')
    action = ActionChains(browser)
    action.context_click(element).perform()

    get_password_option = browser.find_element(
        'css selector', '[data-action="get_password"]'
    )
    get_password_option.click()

    password_element = browser.find_element(
        'css selector', '[key="access_code"]'
    )
    password = password_element.text.strip()
    print(password)
