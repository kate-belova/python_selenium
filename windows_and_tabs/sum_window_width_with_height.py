from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/8/8.2.2/index.html')

    window_width = browser.get_window_size()['width']
    window_height = browser.get_window_size()['height']

    input_field = browser.find_element('css selector', 'input#answer')
    input_field.send_keys(window_width + window_height)

    check_button = browser.find_element('css selector', 'button#checkBtn')
    check_button.click()

    password_element = browser.find_element('css selector', '#resultMessage')
    password = password_element.text.split()[1].strip()
    print(password)
