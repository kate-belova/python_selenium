from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.5/4/1.html')

    gray_fields = browser.find_elements(
        'css selector', 'textarea[color="gray"]'
    )
    blue_fields = browser.find_elements(
        'css selector', 'textarea[color="blue"]'
    )
    check_buttons = browser.find_elements('css selector', 'button')

    for gray_field, blue_field, check_button in zip(
        gray_fields, blue_fields, check_buttons
    ):
        number = gray_field.text
        gray_field.clear()
        blue_field.send_keys(number)
        check_button.click()

    check_button = browser.find_element('css selector', '#checkAll')
    browser.execute_script('arguments[0].scrollIntoView();', check_button)
    check_button.click()

    code_element = browser.find_element('css selector', '#congrats')
    code = code_element.text.strip()
    print(code)
