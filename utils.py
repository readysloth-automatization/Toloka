from selenium.webdriver.support   import expected_conditions as EC
from selenium.webdriver.support   import wait
from selenium.webdriver.common.by import By
import selenium.common as selenium_common

def create_waiter(driver, locator, action, timeout = 30):
    waiter = wait.WebDriverWait(driver, timeout)
    def wait_and_make_action(selector):
        waiter.until(EC.presence_of_element_located((locator, selector)))
        if action is None:
            return
        if locator is By.CSS_SELECTOR:
            action(driver.find_element_by_css_selector(selector))
        elif locator is By.XPATH:
            action(driver.find_element_by_xpath(selector))
    return wait_and_make_action

def iframe_wait(driver, timeout = 30):
    waiter = wait.WebDriverWait(driver, timeout)
    IFRAME_XPATH = '//iframe'
    waiter.until(EC.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath(IFRAME_XPATH)))

def make_bigger_text(driver, element, fontsize = 16):
    bigger_font = """<font size = "{fs}"> ## </font>""".format(fs=fontsize)
    text        = element.text
    bigger_text = bigger_font.replace('##', text)
    driver.execute_script("arguments[0].innerHTML = arguments[0].innerHTML.replace('{e_text}','{e_bigger_text}')".format(e_text=text, e_bigger_text=bigger_text), element)


def add_br(driver, element, count = 1):
    line_break = """<br style="line-height:{cn};">""".format(cn=count)
    driver.execute_script("arguments[0].innerHTML = '{br}' + arguments[0].innerHTML".format(br=line_break), element)

def get_parent(driver, element, ancestor = 1):
    return driver.execute_script("return arguments[0]" + ".parentNode"*ancestor + ";", element)

