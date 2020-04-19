from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By

import utils
import input
import zenmode
from constants import *
from pynput    import keyboard

def go_to_organization_photo_moderation(driver):
    wait_and_click_on_xpath = utils.create_waiter(driver, lambda element: element.click())
    wait_and_click_on_xpath(TASKS["ORGANIZATION_PHOTO_MODERATION"])
    utils.iframe_wait(driver)
    if ZEN_MODE:
        FUNCTION_DICT[keyboard.Key.enter] = lambda : zenmode.zenify_photo_moderation(driver)
        zenmode.zenify_photo_moderation(driver)
    input.start_listening(input.conditional_press(FUNCTION_DICT))

def go_to_simple_photo_moderation(driver):
    wait_and_click_on_xpath = utils.create_waiter(driver, lambda element: element.click())
    wait_and_click_on_xpath(TASKS["SIMPLE_PHOTO_MODERATION"])
    utils.iframe_wait(driver)
    if ZEN_MODE:
        FUNCTION_DICT[keyboard.Key.enter] = lambda : zenmode.zenify_photo_moderation(driver)
        zenmode.zenify_photo_moderation(driver)
    input.start_listening(input.conditional_press(FUNCTION_DICT))

