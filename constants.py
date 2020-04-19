import multiprocessing

ZEN_MODE = True
CORE_COUNT = multiprocessing.cpu_count()
BASE_URL = "https://toloka.yandex.ru/"


LOGIN = {
    "LOGIN_BUTTON" : r"//span[text()='Войти']",
    "INPUT_FIELD"  : r"//input[contains(@id,'passp-field')]",
    "ENTER"        : r"//div[@class='passp-button passp-sign-in-button']",
}

XPATH = {
    "BOOKMARKED"              : r'/html/body/div[1]/div/div[3]/div/div[1]/div/div/div/span[5]',
    "SIMPLE_PHOTO_MODERATION" : r"//div[contains(@class, 'snippet__title') and contains(text(),'одерация фотографий')]/../../div[2]/button",
    "LABEL"                   : r"//div[@class='img__container__imitation']",
    "SEND_BUTTON"             : r"//span[@class='base-action-button__text' and text() ='Отправить']/../..",
    "ANY"                     : r"//*",
    "IMAGES"                  : r"//div[@class='img__container']",
}

ZEN_MODE_XPATHS = {
    "ANSWER"      : r"//div[@class='answer']",
    "RADIOBUTTON" : r"//span[@class='radio__i']/..",
    "NOT_RADIO_BUTTONS" : r"//div[@class='answer']/*[not(contains(@style,'color'))]",
}

THIS  = "THIS"
STYLE = "STYLE"
ARG0  = r"arguments[0]"

CURRENT_ELEMENT = {
    "THIS" : {
                "STYLE"      : ARG0 + r".style",
                "INNER_HTML" : ARG0 + r".innerHTML",
                "ANCESTOR"   : ARG0 + r".parentNode",
             }


}

