import hashlib
from constants import *
from multiprocessing import Process, Manager


COMPLETED_TASKS = Manager().dict()

def add_to_cache(driver, key):
    focused_element = driver.find_element_by_xpath(XPATH["CURRENT_TASK"]+"/div/a")
    image_link = focused_element.get_attribute("href")[:-1] + 'XXXS'
    if key.char in ('j','k'):
        value = {'j' : True, 'k': False}[key.char]
        COMPLETED_TASKS[image_link] = value #(hashlib.sha1(image).hexdigest(),value)

#def compute_hash_of_remote_image(url):
#        #if image_link not in answer_cache.COMPLETED_TASKS:
#        #    image = urllib.request.urlopen(image_link).read()

def schedule_cache(driver, key):
    process = Process(target=add_to_cache, args=(driver, key))
    process.start()
