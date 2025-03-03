"""Вам доступен архив workbook.zip, содержащий различные папки и файлы. 
Напишите программу, которая выводит названия файлов из этого архива, 
которые были созданы или изменены позднее 2021-11-30 14:22:00. 
Названия файлов должны быть расположены в лексикографическом порядке, каждое на отдельной строке.

Примечание 1. Если файл находится в папке, вывести следует только название без пути.

Примечание 2. Начальная часть ответа выглядит так:

countries.json
data_sample.csv
..."""



from zipfile import ZipFile

modify_date = (2021, 11, 30, 14, 22, 0)
updated_workbook = []
with ZipFile('workbook.zip') as zip_file:
    files_list = (list(filter(lambda x: not x.is_dir(), zip_file.infolist())))
    for el in files_list:
        if (el.date_time > modify_date) & ("/" in el.filename):
            updated_workbook.append(el.filename.split("/")[1])
        elif (el.date_time > modify_date) & ("/" not in el.filename):
            updated_workbook.append(el.filename)
print(*sorted(updated_workbook), sep = "\n")
