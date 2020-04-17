from selenium                       import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By

import utils
import tasks
import constants as CONST

driver = webdriver.Chrome()
driver.get(CONST.BASE_URL)

wait_and_click_on_css = utils.create_waiter(driver, By.CSS_SELECTOR, lambda element: element.click())

wait_and_click_on_css(CONST.CSS_SELECTORS["LOGIN_BUTTON"])

username = input("Введите логин : ")
password = input("Введите пароль: ")

utils.create_waiter(driver, By.CSS_SELECTOR, lambda element: element.send_keys(username + "\n"))(CONST.CSS_SELECTORS["LOGIN_FIELD"])
utils.create_waiter(driver, By.CSS_SELECTOR, lambda element: element.send_keys(password + "\n"))(CONST.CSS_SELECTORS["PASSWORD_FIELD"])

tasks.go_to_photo_moderation(driver)

