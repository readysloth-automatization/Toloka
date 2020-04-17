
ZEN_MODE = False
BASE_URL              = "https://toloka.yandex.ru/"
CSS_SELECTORS = {
    "LOGIN_BUTTON"   : r"#content > div > div.main-layout__header > div.head.head_promo > div > div.head__panel > div > span > a",
    "LOGIN_FIELD"    : r"#passp-field-login",
    "LOGIN_ENTER"    : r"#root > div > div > div.passp-flex-wrapper > div > div > div.passp-auth-content > div                                                                                                         : nth-child(2) > div > div > div.passp-login-form > form > div.passp-button.passp-sign-in-button",
    "PASSWORD_FIELD" : r"#passp-field-passwd",
    "PASSWORD_ENTER" : r"#root > div > div > div.passp-flex-wrapper > div > div > div.passp-auth-content > div.passp-route-forward > div > div > form > div.passp-button.passp-sign-in-button",
}

XPATH = {
    "BOOKMARKED"              : r'/html/body/div[1]/div/div[3]/div/div[1]/div/div/div/span[5]',
    "SIMPLE_PHOTO_MODERATION" : r"//div[contains(@class, 'snippet__title') and contains(text(),'одерация фотографий')]/../../div[2]/button",
    "LABEL"                   : r"//div[@class='img__container__imitation']",
}

ZEN_MODE_XPATHS = {
    "ANSWER"      : r"//div[@class='answer']",
    "RADIOBUTTON" : r"//span[@class='radio__i']/..",
}
