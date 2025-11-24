from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

full_code = []
with browser:
    browser.get('https://parsinger.ru/selenium/5.9/5/index.html')

    elements = browser.find_elements('css selector', 'div.box_button')
    for element in elements:
        element.click()

        close_ad_button = browser.find_element('css selector', '#close_ad')
        close_ad_button.click()

        wait = WebDriverWait(browser, 10)
        wait.until(lambda _: element.text.strip() != '')
        code = element.text.strip()
        full_code.append(code)

print('-'.join(full_code))
