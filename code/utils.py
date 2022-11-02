# Libraries
import objects
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import \
    NoSuchElementException

# URL Navigation
def get_driver():

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options, executable_path=objects.CHROMEDRIVER_PATH)

    return driver

def go_to_url(driver, url):

    driver.get(url)

    return True

# Downloads
def get_txt_url(driver):

    text_link = find_by_visible_text(driver, objects.TEXT_LINK)[0]
    url = text_link.get_attribute('href')

    return url

# HTML navigation
def find_by_visible_text(driver, text, n_tries=objects.ATTEMPTS):

    attempts = 0
    while attempts <= n_tries:

        try:
            elements = driver.find_elements_by_xpath("//*[contains(text(), '"+text+"')]")
            return elements
        except NoSuchElementException:
            attempts += 1
            time.sleep(3)

    if n_tries > 1:
        print('\tCould not find the element with text: '+text)

    return False
