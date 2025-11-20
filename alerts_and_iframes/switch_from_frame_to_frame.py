from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/8/8.4.3/index.html')

    for _ in range(4):
        iframe = browser.find_element('css selector', 'iframe')
        browser.switch_to.frame(iframe)

        click_button = browser.find_element('css selector', 'button')
        click_button.click()

    password_element = browser.find_element(
        'css selector', '.password-container'
    )
    password = password_element.text.strip()
    print(password)
