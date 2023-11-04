from data import REGISTRATION_PAGE
from lesson4.pom_practice.pages.registration_page import RegistrationPage


class TestRegistration():
    def test_registration_positive(self, driver, random_email):
        page = RegistrationPage(driver, url=REGISTRATION_PAGE)

        page.open()

        assert page.header().text == 'Практика с ожиданиями в Selenium'

        page.start_testing_button().click()

        page.login_field().clear()
        page.login_field().send_keys(random_email)

        page.password_field().clear()
        page.password_field().send_keys(random_email)

        page.agree_checkbox().click()
        assert page.agree_checkbox().is_selected() == True

        page.registration_button().click()

        assert page.loader().text == 'Загрузка...'

        assert page.success_message().text == "Вы успешно зарегистрированы!"
