"""Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, 
которая выводит название файла из этого архива, который имеет наилучший показатель степени сжатия.

Примечание 1. Если файл находится в папке, вывести следует только название без пути.

Примечание 2. Гарантируется, что в исходном архиве только один файл имеет наилучший 
показатель степени сжатия.

Примечание 3. Степень сжатия файла характеризуется коэффициентом K, определяемым 
как отношение объема сжатого файла Vc к объему исходного файла, выраженным в процентах:

K=Vc / Vo *100%"""


from zipfile import ZipFile

best_compress_size = [1, 0]

with ZipFile('workbook.zip') as zip_file:
    files_list = (list(filter(lambda x: not x.is_dir(), zip_file.infolist())))
    for el in files_list:
        k = (el.compress_size / el.file_size)
        if k < best_compress_size[0]:
            best_compress_size[0] = k
            best_compress_size[1] = el.filename
print(f"{best_compress_size[1].split('/')[-1]}")
