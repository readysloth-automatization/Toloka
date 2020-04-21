import utils
import time

from constants import *
import answer_cache
import re



def zenify_photo_moderation(driver):
    utils.cycle_wait(driver, ZEN_MODE_XPATHS["NOT_RADIO_BUTTONS"], lambda e : len(e) > 0)

    def remove_trash():
        for trash_element in driver.find_elements_by_xpath(ZEN_MODE_XPATHS["NOT_RADIO_BUTTONS"]):
            driver.execute_script(CURRENT_ELEMENT[THIS]["ANCESTOR"] + ".removeChild(arguments[0])", trash_element)

    def resize_tasks():
        for task in driver.find_elements_by_xpath(ZEN_MODE_XPATHS["ANSWER"]+'/..'):
            cmd  = CURRENT_ELEMENT[THIS][STYLE] + ".display = 'grid';"
            cmd += CURRENT_ELEMENT[THIS][STYLE] + "['align-content'] = 'space-between';"
            cmd += CURRENT_ELEMENT[THIS][STYLE] + ".height = '95%';"
            driver.execute_script(cmd, task)

        for element in task.find_elements_by_xpath("//div[@class='block'] | //div[@class='answer']"):
            driver.execute_script(CURRENT_ELEMENT[THIS][STYLE] + ".width = '100%';", element)

    def make_bigger_radio_buttons():
        for radiobutton in driver.find_elements_by_xpath(ZEN_MODE_XPATHS["RADIOBUTTON"]):
            utils.make_bigger_text(driver, radiobutton, 40)
            driver.execute_script(CURRENT_ELEMENT[THIS][STYLE] + "['line-height'] = '0px'", radiobutton)

    def make_bigger_images():
        for image in driver.find_elements_by_xpath(XPATH["IMAGES"]+'/div'):
            url    = image.get_attribute('style')
            bigger = url.replace('L','XL')
            cmd    = CURRENT_ELEMENT[THIS][STYLE] + '=' + "'{}';".format(bigger)
            cmd   += CURRENT_ELEMENT[THIS][STYLE] + ".height = '200%';"
            driver.execute_script(cmd, image)

    def make_annotations():
        for left_annotation, right_annotation in utils.list_to_tuple_list(driver.find_elements_by_xpath(ZEN_MODE_XPATHS["ANNOTATIONS"])):
            cmd  = CURRENT_ELEMENT[THIS][STYLE] + ".width  = '30px';"
            cmd += CURRENT_ELEMENT[THIS][STYLE] + ".height = '30px';"
            cmd += CURRENT_ELEMENT[THIS][STYLE] + "['font-size'] = '25px';"
            cmd += CURRENT_ELEMENT[THIS][STYLE] + "['line-height'] = 1;"
            cmd += CURRENT_ELEMENT[THIS][STYLE] + "['background-color'] = '#E405FF';"
            annotation_text = ARG0 + '.innerText = {}'
            driver.execute_script(cmd + annotation_text.format('"j"'), left_annotation)
            driver.execute_script(cmd + annotation_text.format('"k"'), right_annotation)

    def colorize_previous_answers():
        for image in driver.find_elements_by_xpath(XPATH["IMAGES"]+'/div'):
            url   = image.get_attribute('style')
            match = re.search("'(.+?)'", url)
            cmd  = CURRENT_ELEMENT[THIS][STYLE] + ".background  = "
            if match:
                link = match.group(1)
                if link in answer_cache:
                    choice = answer_cache[link]
                    if choice:
                        cmd += "'palegreen';"
                    else:
                        cmd += "'palevioletred';"
                    driver.execute_script(cmd, utils.get_parent(driver, image, 4))

    remove_trash()
    resize_tasks()
    make_bigger_radio_buttons()
    make_bigger_images()
    make_annotations()
    colorize_previous_answers()
