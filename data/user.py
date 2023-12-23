from dataclasses import dataclass


@dataclass
class User:
    last_name: str
    first_name: str
    email: str
    gender: str
    phone_number: str
    month: str
    year: str
    day: str
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str


user_text = User(
    last_name='Ivan',
    first_name='Romanov',
    email='romanov.i@mail.com',
    gender='Male',
    phone_number='9087658909',
    month='February',
    year='2002',
    day='03',
    subject='Maths',
    hobby='Reading',
    picture='images.jpeg',
    address='city Moscow, street Lenina',
    state='Haryana',
    city='Karnal'
)
