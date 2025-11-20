from browser_setup import browser

with browser:
    numbers = []
    for i in range(1, 7):
        url = f'https://parsinger.ru/blank/1/{i}.html'
        browser.get(url)

        checkbox = browser.find_element(
            'css selector', 'input[type="checkbox"]'
        )
        checkbox.click()

        number_element = browser.find_element('css selector', '#result')
        number = int(number_element.text.strip())
        number_sqrt = number**0.5
        numbers.append(number_sqrt)

    print(round(sum(numbers), 9))
