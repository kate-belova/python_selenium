from browser_setup import browser

with browser:
    browser.set_window_size(1200, 700)
    browser.get('https://parsinger.ru/selenium/8/8.2.1/index.html')

    check_size_button = browser.find_element('css selector', '#checkSizeBtn')
    check_size_button.click()

    message_element = browser.find_element('css selector', '#message')
    message = message_element.text.strip()
    assert message == 'Размеры корректны!', 'Неверный размер окна'

    code_element = browser.find_element('css selector', '#secret')
    code = code_element.text.strip()
    print(code)
