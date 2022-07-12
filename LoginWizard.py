from seleniumpagefactory import PageFactory
# from selenium import webdriver

class LoginWizard(PageFactory):
    locators = {
        "button_enter": ('XPATH',
                         "//div[@class='HeadBanner-ButtonsWrapper']//a[@href='https://passport.yandex.ru/auth?from=mail&origin=hostroot_homer_auth_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1']"),
        "button_enter_by_text": ('XPATH', "//div[@class='HeadBanner-ButtonsWrapper']//span[text()='Войти']/.."),
        # кнопка Войти на странице https://mail.yandex.ru/
        "yandex_login": ('ID', "passp-field-login"),
        # поле ввода email
        "enter_button_login_form": ('ID', "passp:sign-in"),
        # кнопка войти в окне вводе логина
        "yandex_password": ('ID', 'passp-field-passwd'),
        "enter_button_password_form": ('ID', "passp:sign-in"),
        # кнопка войти в окне вводе логина
        "skip_set_password": ('XPATH', "//a[@href='https://mail.yandex.ru/']"),
        # если у пользователя нет фотки может появится окно о том, что аватарку можно добавить
        "relogin_login": ('XPATH', "//div[@class='AuthPasswordForm-currentAccount']"),
        # после logout в поле логина email указан
        "relogin_password": ('ID', "passp-field-passwd")
    }

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def login(self, mail_credentials):
        self.button_enter.click_button()
        self.yandex_login.set_text(mail_credentials["user"])
        self.enter_button_login_form.click_button()
        self.yandex_password.set_text(mail_credentials["password"])
        self.enter_button_password_form.click_button()
        # self.skip_set_password.click_button()

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()

    def check_relogin_form(self):
        self.relogin_login.visibility_of_element_located()
        self.relogin_password.visibility_of_element_located()