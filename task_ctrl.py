"""
Урок 8. Работа с файлами
Дополнить справочник возможностью копирования данных из одного файла в другой. Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
Формат сдачи: ссылка на пулл-реквест в ваш репозиторий.

from random import *
import json
def new():
    name = input('Введите имя абонента')
    phone = input('Введите телефоны абонента через запятую ').split(',')
    email = input('Введите электронный адрес ')
    if "@" in email:
        phone_book[] = {'phones': phone, 'email': email}
    else:
        data_name = {'phones': phone}   
        
def save():
    with open("phone_book.json", "w", encoding = "utf-8") as fh:
        fh.write(json.dumps(phone_book, ensore_ascii = False))
    print('Абонент успешно добавлен в телефонную книгу')        
  """  
import json

phone_book =[]
name = input('введите имя')
phone = input('введите номер')    
data = {
  'name':name,
  'phone':phone
}

phone_book.append(data)
with open('phone_book.json','a')as file:
  json.dump(phone_book, file, indent=4, ensure_ascii=False)  
print('Абонент успешно добавлен в телефонную книгу')                
    
    
#def show()
    