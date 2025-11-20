from selenium.common import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.8/5/index.html')

    wait = WebDriverWait(browser, 5)

    iframes_locator = ('css selector', '#main_container iframe')
    wait.until(ec.presence_of_all_elements_located(iframes_locator))
    iframes = browser.find_elements(*iframes_locator)

    for iframe in iframes:
        browser.execute_script('arguments[0].scrollIntoView();', iframe)
        browser.switch_to.frame(iframe)

        click_me_button = browser.find_element('css selector', 'button')
        click_me_button.click()

        frame_num_element = browser.find_element(
            'css selector', '#numberDisplay'
        )
        frame_num = frame_num_element.text.strip()
        browser.switch_to.default_content()

        input_field = browser.find_element('css selector', 'input#guessInput')
        input_field.clear()
        input_field.send_keys(frame_num)

        check_button = browser.find_element('css selector', 'button#checkBtn')
        check_button.click()

        try:
            alert = browser.switch_to.alert
            result = alert.text
            alert.accept()
            print(result)
            break
        except NoAlertPresentException:
            pass
