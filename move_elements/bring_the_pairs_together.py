from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/5.10/3/index.html')

    wait = WebDriverWait(browser, 10)

    squares_locator = ('css selector', '.draganddrop')
    frames_locator = ('css selector', '.draganddrop_end')

    wait.until(
        ec.all_of(
            ec.visibility_of_all_elements_located(squares_locator),
            ec.visibility_of_all_elements_located(frames_locator),
        )
    )

    squares = browser.find_elements(*squares_locator)
    frames = browser.find_elements(*frames_locator)
    actions = ActionChains(browser)

    frame_by_color = {}

    for frame in frames:
        border_color = frame.value_of_css_property('border-top-color')
        frame_by_color[border_color] = frame

    for square in squares:
        bg_color = square.value_of_css_property('background-color')
        target_frame = frame_by_color.get(bg_color)

        if target_frame:
            browser.execute_script('arguments[0].scrollIntoView();', square)

            actions.click_and_hold(square).move_to_element(
                target_frame
            ).release().perform()

    browser.execute_script('window.scrollTo(0, 0);')

    message_element_locator = ('css selector', '#message')
    wait.until(ec.visibility_of_element_located(message_element_locator))
    message_element = browser.find_element(*message_element_locator)

    message = message_element.text.strip()
    print(message)
