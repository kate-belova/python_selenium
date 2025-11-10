from faker import Faker

from browser_setup import browser

random_generator = Faker()

with browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')

    first_name_input = browser.find_element(
        'css selector', 'input[name="first_name"]'
    )
    first_name = random_generator.first_name()
    first_name_input.send_keys(first_name)

    last_name_input = browser.find_element(
        'css selector', 'input[name="last_name"]'
    )
    last_name = random_generator.last_name()
    last_name_input.send_keys(last_name)

    second_name_input = browser.find_element(
        'css selector', 'input[name="patronymic"]'
    )
    second_name = random_generator.first_name()
    second_name_input.send_keys(second_name)

    age_input = browser.find_element('css selector', 'input[name="age"]')
    age = random_generator.random_int(min=15, max=85)
    age_input.send_keys(age)

    city_input = browser.find_element('css selector', 'input[name="city"]')
    city = random_generator.city()
    city_input.send_keys(city)

    email_input = browser.find_element('css selector', 'input[name="email"]')
    email = random_generator.email()
    email_input.send_keys(email)

    submit_button = browser.find_element(
        'css selector', 'input[type="button"]'
    )
    submit_button.click()

    result = browser.find_element('css selector', '#result')
    browser.execute_script('arguments[0].scrollIntoView();', result)
    code = result.text.strip()
    print(code)
