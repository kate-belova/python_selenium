from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/6/6.3.1/index.html')

    cookie_name = 'token_22'
    cookie = browser.get_cookie(cookie_name)
    cookie_value = cookie['value']
    print(cookie_value)
