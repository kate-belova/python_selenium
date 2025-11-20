from browser_setup import browser
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

with browser:
    browser.get('https://parsinger.ru/blank/3/index.html')

    wait = WebDriverWait(browser, 5)

    buttons_locator = ('css selector', 'input.buttons')
    wait.until(ec.presence_of_all_elements_located(buttons_locator))
    buttons = browser.find_elements(*buttons_locator)

    for button in buttons:
        wait.until(ec.element_to_be_clickable(button))
        button.click()

    titles = []
    tabs = browser.window_handles
    for tab in tabs:
        browser.switch_to.window(tab)
        title = browser.title
        if title.isdigit():
            titles.append(int(title))

    print(sum(titles))
