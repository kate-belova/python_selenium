from browser_setup import browser
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

with browser:
    browser.get('https://parsinger.ru/selenium/8/8.1.2/index.html')

    links = browser.find_elements('css selector', 'a[href]')
    for link in links:
        browser.execute_script(
            'window.open(arguments[0], "_blank");', link.get_attribute('href')
        )

    all_numbers = []
    tabs = browser.window_handles

    wait = WebDriverWait(browser, 5)

    for tab in tabs[1:]:
        browser.switch_to.window(tab)

        numbers_container_locator = ('css selector', '.numbers-container')
        wait.until(ec.presence_of_element_located(numbers_container_locator))

        numbers_elements = browser.find_elements('css selector', '.number')
        numbers = [
            int(num.text.strip())
            for num in numbers_elements
            if num.text.strip().isdigit()
        ]
        all_numbers.extend(numbers)

    browser.switch_to.window(tabs[0])

    input_field = browser.find_element('css selector', 'input')
    input_field.send_keys(sum(all_numbers))

    timer_locator = ('css selector', '#timer')
    wait.until(ec.text_to_be_present_in_element(timer_locator, '0'))

    check_button = browser.find_element('css selector', 'button#checkButton')
    check_button.click()

    password_element = browser.find_element('css selector', '#passwordDisplay')
    password = password_element.text.split(':')[1].strip()
    print(password)
