from seleniumpagefactory import PageFactory

class SendedEmailPage(PageFactory):
    locators = {
        "title_of_email": ('XPATH', "")
        # заголовок письма в окне отправленных писем
    }

    def __init__(self, driver):
        self.driver = driver

    def open_email(self, mail_content):
        self.locators["title_of_email"] = ('XPATH', "//span[@title='{}']".format(mail_content["to"]))
        self.title_of_email.click_button()