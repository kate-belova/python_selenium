from browser_setup import browser
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

with browser:
    browser.get('https://parsinger.ru/selenium/5.7/1/index.html')

    pieces_locator = ('css selector', 'button.clickMe')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.presence_of_all_elements_located(pieces_locator))

    pieces = browser.find_elements(*pieces_locator)
    for piece in pieces:
        browser.execute_script(
            'return arguments[0].scrollIntoView(true);', piece
        )
        piece.click()

    alert = browser.switch_to.alert
    result = alert.text.strip()
    alert.accept()
    print(result)
