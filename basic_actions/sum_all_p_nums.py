from browser_setup import browser
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


with browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')

    p_elements_locator = ('css selector', '.main p')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.presence_of_all_elements_located(p_elements_locator))

    p_elements = browser.find_elements(*p_elements_locator)
    sum_p_numbers = sum([int(p.text.strip()) for p in p_elements])
    print(sum_p_numbers)
