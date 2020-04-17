from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By

import time

import utils
import input
import zenmode
import constants as CONST

def photo_moderation_radiobuttons(driver):
    radiobuttons_iterator = driver.find_elements_by_xpath(CONST.ZEN_MODE_XPATHS["RADIOBUTTON"])
    for yes, no in zip(*[iter(radiobuttons_iterator)]*2):
        yield (yes, no)

def create_if_functions(radiobuttons_iterator):
    def if_true_photo():
        next(radiobuttons_iterator)[0].click()

    def if_false_photo():
        next(radiobuttons_iterator)[1].click()

    return (if_true_photo, if_false_photo)


def go_to_photo_moderation(driver):
    wait_and_click_on_xpath = utils.create_waiter(driver, By.XPATH, lambda element: element.click())
    wait_and_click_on_xpath(CONST.XPATH["SIMPLE_PHOTO_MODERATION"])
    time.sleep(5)
    utils.iframe_wait(driver)
    if CONST.ZEN_MODE:
        zenmode.zenify_photo_moderation(driver)

    if_true, if_false = create_if_functions(photo_moderation_radiobuttons(driver))

    input.start_listening(input.conditional_press(if_true, if_false))
