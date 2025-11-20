import re

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/8/8.4.1/')

    iframe = browser.find_element('css selector', 'iframe')
    browser.switch_to.frame(iframe)
    html_content = browser.page_source

    letters = re.findall(r'\*(\w)\*', html_content)

result = ''.join(letters)
print(result)
