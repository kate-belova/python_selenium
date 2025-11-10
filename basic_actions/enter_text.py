from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.2/index.html')

    input_field = browser.find_element('css selector', '#codeInput')
    dragon_name = 'Дрогон'
    input_field.send_keys(dragon_name)

    get_code_button = browser.find_element('css selector', '#clickButton')
    get_code_button.click()

    code_element = browser.find_element('css selector', '#codeOutput')
    code = code_element.text.strip()
    print(code)
