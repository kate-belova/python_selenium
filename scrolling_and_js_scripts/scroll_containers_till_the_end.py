from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/7/7.3.5/index.html')

    containers = browser.find_elements(
        'css selector', '#containers-wrapper .scroll-container'
    )
    status_ids = ['status-left', 'status-right']

    actions = ActionChains(browser)
    for i, container in enumerate(containers):
        actions.click(container).send_keys(Keys.END).perform()

        status_element = browser.find_element('id', status_ids[i])

        wait = WebDriverWait(browser, 5)
        wait.until(lambda _: 'Прокручено!' in status_element.text)

    access_code_element = browser.find_element(
        'css selector', '[key="access_code"]'
    )
    browser.execute_script(
        'return arguments[0].scrollIntoView(true);', access_code_element
    )
    access_code = access_code_element.text.strip()
    print(access_code)
