"""Вам доступен архив workbook.zip, содержащий различные папки и файлы. 
Напишите программу, которая выводит суммарный объем файлов этого архива в 
сжатом и не сжатом видах в байтах, в следующем формате:

Объем исходных файлов: <объем до сжатия> байт(а)
Объем сжатых файлов: <объем после сжатия> байт(а)
Примечание 1. Вывод на примере архива test.zip из конспекта:

Объем исходных файлов: 7810260 байт(а)
Объем сжатых файлов: 7798267 байт(а)"""

from zipfile import ZipFile

compress_size = 0
file_size = 0
with ZipFile('workbook.zip') as zip_file:
    files_list = (list(filter(lambda x: not x.is_dir(), zip_file.infolist())))
    for el in files_list:
        compress_size += el.compress_size
        file_size += el.file_size
print(f"Объем исходных файлов: {file_size} байт(а)")
print(f"Объем сжатых файлов: {compress_size} байт(а)")
