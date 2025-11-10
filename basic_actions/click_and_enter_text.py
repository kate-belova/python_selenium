from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.3/index.html')

    start_mission_button = browser.find_element('css selector', '#showTextBtn')
    start_mission_button.click()

    password_element = browser.find_element('css selector', '#text1')
    password = password_element.text.strip()

    input_password_field = browser.find_element('css selector', '#userInput')
    input_password_field.send_keys(password)

    check_button = browser.find_element('css selector', '#checkBtn')
    check_button.click()

    code_element = browser.find_element('css selector', '#text2')
    code = code_element.text.strip()
    print(code)
