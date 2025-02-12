"""Вам доступен файл data.csv, который содержит неповторяющиеся данные о 
пользователях некоторого ресурса. В первом столбце записано имя пользователя, 
во втором — фамилия, в третьем — адрес электронной почты:

first_name,surname,email
John,Wilson,johnwilson@outlook.com
Mary,Wilson,marywilson@list.ru
...
Напишите программу, которая создает файл domain_usage.csv, имеющий следующее содержание:

domain,count
rambler.ru,24
iCloud.com,29
...
где в первом столбце записано название почтового домена, а во втором — количество 
пользователей, использующих данный домен. Домены в файле должны быть расположены 
в порядке возрастания количества их использований, при совпадении количества 
использований — в лексикографическом порядке.

Примечание 1. Разделителем в файле data.csv является запятая, при этом кавычки не используются.

Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/518491/data.csv
https://stepik.org/media/attachments/lesson/518491/clue_domains.txt"""

import csv

table = {}

with open('data.csv', encoding='utf-8') as file:
    data = file.read()
    table_raw = [r.split('@')[-1] for r in data.splitlines()]

for el in table_raw[1::]:
    table[el] = table.get(el, 0) + 1


with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["domain","count"])
    for k,v in sorted(table.items(), key= lambda x : (x[1], x[0])):                         
        writer.writerow([k, v])