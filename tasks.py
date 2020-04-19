from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By

import utils
import input
import zenmode
from constants import *

#def photo_moderation_radiobuttons(driver):
#    radiobuttons_iterator = driver.find_elements_by_xpath(ZEN_MODE_XPATHS["RADIOBUTTON"])
#    for suitable, not_suitable in zip(*[iter(radiobuttons_iterator)]*2):
#        yield (suitable, not_suitable)
#
#def create_if_functions(driver, radiobuttons_iterator):
#    def if_suitable_photo():
#        suitable = next(radiobuttons_iterator)[0]
#
#    def if_not_suitable_photo():
#        not_suitable  = next(radiobuttons_iterator)[1]
#
#    return (if_suitable_photo, if_not_suitable_photo)


def go_to_photo_moderation(driver):
    wait_and_click_on_xpath = utils.create_waiter(driver, lambda element: element.click())
    wait_and_click_on_xpath(XPATH["SIMPLE_PHOTO_MODERATION"])
    utils.iframe_wait(driver)
    if ZEN_MODE:
        zenmode.zenify_photo_moderation(driver)
        input.start_listening(input.conditional_press(another = lambda : zenmode.zenify_photo_moderation(driver)))
    else:
        input.start_listening(input.conditional_press())

