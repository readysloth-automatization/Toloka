from selenium                       import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By

import utils
import pynput
import constants as CONST

driver = webdriver.Chrome()
driver.get(CONST.BASE_URL)

wait_and_click_on_css = utils.create_waiter(driver, By.CSS_SELECTOR, lambda element: element.click())

wait_and_click_on_css(CONST.CSS_SELECTORS["LOGIN_BUTTON"])

username = input("Введите логин : ")
password = input("Введите пароль: ")

utils.create_waiter(driver, By.CSS_SELECTOR, lambda element: element.send_keys(username + "\n"))(CONST.CSS_SELECTORS["LOGIN_FIELD"])
utils.create_waiter(driver, By.CSS_SELECTOR, lambda element: element.send_keys(password + "\n"))(CONST.CSS_SELECTORS["PASSWORD_FIELD"])

wait_and_click_on_xpath = utils.create_waiter(driver, By.XPATH, lambda element: element.click())
wait_and_click_on_xpath(CONST.XPATH["SIMPLE_PHOTO_MODERATION"])

import time
time.sleep(4)
#utils.create_waiter(driver, By.XPATH, None)("//iframe")
utils.iframe_wait(driver)

if CONST.ZEN_MODE:
    for answer in driver.find_elements_by_xpath(CONST.ZEN_MODE_XPATHS["ANSWER"]):
        trash_element = answer.find_element_by_xpath(".//*")
        driver.execute_script("arguments[0].parentNode.removeChild(arguments[0])", trash_element)
