from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/2/2.html')

    link_text = '16243162441624'
    link = browser.find_element('link text', link_text)
    link.click()

    code_element = browser.find_element('css selector', '#result')
    code = code_element.text.strip()
    print(code)
