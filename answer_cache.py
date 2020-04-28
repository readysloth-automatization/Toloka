"""
Модуль для работы с кэшем
"""
#from multiprocessing import Process, Manager

import constants as CONST


COMPLETED_TASKS = {}

def add_to_cache(driver, key):
    """
    Добавляет в кэш адрес новой картинки
    """
    focused_element = driver.find_element_by_xpath(CONST.XPATH["CURRENT_TASK"]+"/div/a")
    image_link = focused_element.get_attribute("href")
    #image_link = image_link[:image_link.rfind('/')+1] + 'XXXS'
    if key.char in ('j', 'k'):
        value = {'j' : True, 'k': False}[key.char]
        COMPLETED_TASKS[image_link] = value #(hashlib.sha1(image).hexdigest(),value)

#def compute_hash_of_remote_image(url):
#        #if image_link not in answer_cache.COMPLETED_TASKS:
#        #    image = urllib.request.urlopen(image_link).read()

def schedule_cache(driver, key):
    """
    Функция запускает в новом процессе fire-and-forget
    функцию add_to_cache
    """
    process = Process(target=add_to_cache, args=(driver, key))
    process.start()
