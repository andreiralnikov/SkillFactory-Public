valid_email = "andruha1995@inbox.ru"
valid_pass = "qwer1995ANDRO"

invalid_email = 'andruha1995@inbox.com'
invalid_pass = 'qwerty'

name = 'Андрей'
surname = 'Ральников'
region = 'Москва г'
email = 'andreyralnikov@yandex.ru'
password = 'astro2001BOWIE'

false_email = '123456'
false_mobile_max = '8950817006798'
false_mobile_mini = '8950817006'
false_name_mini = 'А'
name_two_letters = "Ал"
thirty_letters = 'Бежатьчерезпеньколодувперёдраз'
thirty_one_letters = 'Бежатьчерезпеньколодувперёдпять'

class TestData:
    BASE_URL = 'https://b2c.passport.rt.ru/'

    # Названия заголовков элементов:
    FORM_AUTH_MAIL = 'Почта'
    AUTH = 'Авторизация'
    RECOVERY = 'Восстановление пароля'
    CHECK = 'Регистрация'
    VERIFICATION_EMAIL = 'Подтверждение email'
    VERIFICATION_INVALID_EMAIL = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    VERIFICATION_INVALID_NAME = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    ENTRY_VK = 'Войти'
    OK = 'Одноклассники'
    CHOICE_ACCOUNT = 'Вход'
    MM = 'Войти и разрешить'