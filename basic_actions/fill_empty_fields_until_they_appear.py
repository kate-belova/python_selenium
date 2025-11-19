from faker import Faker
from selenium.webdriver import Keys

from browser_setup import browser

random_generator = Faker()

with browser:
    browser.get('https://parsinger.ru/selenium/7/7.2/index.html')

    while True:
        fields = browser.find_elements(
            'css selector',
            '.input-wrapper:has(div[data-filled="false"]) > input',
        )
        if not fields:
            break
        fields[0].send_keys(random_generator.word(), Keys.ENTER, Keys.DOWN)

    password_element = browser.find_element('css selector', '#hidden-password')
    password = password_element.text.split()[1].strip()
    print(password)
