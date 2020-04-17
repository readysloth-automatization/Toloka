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

