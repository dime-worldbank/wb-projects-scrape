# Libraries
import objects
import os
import csv
import time
import requests
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
def retrieve_txt_url(driver, n_tries=objects.ATTEMPTS):

    attempts = 0
    text_link = find_by_visible_text(driver, objects.TEXT_LINK)

    if len(text_link) == 0:
        return objects.DOC_NOT_AVAILABLE_MSG
    else:
        url = text_link[0].get_attribute('href')
        return url

def get_txt_url(driver, url):

    go_to_url(driver, url)
    txt_url = retrieve_txt_url(driver)

    return txt_url

def get_txt_urls(urls_dois, file):

    driver = get_driver()

    for url, doi in urls_dois:
        txt_url = get_txt_url(driver, url)
        add_rows_to_csv(objects.TXT_URL_FILE, ['doi', 'url'], [[doi, txt_url]])

    return True

def get_txt_doc(url_txt, doi):

    response = requests.get(url_txt)

    if response.status_code == 200:
        text = response.text
        with open(objects.TXT_DOC_LOCATION+str(doi)+'.txt', 'w', encoding=objects.ENCODING) as txt_file:
            txt_file.write(text)
        return True

    else:
        return False

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

# Data in files
def add_rows_to_csv(file, columns, rows):

    if not os.path.exists(file):
        with open(file, 'w', newline='', encoding=objects.ENCODING) as f:
            print('Created file')
            wr = csv.writer(f, dialect='excel')
            wr.writerows([columns])

    with open(file, 'a', newline='', encoding=objects.ENCODING) as f:
        wr = csv.writer(f, dialect='excel')
        wr.writerows(rows)

    return True
