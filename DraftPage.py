from seleniumpagefactory import PageFactory


class DraftPage(PageFactory):
    locators = {
        "title_of_draft_email": ('XPATH', "")
        # заголовок письма, которое мы хотим открыть в окне черновиков
    }

    def __init__(self, driver):
        self.driver = driver

    def open_draft_email(self, draft_mail_content):
        self.locators["title_of_draft_email"] = ('XPATH', "//span[@title='{}']".format(draft_mail_content["to"]))
        self.title_of_draft_email.click_button()
