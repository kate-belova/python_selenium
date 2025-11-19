from selenium.webdriver import Keys

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')

    scrolling_container = browser.find_element(
        'css selector', '#scroll-container'
    )

    data = []
    numbers = []
    last_of_list_found = False

    while not last_of_list_found:
        number_elements = scrolling_container.find_elements(
            'css selector', 'span'
        )
        for element in number_elements:
            if element not in data:
                checkbox = element.find_element(
                    'css selector', 'input[type="checkbox"]'
                )
                checkbox.send_keys(Keys.DOWN)

                data.append(element)
                number = element.text.strip()
                if number:
                    numbers.append(int(number))

            if 'last-of-list' in element.get_attribute('class'):
                last_of_list_found = True
                break

    print(sum(numbers))
