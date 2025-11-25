from selenium.webdriver import ActionChains

from browser_setup import browser
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

with browser:
    browser.get('https://parsinger.ru/draganddrop/4/index.html')

    target_word_element = browser.find_element('css selector', '#target-word')
    target_word = target_word_element.text.strip()
    word_as_letters = list(target_word)

    letters_locator = ('css selector', '#alphabet .draggable-letter')

    wait = WebDriverWait(browser, 5)
    wait.until(ec.visibility_of_all_elements_located(letters_locator))

    letters = browser.find_elements(*letters_locator)
    letters_dict = {letter.text.strip(): letter for letter in letters}

    targets_locator = ('css selector', '#letter-slots .letter-slot')
    wait.until(ec.visibility_of_all_elements_located(targets_locator))
    targets = browser.find_elements(*targets_locator)

    actions = ActionChains(browser)
    for letter, target in zip(word_as_letters, targets):
        target_letter = letters_dict[letter]
        browser.execute_script('arguments[0].scrollIntoView();', target_letter)
        actions.drag_and_drop(letters_dict[letter], target).perform()

    code_locator = ('css selector', '#password')
    wait.until(ec.visibility_of_element_located(code_locator))

    code_element = browser.find_element(*code_locator)
    code = code_element.text.strip()
    print(code)
