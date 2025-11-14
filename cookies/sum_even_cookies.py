from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/methods/3/index.html')

    cookies = browser.get_cookies()

    result = sum(
        [
            int(cookie['value'])
            for cookie in cookies
            if int(cookie['name'].rsplit('_', 1)[1]) % 2 == 0
        ]
    )
    print(result)
