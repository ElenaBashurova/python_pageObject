from pages.registration_page import PageRegistration
from data.user import user_text
from selene.support.shared.jquery_style import s
from selene import browser


def test_student_registration(browser_management):
    page = PageRegistration()
    page.open_browser()
    page.registration_student(user_text)
    page.should_text(user_text)
    page.close()


