from datetime import datetime

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/methods/5/index.html')

    links_locator = ('css selector', 'a[href]')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.presence_of_all_elements_located(links_locator))

    links = browser.find_elements(*links_locator)
    urls = [link.get_attribute('href') for link in links]

    max_date = None
    the_very_url = None
    number = None
    for url in urls:
        browser.get(url)
        cookies = browser.get_cookies()

        for cookie in cookies:
            expiry_date = datetime.fromtimestamp(cookie['expiry'])
            if max_date is None or expiry_date > max_date:
                max_date = expiry_date
                the_very_url = url

                num_element = browser.find_element('css selector', '#result')
                number = num_element.text.strip()

    print(
        f'Самый долгий срок действия: {max_date} '
        f'у cookie на странице {the_very_url}\n'
        f'Число на странице: {number}'
    )
