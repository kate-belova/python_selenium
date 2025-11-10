from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.4/index.html')

    secret_key_button = browser.find_element(
        'css selector', '#secret-key-button'
    )
    secret_key_button.click()

    secret_key = secret_key_button.get_attribute('data')
    print(secret_key)
