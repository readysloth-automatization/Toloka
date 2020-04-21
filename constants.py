import multiprocessing

ZEN_MODE = False
CORE_COUNT = multiprocessing.cpu_count()
BASE_URL = "https://toloka.yandex.ru/"

CACHE_FILE = ".cache.json"

GUI_CHOICES = {
    'Простая модерация фотографий': "SIMPLE_PHOTO_MODERATION",
    'Модерация фотографий организаций': "ORGANIZATION_PHOTO_MODERATION",
}

LOGIN = {
    "LOGIN_BUTTON": r"//span[text()='Войти']",
    "INPUT_FIELD": r"//input[contains(@id,'passp-field')]",
    "ENTER": r"//div[@class='passp-button passp-sign-in-button']",
}

BEGIN_BUTTON = "/../../div[2]/button"
TASKS = {
    "ORGANIZATION_PHOTO_MODERATION": r"//div[contains(@class, 'snippet__title') and contains(text(),'Модерация фотографий организаций')]" +
    BEGIN_BUTTON,
    "SIMPLE_PHOTO_MODERATION": r"//div[contains(@class, 'snippet__title') and contains(text(),'Простая модерация фотографий')]" +
    BEGIN_BUTTON,
}

XPATH = {
    "BOOKMARKED": r'/html/body/div[1]/div/div[3]/div/div[1]/div/div/div/span[5]',
    "LABEL": r"//div[@class='img__container__imitation']",
    "SEND_BUTTON": r"//span[@class='base-action-button__text' and text() ='Отправить']/../..",
    "ANY": r"//*",
    "IMAGES": r"//div[@class='img__container']",
    "CURRENT_TASK": r"//div[@class='task task_focused']",
}

ZEN_MODE_XPATHS = {
    "ANSWER": r"//div[@class='answer']",
    "RADIOBUTTON": r"//span[@class='radio__i']/..",
    "NOT_RADIO_BUTTONS": r"//div[@class='answer']/*[not(contains(@style,'color'))]",
    "ANNOTATIONS": r"//div[@class='field__hotkey']",
}

THIS = "THIS"
STYLE = "STYLE"
ARG0 = r"arguments[0]"

CURRENT_ELEMENT = {
    "THIS": {
        "STYLE": ARG0 + r".style",
        "INNER_HTML": ARG0 + r".innerHTML",
        "ANCESTOR": ARG0 + r".parentNode",
    }
}

FUNCTION_DICT = {}
