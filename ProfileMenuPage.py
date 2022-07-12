from seleniumpagefactory import PageFactory

class ProfileMenuPage(PageFactory):
    locators = {
        "exit_button": ('XPATH', "//a[@data-count='{\"name\":\"user-menu\",\"id\":\"exit\"}']"),
        # кнопка Выйти из сервисов Яндекса
        "user_email": ('XPATH', "//div[@class='legouser__menu-header']//span[@class='user-account__subname']")
        # email пользователя
    }

    def __init__(self, driver):
        self.driver = driver

    def exit(self):
        self.exit_button.click_button()

    def check_user_email(self, mail_credentials):
        assert self.user_email.get_text() == mail_credentials["user"]