"""Вам доступен архив workbook.zip, содержащий различные папки и файлы. 
Напишите программу, которая выводит названия всех файлов из этого архива в 
лексикографическом порядке, указывая для каждого его дату изменения, 
а также объем до и после сжатия, в следующем формате:

<название файла>
  Дата модификации файла: <дата изменения>
  Объем исходного файла: <объем до сжатия> байт(а)
  Объем сжатого файла: <объем после сжатия> байт(а)
Между данными о двух файлах должна располагаться пустая строка.

Примечание 1. Если файл находится в папке, вывести следует только название без пути.

Примечание 2. Начальная часть ответа выглядит так (в качестве отступов используйте два пробела):

Alexandra Savior – Crying All the Time.mp3
  Дата модификации файла: 2021-11-30 13:27:02
  Объем исходного файла: 5057559 байт(а)
  Объем сжатого файла: 5051745 байт(а)

Hollow Knight Silksong.exe
  Дата модификации файла: 2013-08-22 08:20:06
  Объем исходного файла: 805992 байт(а)
  Объем сжатого файла: 494930 байт(а)

..."""



from zipfile import ZipFile
from datetime import datetime

flag = False
updated_workbook = []
with ZipFile('workbook.zip') as zip_file:
    files_list = (list(filter(lambda x: not x.is_dir(), zip_file.infolist())))
    for el in files_list:
        if ("/" in el.filename):
            updated_workbook.append([el.filename.split("/")[1], datetime(*el.date_time), el.file_size, el.compress_size])
        elif ("/" not in el.filename):
            updated_workbook.append([el.filename, datetime(*el.date_time), el.file_size, el.compress_size])
for el in sorted(updated_workbook, key= lambda x: x[0]):
    if flag:
        print()
    print(f"{el[0]}")
    print(f"  Дата модификации файла: {el[1]}")
    print(f"  Объем исходного файла: {el[2]} байт(а)")
    print(f"  Объем сжатого файла: {el[3]} байт(а)")
    flag = True
