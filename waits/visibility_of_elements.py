from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

# fmt: off
ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB',
               'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I','jolHZqD1', 'ZM6Ms3tw',
               '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']
# fmt: on

with browser:
    browser.get('https://parsinger.ru/selenium/5.9/3/index.html')

    for id_to_find in ids_to_find:
        element_locator = ('id', id_to_find)

        wait = WebDriverWait(browser, 50)
        wait.until(ec.visibility_of_element_located(element_locator))

        element = browser.find_element(*element_locator)
        element.click()

    alert = browser.switch_to.alert
    code = alert.text
    alert.accept()
    print(code)
