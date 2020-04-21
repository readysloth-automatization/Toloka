from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import selenium.common.exceptions as selenium_exceptions

import constants as CONST
import os

import utils

import utils
import tasks
import time
import json
import answer_cache

from gooey import Gooey, GooeyParser


@Gooey(program_name='AUToloka',
       language='russian',
       default_size=(800, 600),
       image_dir='.',
       menu=[{
           "name": 'Прочти меня',
           "items": [{
               'type': 'AboutDialog',
               'menuTitle': 'Помощь',
               'description':
               """
Управление на толоке:

j       отметить "подходит"

k       отметить "не подходит"

Shift+j отметить "подходит" на предыдущем задании

Shift+k отметить "не подходит" на предыдущем задании

Enter   перейти на следующий лист с заданиями

Esc     завершить программу
""",
               'version': '0.0.1',
               'copyright': '2020',
               'website': 'https://vk.com/autoloka',
           }
           ]}
       ])
def parse_arguments():
    parser = GooeyParser(
        description="Программа для быстрой и приятной работы с Яндекс.Толокой")
    parser.add_argument("Логин", help="Логин пользователя")
    parser.add_argument(
        "Пароль",
        help="Пароль пользователя",
        widget='PasswordField')
    parser.add_argument(
        "Задание",
        help="Выберите задание из списка ниже",
        choices=CONST.GUI_CHOICES.keys())
    parser.add_argument(
        "--ZEN",
        required=False,
        help="Режим, в котором приятно работать",
        action='store_true')

    return parser.parse_args()


def main():
    arguments = parse_arguments()
    if os.path.exists(CONST.CACHE_FILE):
        with open(CONST.CACHE_FILE, "r") as cache_json:
            loaded_dict = json.loads(cache_json.read())
            answer_cache.COMPLETED_TASKS.update(loaded_dict)
    try:
        startup(arguments).quit()
    except selenium_exceptions.WebDriverException:
        pass
    with open(CONST.CACHE_FILE, "w") as cache_json:
        cache_json.write(json.dumps(dict(answer_cache.COMPLETED_TASKS)))


def startup(arguments):
    constants.ZEN_MODE = arguments.ZEN

    driver = webdriver.Chrome()
    driver.get(CONST.BASE_URL)

    wait_and_click_on_css = utils.create_waiter(
        driver, lambda element: element.click())
    wait_and_click_on_css(CONST.LOGIN["LOGIN_BUTTON"])

    utils.create_waiter(
        driver,
        lambda element: element.send_keys(
            arguments.Логин +
            "\n"))(
        CONST.LOGIN["INPUT_FIELD"])
    time.sleep(1)
    utils.create_waiter(
        driver,
        lambda element: element.send_keys(
            arguments.Пароль +
            "\n"))(
        CONST.LOGIN["INPUT_FIELD"])

    tasks.go_to_photo_moderation(driver, CONST.GUI_CHOICES[arguments.Задание])
    return driver


main()
