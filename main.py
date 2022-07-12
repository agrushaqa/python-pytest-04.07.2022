import allure
import pyautogui
import pytest
from neoflex.LoginWizard import LoginWizard
from neoflex.MainYandexMailPage import MainYandexMailPage
from neoflex.SendMailPage import SendMailPage
from neoflex.DraftPage import DraftPage
from neoflex.SendedEmailPage import SendedEmailPage
from neoflex.ProfileMenuPage import ProfileMenuPage
from neoflex.ReadEmailPage import ReadEmailPage
import time
import logging
LOG_FILENAME = 'logging_autotest.txt'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

@allure.epic('Yandex')
@allure.feature('Auth')
class TestYandexMail:
    @allure.story('create draft')
    @allure.title('create draft letter in mail.yandex.ru')
    @allure.tag('author: agrusha')
    # @allure.severity(allure.severity_level.MINOR)
    @allure.link('https://mail.yandex.ru')
    def test_draft(self, draft_mail_content, mail_credentials, url, browser):
        allure.dynamic.description("""
        1. Авторизоваться в системе пользователем
        2. Нажать кнопку «Создать письмо» / «Написать письмо».
        3. Заполнить поля «Кому», «Тема» и «Тело» и сохранить письмо как черновик.
        4. Открыть папку с черновиками и проверить поля «Кому», «Тема» и «Тело» созданного письма
        5. Выход из системы с помощью нажатия «Выход»/«Выйти»""")
        try:
            login_wizard = LoginWizard(browser)
            main_window = MainYandexMailPage(browser)
            send_mail = SendMailPage(browser)
            draft_page = DraftPage(browser)
            profile_menu = ProfileMenuPage(browser)

            login_wizard.open(url)
            login_wizard.login(mail_credentials)

            main_window.open_profile_menu()
            profile_menu.check_user_email(mail_credentials)
            main_window.open(url)

            main_window.open_write_letter_page()
            send_mail.fill_content(draft_mail_content)

            main_window.open(url)
            main_window.open_draft_page()
            draft_page.open_draft_email(draft_mail_content)
            send_mail.check_draft(draft_mail_content)

            main_window.open(url)
            main_window.open_profile_menu()
            profile_menu.exit()
            login_wizard.check_relogin_form()
        except Exception as e:
            pytest.fail("an exception")
            logging.error(e, exc_info=True)
        finally:
            time.sleep(3)
            im1 = pyautogui.screenshot()
            im1.save('test_draft.png')
            login_wizard.delete_all_cookies()

    @allure.story('create letter')
    @allure.title('create letter in mail.yandex.ru')
    @allure.tag('author: agrusha')
    @allure.severity(allure.severity_level.MINOR)
    @allure.link('https://mail.yandex.ru')
    def test_send_letter(self, success_mail_content, mail_credentials, url, browser):
        allure.dynamic.description("""
        1. Авторизоваться в системе пользователем
        2. Нажать кнопку «Создать письмо» / «Написать письмо».
        3. Заполнить поля «Кому», «Тема» и «Тело» корректными/допустимыми данными и отправить письмо.
        4. Открыть папку с отправленными письмами и проверить поля «Кому», «Тема» и «Тело» отправленного письма
        5. Выход из системы с помощью нажатия «Выход»/«Выйти»""")
        login_wizard = LoginWizard(browser)
        main_window = MainYandexMailPage(browser)
        send_mail = SendMailPage(browser)
        profile_menu = ProfileMenuPage(browser)
        sended_email_page = SendedEmailPage(browser)
        read_email_page = ReadEmailPage(browser)
        try:
            login_wizard.open(url)
            login_wizard.login(mail_credentials)

            main_window.open_profile_menu()
            profile_menu.check_user_email(mail_credentials)
            main_window.open(url)

            main_window.open_write_letter_page()
            send_mail.fill_content(success_mail_content)
            send_mail.click_send_button()
            send_mail.check_email_send_notification()

            login_wizard.open(url)
            main_window.open_sended_email_page()
            sended_email_page.open_email(success_mail_content)
            read_email_page.check_email(success_mail_content)

            main_window.open(url)
            main_window.open_profile_menu()
            profile_menu.exit()
            login_wizard.check_relogin_form()
        except Exception as e:
            pytest.fail("an exception")
            logging.error(e, exc_info=True)
        finally:
            time.sleep(3)
            im1 = pyautogui.screenshot()
            im1.save('test_send_letter.png')
            login_wizard.delete_all_cookies()

