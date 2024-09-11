"""Вам доступен текстовый файл diary.txt, в который космонавт записывал небольшие отчёты за день. 
Каждый новый отчёт он мог записать либо в начало файла, либо в середину, либо в конец. 
Все отчеты разделены между собой пустой строкой. Каждый новый отчёт начинается со строки с датой 
и временем в формате DD.MM.YYYY; HH:MM, после которой следуют события, произошедшие за указанный день:

29.04.2006; 06:55
It wasn’t until several hours after launch that we were able to take the time to get out of our seats and enter the “habitation module.”
Then, after another orbital maneuver, we finally were able to take a several hour break and get a little sleep.

03.05.2006; 20:24
Everybody had a sleeping bag although I only used mine on a couple of brief occasions, and then only when getting a little chilly.
...
Напишите программу, которая расставляет все записи космонавта в хронологическом порядке и выводит полученный результат."""


from datetime import datetime


def read_file():
    with open("D:\Work\GitHub\Stepik_Python_Professional\Module_3\Module_3.3\Module_3.3.18\diary.txt", "r") as f:
        data_raw = [[i[:17], i[18:]] for i in f.read().split("\n\n")]
    return data_raw

def dividing():
    data = {}
    raw_data = read_file()
    for el in raw_data:
        data[datetime.strptime(el[0], "%d.%m.%Y; %H:%M").timestamp()] = el[1]
    data = dict(sorted(data.items()))
    count = 0
    for k, v in data.items():
        count += 1
        print((datetime.fromtimestamp(k).strftime('%d.%m.%Y; %H:%M')), v, sep="\n", end = "")
        if count != len(data):
            print("\n")
    return
    
dividing()