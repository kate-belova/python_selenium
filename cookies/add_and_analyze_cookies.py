from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser
from cookies.cookies_data import cookies

with browser:
    browser.get('https://parsinger.ru/selenium/5.6/1/index.html')

    browser.delete_all_cookies()
    browser.refresh()

    min_age = float('inf')
    max_number_of_skills = -float('inf')
    the_very_cookie = None

    for cookie in cookies:
        browser.add_cookie(cookie)
        browser.refresh()

        age_element_locator = ('css selector', '#age')
        skills_locator = ('css selector', '#skillsList li')

        wait = WebDriverWait(browser, 5)
        wait.until(ec.visibility_of_element_located(age_element_locator))
        wait.until(ec.presence_of_all_elements_located(skills_locator))

        age_element = browser.find_element(*age_element_locator)
        browser.execute_script('arguments[0].scrollIntoView();', age_element)
        age = int(age_element.text.split()[1].strip())

        skills_elements = browser.find_elements(*skills_locator)
        browser.execute_script(
            'arguments[0].scrollIntoView();', skills_elements[0]
        )
        number_of_skills = len(skills_elements)

        if age < min_age and number_of_skills > max_number_of_skills:
            min_age = age
            max_number_of_skills = number_of_skills
            the_very_cookie = cookie

        browser.delete_all_cookies()
        browser.refresh()

    print(
        f'Cookie: {the_very_cookie}\nAge: {min_age}, '
        f'Number of Skills: {max_number_of_skills}'
    )
