import os
from selene import browser, have, command
from helpers.users import User


class RegistrationPage:

    def __init__(self):
        self.subjectsInput = browser.element('#subjectsInput')

    def open(self):
        browser.open('/automation-practice-form')

    def __fill_firstname(self, value):
        browser.element('#firstName').type(value)

    def __fill_lastname(self, value):
        browser.element('#lastName').type(value)

    def __fill_email(self, email):
        browser.element('#userEmail').type(email)

    def __fill_gender(self, gender):
        browser.element(f'input[value={gender}]').perform(command.js.click)

    def __fill_mobile(self, mobile):
        browser.element('#userNumber').type(mobile)

    def __fill_birthday(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.all('.react-datepicker__year-select option').element_by(have.text(year)).click()
        browser.element('.react-datepicker__month-select').click()
        browser.all('.react-datepicker__month-select option').element_by(have.text(month)).click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def __fill_subjects(self, subjects):
        if not subjects:
            raise ValueError('Список предметов не может быть пуст')
        self.subjectsInput.click().type(subjects[0])
        browser.all('.subjects-auto-complete__menu').element_by(have.text(subjects[0])).click()
        for subject in subjects[1:]:
            self.subjectsInput.click().type(subject).press_enter()

    def __fill_hobbby(self, hobby):
        browser.all('.custom-checkbox label').element_by(have.text(hobby)).click()

    def __fill_picture(self, name):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'data', name))
        browser.element('#uploadPicture').send_keys(full_path)

    def __submit(self):
        browser.element("#submit").click()

    def __fill_address(self, address):
        browser.element('#currentAddress').type(address)

    def __fill_state(self, state):
        browser.element('#state').click()
        browser.all('[id^="react-select-3-option"]').element_by(have.text(state)).click()

    def __fill_city(self, city):
        browser.element('#city').click()
        browser.all('[id^="react-select-4-option"]').element_by(have.text(city)).click()

    def __assert_filled_state_and_city(self, state, city):
        browser.all('tr').element_by(have.text('State and City')).should(have.text(f'{state} {city}'))

    def __assert_filled_address(self, address):
        browser.all('tr').element_by(have.text('Address')).should(have.text(address))

    def __assert_filled_picture(self, picture):
        browser.all('tr').element_by(have.text('Picture')).should(have.text(os.path.basename(picture)))

    def __assert_filled_hobby(self, hobby):
        browser.all('tr').element_by(have.text('Hobbies')).should(have.text(hobby))

    def __assert_filled_subjects(self, subjects):
        result = f''
        for subject in subjects:
            result += f'{subject}, '
        browser.all('tr').element_by(have.text('Subjects')).should(have.text(result[:-2]))

    def __assert_filled_birthday(self, birth_day, birth_month, birth_year):
        browser.all('tr').element_by(have.text('Date of Birth')).should(
            have.text(f'{birth_day} {birth_month},{birth_year}'))

    def __assert_filled_mobile(self, mobile):
        browser.all('tr').element_by(have.text('Mobile')).should(have.text(mobile))

    def __assert_filled_gender(self, gender):
        browser.all('tr').element_by(have.text('Gender')).should(have.text(gender))

    def __assert_filled_email(self, email):
        browser.all('tr').element_by(have.text('Student Email')).should(have.text(email))

    def __assert_filled_full_name(self, firstname, lastname):
        browser.all('tr').element_by(have.text('Student Name')).should(have.text(f'{firstname} {lastname}'))

    def register(self, user: User):
        self.__fill_firstname(user.firstName)
        self.__fill_lastname(user.lastName)
        self.__fill_email(user.email)
        self.__fill_gender(user.gender)
        self.__fill_mobile(user.mobile)
        self.__fill_birthday(user.birth_day, user.birth_month, user.birth_year)
        self.__fill_subjects(user.subjects)
        self.__fill_hobbby(user.hobby)
        self.__fill_picture(user.picture)
        self.__fill_address(user.address)
        self.__fill_state(user.state)
        self.__fill_city(user.city)

        self.__submit()

    def should_registered_user_with(self, user: User):
        self.__assert_filled_full_name(user.firstName, user.lastName)
        self.__assert_filled_email(user.email)
        self.__assert_filled_gender(user.gender)
        self.__assert_filled_mobile(user.mobile)
        self.__assert_filled_birthday(user.birth_day, user.birth_month, user.birth_year)
        self.__assert_filled_subjects(user.subjects)
        self.__assert_filled_hobby(user.hobby)
        self.__assert_filled_picture(user.picture)
        self.__assert_filled_address(user.address)
        self.__assert_filled_state_and_city(user.state, user.city)
