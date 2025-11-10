from browser_setup import browser
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

with browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')

    blocks_locator = ('css selector', '.main .text')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.presence_of_all_elements_located(blocks_locator))

    blocks = browser.find_elements(*blocks_locator)

    second_ps_elements = [
        block.find_element('css selector', 'p:nth-child(2)')
        for block in blocks
    ]
    sum_numbers_from_second_ps = sum(
        [int(p.text.strip()) for p in second_ps_elements]
    )
    print(sum_numbers_from_second_ps)
