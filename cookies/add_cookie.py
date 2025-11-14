from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/6/6.3.3/index.html')

    browser.add_cookie({'name': 'secretKey', 'value': 'selenium123'})
    browser.refresh()

    password_element = browser.find_element('css selector', '#password')
    password = password_element.text.split()[1].strip()
    print(password)
