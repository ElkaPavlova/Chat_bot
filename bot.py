# coding: utf-8
import json
from random import *

def save():
    # with codecs.open("phone_book.json", "w", encoding="utf-8") as file:
    #     file.write(json.dumps(phone_book, ensure_ascii=False))

    with open("phone_book.json", "w") as outfile:
        json.dump(contacts, outfile)

     
    print("Данные сохранены в файле phone_book.json")

contacts = {"Ivanov Ivan": {'phones': [4567847, 888888889], 'email': '345677@mail.ru', 'birthday':'04.04.1990'},
            "Petrov Petr": {'phones': [11122223333], 'email': 'qwerty@mail.ru', 'birthday':'15.04.1987'},
            "Vasilev Vasya": {'phones': [6778890678], 'email': 'q7b78g9kl@mail.ru', 'birthday':'11.11.2000'}}

while True:
    command=raw_input("Введите команду: ")
    if command=="/all":
       print(contacts)
    elif command == "/find":
        contact_name = raw_input("Введите имя: ")
        print(contacts[contact_name])
    elif command == "/del":
        contact_name = raw_input("Введите имя: ")
        if contact_name in contacts:
            del contacts[contact_name]
            print("Запись успешно удалена")
        else:
            print("Контакт с таким именем не найден!")
    elif command == "/save":
        save()
    elif command == "/add":
        contact_name = raw_input("Введите имя: ")
        phones = raw_input("Введите номера телефонов через запятую: ").split(",")
        email = raw_input("Введите email через запятую: ").split(",")
        contact = {
            'phones': phones,
            'email': email,
            'birthday': raw_input("Введите день рождения: ")
        }
        contacts.update({contact_name: contact})
        print("Контакт успешно добавлен")
    elif command == "/load":
        with open("phone_book.json", "r") as outfile:
            contacts=json.load(outfile)
        print("Телефонный спраочник был успешно загружен!")

    elif command == "/exit":
        break