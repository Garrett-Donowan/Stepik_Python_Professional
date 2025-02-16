"""Вам доступен файл countries.json, содержащий список JSON-объектов c информацией о 
странах и исповедуемых в них религиях:

[
   {
      "country": "Afghanistan",
      "religion": "Islam"
   },
   {
      "country": "Albania",
      "religion": "Islam"
   },
   ...
]
Каждый объект из этого списка содержит два атрибута:

country — страна
religion — исповедуемая религия
Напишите программу, которая создает единственный JSON-объект, имеющий в качестве 
ключа название религии, а в качестве значения — список стран, в которых исповедуется
данная религия. Полученный JSON-объект программа должна записать в файл religion.json.

Примечание 1. Страны в списках должны располагаться в своем исходном порядке.

Примечание 2. Начальная часть файла religion.json выглядит так:

{
   "Islam":[
      "Afghanistan",
      "Albania",
      "Algeria",
      ...
   ],
   ...
}"""


import json

dict = {}
with open('countries.json', encoding="UTF-8") as file:
    data = json.load(file)

for el in data:
    dict.setdefault(el["religion"], []).append(el["country"])


with open('religion.json', 'w', encoding='utf-8') as file: 
        json.dump(dict, file, separators=(', ', ': '), indent=3)