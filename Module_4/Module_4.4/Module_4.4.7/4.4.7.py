"""Вам доступен файл data.json, содержащий список различных объектов:

[
   "nwkWXma",
   null,
   {
      "ISgHT": "dIUbf"
   },
   "Pzt",
   "BXcbGVTE",
   ...
]
Напишите программу, которая создает список, элементами которого являются объекты из списка, 
содержащегося в файле data.json, измененные по следующим правилам:

если объект является строкой, в его конец добавляется восклицательный знак
если объект является числом, он увеличивается на единицу
если объект является логическим значением, он инвертируется
если объект является списком, он удваивается
если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
если объект является пустым значением (null), он не добавляется
Полученный список программа должна записать в файл updated_data.json.

Примечание 1. Например, если бы файл data.json имел вид:

["Hello", 179, true, null, [1, 2, 3], {"key": "value"}]
то программа должна была бы создать файл updated_data.json со следующим содержанием:

["Hello!", 180, false, [1, 2, 3, 1, 2, 3], {"key": "value", "newkey": null}]"""



import json

def process_data(data):
    data_type = type(data)
    if data_type == str:
        return data + '!'
    elif data_type == int:
        return data + 1
    elif data_type == bool:
        return not data
    elif data_type == list:
        return data + data
    elif data_type == dict:
        data.update(newkey=None)
        return data
    else:
        pass
    
output = []
with open('data.json', encoding="UTF-8") as file:
    data = json.load(file)
for el in data:
    if el != None:
        output.append(process_data(el))

with open('updated_data.json', 'w', encoding='utf-8') as file: 
        json.dump(output, file, separators=(', ', ': '))


