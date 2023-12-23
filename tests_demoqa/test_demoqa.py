from pages.registration_page import PageRegistration
from resources_path.resources import resources_picture


def test_student_registration(browser_management_demoqa):
    page = PageRegistration()
    page.open_browser()

 #Регистрация студента

    page.fill_last_name('Ivan')
    page.fill_first_name('Romanov')
    page.fill_email('romanov.i@mail.com')
    page.fill_gender()
    page.fill_number('9087658909')
    page.fill_birthday('2002', 'February', '03')
    page.fill_subjects('Maths')
    page.checkbox_hobbies()
    page.picture(resources_picture('images.jpeg'))
    page.fill_address('city Moscow, street Lenina')
    page.fill_city('Haryana','Karnal')
    page.submit_btn()

#Проверка данных
    page.should_text(name='Romanov Ivan',
                     email='romanov.i@mail.com',
                     gender='Male',
                     number_phone='9087658909',
                     birthday='03 February,2002',
                     subject='Maths',
                     hobby='Reading',
                     picture='images.jpeg',
                     address='city Moscow, street Lenina',
                     city='Haryana Karnal')
    page.close()


