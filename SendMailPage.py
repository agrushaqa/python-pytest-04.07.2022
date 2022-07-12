from seleniumpagefactory import PageFactory

class SendMailPage(PageFactory):
    locators = {
        "to": ('ID', "compose-field-1"),
        # поле ввода Кому
        "to_without_avatar": ('XPATH', "//div[@id='compose-field-1']//div[@class='ComposeYabble-Text']"),
        # поле ввода Кому содержит аватар, поэтому читаем email Кому из дочернего локатора
        "subject": ('XPATH', "//input[@name='subject']"),
        # Тема письма
        "subject_caption": ('XPATH', "//div[@class='ComposePopup-Head']//span[@class='composeHeader-Title']"),
        # Заголовок письма
        "body": ('XPATH', "//div[@role='textbox']"),
        # Тело письма
        "auto_save_as_draft": ('XPATH', "//span[@class='composeHeader-SavedAt']"),
        # через пару секунд появляется сообщение о том, что сообщение сохранено в черновиках
        "button_send": ('XPATH', "//div[@class='ComposeSendButton-Text']/../.."),
        # кнопка Отправить
        'success':('XPATH', "//span[text()='Письмо отправлено']")
    }

    def __init__(self, driver):
        self.driver = driver

    def fill_content(self, mail_content):
        self.to.set_text(mail_content["to"])
        self.subject.set_text(mail_content["subject"])
        self.body.set_text(mail_content["body"])
        self.auto_save_as_draft.visibility_of_element_located()

    def check_draft(self, mail_content):
        assert self.to_without_avatar.get_text() == mail_content["to"],\
            f"to contains text: {self.to_without_avatar.get_text()}"
        assert self.subject_caption.get_text() == mail_content["subject"], \
            f"subject contains text: {self.subject_caption.get_text()}"
        assert self.body.get_text() == mail_content["body"], f"body contains text: {self.body.get_text()}"

    def click_send_button(self):
        self.button_send.click_button()

    def check_email_send_notification(self):
        self.success.visibility_of_element_located()