import utils
import time

from constants import *

def zenify_photo_moderation(driver):
    utils.cycle_wait(driver, ZEN_MODE_XPATHS["NOT_RADIO_BUTTONS"], lambda e : len(e) > 0)

    def remove_trash():
        for trash_element in driver.find_elements_by_xpath(ZEN_MODE_XPATHS["NOT_RADIO_BUTTONS"]):
            driver.execute_script(CURRENT_ELEMENT[THIS]["ANCESTOR"] + ".removeChild(arguments[0])", trash_element)

    def resize_tasks():
        for task in driver.find_elements_by_xpath(ZEN_MODE_XPATHS["ANSWER"]+'/..'):
            driver.execute_script(CURRENT_ELEMENT[THIS][STYLE] + ".display = 'grid';", task)
        for element in task.find_elements_by_xpath("//div[@class='block'] | //div[@class='answer']"):
            driver.execute_script(CURRENT_ELEMENT[THIS][STYLE] + ".width = '100%';", element)

    def make_bigger_radio_buttons():
        for radiobutton in driver.find_elements_by_xpath(ZEN_MODE_XPATHS["RADIOBUTTON"]):
            utils.make_bigger_text(driver, radiobutton, 40)
            driver.execute_script(CURRENT_ELEMENT[THIS][STYLE] + "['line-height'] = '0px'", radiobutton)

    remove_trash()
    resize_tasks()
    make_bigger_radio_buttons()
