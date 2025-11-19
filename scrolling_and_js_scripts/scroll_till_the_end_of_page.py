from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/7/7.1/index.html')

    page_height = browser.execute_script('return document.body.scrollHeight')
    browser.execute_script(f'window.scrollTo(0, {page_height})')

    password_element = browser.find_element(
        'css selector', '#secret-container'
    )

    wait = WebDriverWait(browser, 5)
    wait.until(lambda _: password_element.text.strip() != '')

    password = password_element.text.split()[1].strip()
    print(password)
