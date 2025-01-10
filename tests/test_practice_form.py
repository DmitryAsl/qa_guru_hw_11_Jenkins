from helpers.pages.registration_page import RegistrationPage
from helpers.users import test_user


def test_registration_form():
    registration_form = RegistrationPage()
    registration_form.open()
    registration_form.register(test_user)

    registration_form.should_registered_user_with(test_user)
