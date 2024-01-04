from selene import browser, by, have
from selene.support.shared.jquery_style import s
from locators.locator import Locators_Page as L


class PageRegistration:
    def open_browser(self):
        browser.open('/automation-practice-form')
        s(L.find_text_on_page).should(have.text('Student Registration Form'))
        return self

    def fill_first_name(self, first_name_text):
        s(L.first_name).type(first_name_text)
        return self

    def fill_last_name(self, last_name_text):
        s(L.last_name).type(last_name_text)
        return self

    def fill_email(self, email_text):
        s(L.email).type(email_text)
        return self

    def fill_gender(self):
        s(L.gender).double_click()
        return self

    def fill_number(self, number_phone_text):
        s(L.number_phone).type(number_phone_text)
        return self

    def fill_birthday(self, year, month, day):
        s(L.birthday_btn).click()
        s(L.birthday_month).click().element(by.text(month)).click()
        s(L.birthday_year).click().element(by.text(year)).click()
        s(f'.react-datepicker__day--0{day}').click()
        return self


    def fill_subjects(self, subject_text):
        s(L.subject).send_keys(subject_text).press_enter()
        return self

    def checkbox_hobbies(self):
        s(L.hobbies).click()
        return self

    def picture(self, picture):
        s(L.picture).set_value(picture)
        return self

    def fill_address(self, address_text):
        s(L.address).type(address_text)
        return self

    def fill_city(self, state_text, city):
        s(L.state).type(state_text).press_enter()
        s(L.city).type(city).press_enter()
        return self

    def submit_btn(self):
        s(L.submit_btn).click()
        return self

    def should_text(self, name, gender, email, number_phone, birthday, subject, hobby,
                    picture, address, city):
        s(L.should_text).should(have.text('Thanks for submitting the form'))
        browser.all('tbody tr td:last-child').should(have.exact_texts(
            name, email, gender, number_phone, birthday, subject,
            hobby, picture, address, city))
        return self

    def close(self):
        s(L.close).click()
        return self


    # def registration_student(self, user: User):
    #     s(L.first_name).type(user.first_name)
    #     s(L.last_name).type(user.last_name)
    #     s(L.email).type(user.email)
    #     s(L.gender).double_click()
    #     s(L.number_phone).type(user.phone_number)
    #     s(L.birthday_btn).click()
    #     s(L.birthday_month).click().element(by.text(user.month)).click()
    #     s(L.birthday_year).click().element(by.text(user.year)).click()
    #     s(L.birthday_day + user.day).click()
    #     s(L.subject).send_keys(user.subject).press_enter()
    #     s(L.hobbies).click()
    #     s(L.picture).set_value(resources_picture('images.jpeg'))
    #     s(L.address).type(user.address)
    #     s(L.state).type(user.state).press_enter()
    #     s(L.city).type(user.city).press_enter()
    #     s(L.submit_btn).click()
    #     return self
    #


