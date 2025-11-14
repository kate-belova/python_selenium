from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/6/6.3/index.html')

    cookies = browser.get_cookies()

    song_name = None
    if len(cookies) > 0:
        song_name = cookies[0]['name']
        print(song_name)

    input_field = browser.find_element('css selector', 'input[type="text"]')
    input_field.send_keys(song_name)

    check_button = browser.find_element('css selector', '#checkButton')
    check_button.click()

    motto_element = browser.find_element('css selector', '#result')
    motto = motto_element.text.strip()
    print(motto)
