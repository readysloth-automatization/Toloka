from selenium                       import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By

from getpass import getpass
from constants import *

import utils
import tasks
import time

driver = webdriver.Chrome()
driver.get(BASE_URL)

wait_and_click_on_css = utils.create_waiter(driver, lambda element: element.click())

wait_and_click_on_css(LOGIN["LOGIN_BUTTON"])

username = input("Введите логин : ")
password = getpass("Введите пароль: ")

utils.create_waiter(driver, lambda element: element.send_keys(username + "\n"))(LOGIN["INPUT_FIELD"])
time.sleep(0.1)
utils.create_waiter(driver, lambda element: element.send_keys(password + "\n"))(LOGIN["INPUT_FIELD"])

tasks.go_to_photo_moderation(driver)

