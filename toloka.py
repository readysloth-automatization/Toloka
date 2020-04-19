from selenium                       import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By

from getpass import getpass
from constants import *

import utils
import tasks
import time
from argparse import ArgumentParser

from gooey import Gooey, GooeyParser

@Gooey(program_name='AUToloka',
       language='russian',
       image_dir='.')
def parse_arguments():
    parser = GooeyParser(description="Программа для быстрой и приятной работы с Яндекс.Толокой")
    parser.add_argument("Логин"   ,  help="Логин пользователя")
    parser.add_argument("Пароль"  ,  help="Пароль пользователя"             , widget='PasswordField')
    parser.add_argument("Задание" ,  help="Выберите задание из списка ниже" , choices=GUI_CHOICES.keys())
    parser.add_argument("--ZEN"   , required=False , help="Режим, в котором приятно работать" , action='store_true')

    return parser.parse_args()

def main():
    arguments = parse_arguments()
    startup(arguments)

def startup(arguments):
    driver = webdriver.Chrome()
    driver.get(BASE_URL)

    wait_and_click_on_css = utils.create_waiter(driver, lambda element: element.click())

    wait_and_click_on_css(LOGIN["LOGIN_BUTTON"])

    utils.create_waiter(driver, lambda element: element.send_keys(arguments.Логин + "\n"))(LOGIN["INPUT_FIELD"])
    time.sleep(1)
    utils.create_waiter(driver, lambda element: element.send_keys(arguments.Пароль + "\n"))(LOGIN["INPUT_FIELD"])

    tasks.go_to_organization_photo_moderation(driver)

main()
