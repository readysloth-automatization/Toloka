import utils
import constants as CONST

def zenify_photo_moderation(driver):
    for answer in driver.find_elements_by_xpath(CONST.ZEN_MODE_XPATHS["ANSWER"]):
        trash_element = answer.find_element_by_xpath(".//*")
        driver.execute_script("arguments[0].parentNode.removeChild(arguments[0])", trash_element)

    for answer in driver.find_elements_by_xpath(CONST.ZEN_MODE_XPATHS["ANSWER"]):
        utils.add_br(driver, answer, count=6)

    for radiobutton in driver.find_elements_by_xpath(CONST.ZEN_MODE_XPATHS["RADIOBUTTON"]):
        utils.make_bigger_text(driver, radiobutton)
        utils.add_br(driver, utils.get_parent(driver, radiobutton, ancestor=4), count=3)
