from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/6/6.html')

    formula_element = browser.find_element('css selector', '#text_box')
    formula = formula_element.text.replace(' ', '')
    result = eval(formula)

    dropdown = browser.find_element('css selector', '#selectId')
    dropdown.send_keys(result)

    send_button = browser.find_element('css selector', 'input[type="button"]')
    send_button.click()

    code_element = browser.find_element('css selector', '#result')
    code = code_element.text.strip()
    print(code)
