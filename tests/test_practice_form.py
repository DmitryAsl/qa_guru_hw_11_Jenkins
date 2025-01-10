from helpers.pages.registration_page import RegistrationPage
from helpers.users import test_user
import allure


def test_registration_form(browser_config):
    with allure.step('Открытие формы регистрации'):
        registration_form = RegistrationPage()
        registration_form.open()
    with allure.step('Заполнение формы и отправка ее'):
        registration_form.register(test_user)
    with allure.step('Проверка данных регистрации'):
        registration_form.should_registered_user_with(test_user)
