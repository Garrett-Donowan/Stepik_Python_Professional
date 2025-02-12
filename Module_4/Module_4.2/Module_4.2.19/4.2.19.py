"""Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя. 
В первом столбце записано измененное имя пользователя, во втором — адрес электронной почты, 
в третьем — дата и время изменения. При этом email пользователь менять не может, только имя:

username,email,dtime
rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
...
Напишите программу, которая отбирает из файла name_log.csv только самые свежие 
записи для каждого пользователя и записывает их в файл new_name_log.csv. 
В файле new_name_log.csv первой строкой должны быть заголовки столбцов такие же, 
как в файле name_log.csv. Логи в итоговом файле должны быть расположены в 
лексикографическом порядке названий электронных ящиков пользователей.

Примечание 1. Для части пользователей в исходном файле запись только одна, 
и тогда в итоговый файл следует записать только ее, для некоторых пользователей 
есть несколько записей с разными именами.

Например, пользователь с электронной почтой c3po@gmail.com несколько раз менял имя:

C=3PO,c3po@gmail.com,16/11/2021 17:10
C3PO,c3po@gmail.com,16/11/2021 17:15
C-3PO,c3po@gmail.com,16/11/2021 17:24
Из этих трех записей в итоговый файл должна быть записана только одна — самая свежая:

C-3PO,c3po@gmail.com,16/11/2021 17:24
Примечание 2. Разделителем в файле name_log.csv является запятая, при этом кавычки 
не используются."""

import csv 

table = {}

with open('name_log.csv', encoding='utf-8') as file:
    data = file.read()
    table_raw = [r.split(',')  for r in data.splitlines()]

for el in sorted(table_raw[1::], key= lambda x: x[1]):
    if el[1] not in table:
        table[el[1]] = [el[0], el[2]]
    elif (el[1] in table) & (el[2] > table[el[1]][1]):
        table[el[1]] = [el[0], el[2]]

with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(table_raw[0])
    for k,v in table.items():                         
        writer.writerow([v[0], k, v[1]])