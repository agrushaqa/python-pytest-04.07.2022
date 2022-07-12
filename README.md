Тестовое задание по автоматизации тестирования.

В рамках тестового задания предлагается автоматизировать несколько тестов почтового ящика (например, на mail.yandex.ru или любом другом общедоступном почтовом сервисе).

Сценарии тестов почтового ящика:

|№ Теста | Действия | Ожидаемый результат (проверки) |
| ------------- |:-------------:| -----: |
|1 | 1. Авторизоваться в системе пользователем. Открыть меню Profile. | 1. Отображается на экране почта пользователя |
||2. Нажать кнопку «Создать письмо» / «Написать письмо». | 2.  Открылась форма создания нового письма |
||3. Заполнить поля «Кому», «Тема» и «Тело» и сохранить письмо как черновик. | 3. Письмо сохранилось как черновик (появилось сообщение/уведомление об этом, либо можно проверить статус письма, либо другой способ проверки) |
||4. Открыть папку с черновиками и проверить поля «От кого», «Тема» и «Тело» созданного письма | 4. «Кому», «Тема» и «Тело» письма заполнены данными |
||5. Выход из системы с помощью нажатия «Выход»/«Выйти» | 5. На странице появилось поле для ввода логина и/или пароля. |
|2 | 1. Авторизоваться в системе пользователем. Открыть меню Profile. | 1. Отображается на экране почта пользователя |
|| 2. Нажать кнопку «Создать письмо» / «Написать письмо». | 2. Открылась форма создания нового письма |
|| 3. Заполнить поля «Кому», «Тема» и «Тело» корректными/допустимыми данными и отправить письмо. | 3. Письмо отправилось успешно (появилось сообщение/уведомление об этом, либо можно проверить статус письма, либо найти в отправленных, либо другой способ проверки) |
|| 4. Открыть папку с отправленными письмами и проверить поля «Кому», «Тема» и «Тело» отправленного письма | 4. «Кому», «Тема» и «Тело» письма заполнены данными|
|| 5. Выход из системы с помощью нажатия «Выход»/«Выйти» | 5. На странице появилось поле для ввода логина и/или пароля. |

  В conftest.py
  вместо
        "user": "xxx@yandex.ru",
        "password": "xxx"
  нужно указать свой логин и пароль

<h2> how to install </h2>
  * https://docs.qameta.io/allure/#_installing_a_commandline
  * нужно в системные переменные PATH добавить путь к allure
  E:\prog\allure\allure-2.18.1\bin;
  * https://www.youtube.com/watch?v=xdjN-4UxL1c

  <h2> how to install pytest </h2>
  * pip install pytest
  * pip install allure-pytest
  * pip install pytest-adapter-allure
  * pip install selenium-page-factory
  * pip install pyautogui // create screenshot
  * pip install pytest-firefox
  * pip install webdriver-manager

  pytest-django - not install

  allure-pytest is the next version of pytest-allure-adaptor.

  check versions
  allure --version
  pytest --version

  run firefox
  * pytest main.py::TestYandexMail --alluredir="E:\python_scripts\code\neoflex\allure-results" --browser firefox

  run chrome
  * pytest main.py::TestYandexMail --alluredir="E:\python_scripts\code\neoflex\allure-results" --browser chrome


  run without· allure:
  * E:\python scripts\code\neoflex> pytest main.py::TestYandexMail

  run with allure:
  * pytest main.py::TestYandexMail --alluredir="E:\python_scripts\code\neoflex\allure-results"
  * pytest main.py::TestYandexMail::test_draft --alluredir="E:\python_scripts\code\neoflex\allure-results"
  * pytest main.py::TestYandexMail::test_send_letter --alluredir="E:\python_scripts\code\neoflex\allure-results"
  * pytest main2.py --alluredir=result

  allure serve E:\python_scripts\code\neoflex\allure-results


  pip install --upgrade pip
