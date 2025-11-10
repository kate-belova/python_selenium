from selenium import webdriver


def create_driver():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument('--window-size=1920,1080')
    driver_options.add_argument('--incognito')
    driver_options.add_argument('--disable-notifications')
    driver_options.add_argument('--ignore-certificate-errors')
    driver_options.add_experimental_option(
        'excludeSwitches', ['enable-automation']
    )

    driver = webdriver.Chrome(options=driver_options)
    return driver


browser = create_driver()
