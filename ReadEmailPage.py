from seleniumpagefactory import PageFactory

class ReadEmailPage(PageFactory):
    locators = {
        "to": ('XPATH', "//div[@title='1 получатель']/div"),
        "subject": ('XPATH', "//h1[contains(@class,qa-MessageViewer-Title-text)]"),
        "body": ('XPATH', "//div[contains(@class,'MessageBody')]"),
    }

    def __init__(self, driver):
        self.driver = driver

    def check_email(self, mail_content):
        self.locators["to"] = ('XPATH', "//div[text()='{}']".format(mail_content["to"]))

        assert self.to.get_text() == mail_content["to"],\
            f"to contains text: {self.to_without_avatar.get_text()}"
        assert self.subject.get_text() == mail_content["subject"], \
            f"subject contains text: {self.subject_caption.get_text()}"
        assert self.body.get_text() == mail_content["body"], f"body contains text: {self.body.get_text()}"