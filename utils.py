from selenium.webdriver.support   import expected_conditions as EC
from selenium.webdriver.support   import wait
from selenium.webdriver.common.by import By
import selenium.common as selenium_common

from constants import *

import time

def create_waiter(driver, action, timeout = 30):
    waiter = wait.WebDriverWait(driver, timeout)
    def wait_and_make_action(selector):
        waiter.until(EC.presence_of_element_located((By.XPATH, selector)))
        if action is None:
            return
        action(driver.find_element_by_xpath(selector))
    return wait_and_make_action

def iframe_wait(driver, timeout = 30):
    waiter = wait.WebDriverWait(driver, timeout)
    IFRAME_XPATH = '//iframe'
    time.sleep(0.5)
    frame = cycle_wait(driver, IFRAME_XPATH, lambda e: len(e) > 0)
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath(IFRAME_XPATH))


def make_bigger_text(driver, element, fontsize = 16):
    driver.execute_script(CURRENT_ELEMENT[THIS][STYLE] + "['font-size'] = {fs}".format(fs=fontsize), element)

def add_br(driver, element, count = 1):
    line_break = """<br style="line-height:{cn};">""".format(cn=count)
    driver.execute_script(CURRENT_ELEMENT[THIS]["INNER_HTML"] + " = '{br}'".format(br=line_break) + CURRENT_ELEMENT[THIS]["INNER_HTML"], element)

def get_parent(driver, element, ancestor = 1):
    return driver.execute_script("return" + CURRENT_ELEMENT[THIS] + ".parentNode"*ancestor + ";", element)

def cycle_wait(driver, locator, predicate):
    elements = None
    while True:
        elements = driver.find_elements_by_xpath(locator)
        if predicate(elements):
            break
    return elements
