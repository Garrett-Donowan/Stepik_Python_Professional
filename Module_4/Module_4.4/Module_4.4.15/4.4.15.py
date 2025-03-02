"""Вам доступен файл food_services.json, содержащий список JSON-объектов, которые 
представляют данные о заведениях общественного питания:

[
   {
      "Name": "СМЕТАНА",
      "IsNetObject": "нет",
      "OperatingCompany": "",
      "TypeObject": "кафе",
      "AdmArea": "Северо-Восточный административный округ",
      "District": "Ярославский район",
      "Address": "город Москва, улица Егора Абакумова, дом 9",
      "SeatsCount": 48
   },
   ...
]
Под «заведением» будем подразумевать один JSON-объект из этого списка.
У заведения имеются следующие атрибуты:

Name — название 
IsNetObject — да\нет в зависимости от того, является ли заведение сетевым
OperatingCompany — название сети
TypeObject — вид (кафе, столовая, ресторан и т.д.)
AdmArea — административная зона
District — район
Address — полный адрес
SeatsCount — количество мест
Напишите программу, которая:

определяет район Москвы, в котором находится больше всего заведений, и выводит название 
этого района и количество заведений в нем
определяет сеть с самым большим числом заведений и выводит название этой сети и 
количество заведений этой сети
Полученные значения программа должна вывести в следующем формате:

<район>: <количество заведений>
<название сети>: <количество заведений>
Примечание 1. Гарантируется, что искомая сеть единственная.

Примечание 2. Пример вывода:

район Метрогородок: 456
Французская пекарня SeDelice: 144"""


import json
from collections import defaultdict

operatingCompany_count = defaultdict(int)
district_count = defaultdict(int)
with open('food_services.json', encoding="UTF-8") as file:
    data = json.load(file)
    for el in data:
        if (el["OperatingCompany"] != ""):
            operatingCompany_count[el["OperatingCompany"]] += 1
        district_count[el["District"]] += 1
operatingCompany_count = sorted(operatingCompany_count.items(), key = lambda x: x[1], reverse= True)[0]
district_count = sorted(district_count.items(), key = lambda x: x[1], reverse= True)[0]
print(f"{district_count[0]}: {district_count[1]}")
print(f"{operatingCompany_count[0]}: {operatingCompany_count[1]}")