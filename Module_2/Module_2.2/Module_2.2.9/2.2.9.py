"""Вам доступен текстовый файл files.txt, содержащий информацию о файлах. Каждая строка файла содержит три значения, 
разделенные символом пробела — имя файла, его размер (целое число) и единицы измерения:

cant-help-myself.mp3 7 MB
keep-yourself-alive.mp3 6 MB
bones.mp3 5 MB
...
Напишите программу, которая группирует данные файлы по расширению, определяя общий объем файлов каждой группы, 
и выводит полученные группы файлов, указывая для каждой ее общий объем. Группы должны быть расположены в 
лексикографическом порядке названий расширений, файлы в группах — в лексикографическом порядке их имен.

Примечание 1. Например, если бы файл files.txt имел вид:

input.txt 3000 B
scratch.zip 300 MB
output.txt 1 KB
temp.txt 4 KB
boy.bmp 2000 KB
mario.bmp 1 MB
data.zip 900 MB
то программа должна была бы вывести:

boy.bmp
mario.bmp
----------
Summary: 3 MB

input.txt
output.txt
temp.txt
----------
Summary: 8 KB

data.zip
scratch.zip
----------
Summary: 1 GB
где Summary — общий объем файлов группы.

Примечание 2. Гарантируется, что все имена файлов содержат расширение.

Примечание 3. Общий объем файлов группы записывается в самых крупных (максимально возможных) единицах измерения 
с округлением до целых. Другими словами, сначала следует определить суммарный объем всех файлов группы, скажем, в байтах, 
а затем перевести полученное значение в самые крупные (максимально возможные) единицы измерения. Примеры перевода:

1023 B -> 1023 B
1300 B -> 1 KB
1900 B -> 2 KB
Примечание 4. Значения единиц измерения такие же, какие приняты в информатике:

1 KB = 1024 B
1 MB = 1024 KB
1 GB = 1024 MB
Примечание 5. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 6. При открытии файла используйте явное указание кодировки UTF-8."""
import re, math

def group_size(*args):
    data_group = {}
    extentions = []
    for el in args:
        data_group[(el[1])] = data_group.get((el[1]), [])  + [[el[0], el[1], el[2], el[3]]]
        data_group[(el[1])] = sorted(data_group[(el[1])])
    for k in data_group.keys():
        extentions.append(k)
    extentions = sorted(extentions)
    for el in extentions:
        summary = 0
        for i in range(len(data_group[el])):
            print(f"{data_group[el][i][0]}.{data_group[el][i][1]}")
            if data_group[el][i][3] == "GB":
                summary += int(data_group[el][i][2])*1024*1024*1024
            elif data_group[el][i][3] == "MB":
                summary += int(data_group[el][i][2])*1024*1024
            elif data_group[el][i][3] == "KB":
                summary += int(data_group[el][i][2])*1024
            else: 
                summary += int(data_group[el][i][2])
        print("----------")
        if (summary / 1024 < 1):
            print(f"Summary: {round(summary)} B")
        elif (summary / 1024 > 1) & (summary / 1024 < 1024):
            print(f"Summary: {round(summary / 1024)} KB")
        elif ((summary / (1024*1024))> 1) & ((summary / (1024*1024)) < 1024):
            print(f"Summary: {round(summary / 1024 / 1024)} MB")
        elif ((summary / (1024*2024*1024) ) > 1):
            print(f"Summary: {round(summary / 1024 / 1024 / 1024)} GB")
        print()
    return 


def read_file():
    with open("D:\Work\GitHub\Stepik_Python_Professional\Module_2\Module_2.2\Module_2.2.9\/files.txt", "r") as f:
        data_raw = [re.split("[. ]", i.rstrip()) for i in f.readlines()]
    return data_raw



group_size(*read_file())