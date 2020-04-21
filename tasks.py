from pynput import keyboard

import utils
import input
import zenmode
import answer_cache

import constants as CONST

def choose_task(driver, choice):
    {
        "ORGANIZATION_PHOTO_MODERATION" :  go_to_photo_moderation,
        "SIMPLE_PHOTO_MODERATION" : go_to_photo_moderation,
        "RATE_CARD" : go_to_card_rating,
    }[choice](driver,choice)


def go_to_photo_moderation(driver, choice):
    wait_and_click_on_xpath = utils.create_waiter(
        driver, lambda element: element.click())
    wait_and_click_on_xpath(CONST.TASKS[choice])
    utils.iframe_wait(driver)
    CONST.FUNCTION_DICT[keyboard.Key.enter] = lambda: None
    if CONST.ZEN_MODE:
        CONST.FUNCTION_DICT[keyboard.Key.enter] = lambda: zenmode.zenify_photo_moderation(
            driver)
        zenmode.zenify_photo_moderation(driver)
    input.start_listening(
        input.conditional_press(
            CONST.FUNCTION_DICT,
            preprocess=lambda key: answer_cache.schedule_cache(driver, key)
        )
    )

def go_to_card_rating(driver, choice):
    wait_and_click_on_xpath = utils.create_waiter(
        driver, lambda element: element.click())
    wait_and_click_on_xpath(CONST.TASKS[choice])
    utils.iframe_wait(driver)
    CONST.FUNCTION_DICT[keyboard.Key.enter] = lambda: None
    if CONST.ZEN_MODE:
        CONST.FUNCTION_DICT[keyboard.Key.enter] = lambda: zenmode.zenify_card_rating(
            driver)
        zenmode.zenify_photo_moderation(driver)
    input.start_listening(
        input.conditional_press(
            CONST.FUNCTION_DICT,
            preprocess=lambda key: answer_cache.schedule_cache(driver, key)
        )
    )
