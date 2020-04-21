from pynput import keyboard

import utils
import input

import constants as CONST


def go_to_photo_moderation(driver, choice):
    wait_and_click_on_xpath = utils.create_waiter(
        driver, lambda element: element.click())
    wait_and_click_on_xpath(CONST.TASKS[choice])
    utils.iframe_wait(driver)
    CONST.FUNCTION_DICT[keyboard.Key.enter] = lambda: None
    input.start_listening(
        input.conditional_press(
            CONST.FUNCTION_DICT)
    )
