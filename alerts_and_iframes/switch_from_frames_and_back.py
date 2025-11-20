from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/8/8.4.2/index.html')

    for i in range(1, 5):
        iframe = browser.find_element('css selector', f'iframe#frame{i}')
        browser.execute_script(
            'return arguments[0].scrollIntoView(true);', iframe
        )
        browser.switch_to.frame(iframe)

        if i != 4:
            unlock_button = browser.find_element(
                'css selector', 'button.unlock-button'
            )
            unlock_button.click()
            browser.switch_to.default_content()
        else:
            password_element = browser.find_element('css selector', 'h2')
            password = password_element.text.split(':')[1].strip()
            print(password)
