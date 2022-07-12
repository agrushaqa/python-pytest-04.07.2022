from seleniumpagefactory import PageFactory

class MainYandexMailPage(PageFactory):
    locators = {
        "write_letter": ('XPATH', "//a[@href='#compose']"),
        # кнопка Написать (письмо)
        "draft_page": ('XPATH', "//a[@href='#draft']"),
        # Закладка Черновики
        "profile_menu": ('XPATH', "//div[@class='PSHeader-User']//a[@href='https://passport.yandex.ru']"),
        # Меню, которое появляется при щелчке по аватарке пользователя
        "sended_email_page": ('XPATH', "//a[@href='#sent']")
    }

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def open_write_letter_page(self):
        self.write_letter.click_button()

    def open_draft_page(self):
        self.draft_page.click_button()

    def open_profile_menu(self):
        self.profile_menu.click_button()

    def open_sended_email_page(self):
        self.sended_email_page.click_button()