from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/6/6.5/index.html')

    button_finish = browser.find_element('css selector', '#target')
    browser.execute_script('arguments[0].scrollIntoView();', button_finish)
    button_finish.click()

    secret_key_element = browser.find_element('css selector', '#secret-key')
    secret_key = secret_key_element.text.split(':')[1].strip()
    print(secret_key)
