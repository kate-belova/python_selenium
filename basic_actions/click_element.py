from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.1/index.html')

    start_button = browser.find_element('css selector', '#clickButton')
    start_button.click()

    code_element = browser.find_element('css selector', '#codeOutput')
    code = code_element.text.strip()
    print(code)
