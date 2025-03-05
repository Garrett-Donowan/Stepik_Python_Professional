"""Вам доступен архив data.zip, содержащий различные папки и файлы. 
Среди них есть несколько JSON файлов, каждый из которых содержит информацию о 
каком-либо футболисте:

{
   "first_name": "Gary",
   "last_name": "Cahill",
   "team": "Chelsea",
   "position": "Defender"
}
У футболиста имеются следующие атрибуты: 

first_name — имя
last_name — фамилия
team — название футбольного клуба
position — игровая позиция
Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и 
фамилии футболистов, выступающих за футбольный клуб Arsenal. Футболисты должны быть 
расположены в лексикографическом порядке имен, а при совпадении — в лексикографическом 
порядке фамилий, каждый на отдельной строке.

Примечание 1. Обратите внимание, что наличие у файла расширения .json не гарантирует, 
что он является корректным текстовым файлом в формате JSON. Для того чтобы определить, 
является ли файл корректным текстовым файлом в формате JSON, воспользуйтесь конструкцией 
try-except и функцией is_correct_json() из предыдущего урока.

Примечание 2. Начальная часть ответа выглядит так:

Alex Iwobi
Alexis Sanchez"""

from zipfile import ZipFile
import json


def extract_json(zip_name):
    players = []
    with ZipFile(zip_name) as zip_file:
        for el in list(filter(lambda el: el if ".json" in el.split('/')[-1] else "", zip_file.namelist())):
            with zip_file.open(el) as file:
                if is_correct_json(file.read()):
                    with open(zip_file.extract(el), encoding="UTF-8") as f:
                        data = json.load(f)
                        if data["team"] == "Arsenal":              
                                players.append([data["first_name"], data["last_name"]])
    for el in sorted(players, key= lambda x: [x[0],x[1]]):
        print(f"{el[0]} {el[1]}")
    return


def is_correct_json(str):
    try:
        json.loads(str)
        return True
    except Exception:
        return False


extract_json("data.zip")


