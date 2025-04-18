"""Вам доступен файл salary_data.csv, который содержит анонимную информацию о 
зарплатах сотрудников в различных компаниях. В первом столбце записано название компании, 
а во втором — зарплата очередного сотрудника:

company_name;salary
Atos;135000
ХайТэк;24400
Philax;128600
Инлайн Груп;43900
IBS;70600
Oracle;131600
Atos;91000
...
Напишите программу, которая упорядочивает компании по возрастанию средней зарплаты ее 
сотрудников и выводит их названия, каждое на отдельной строке. Если две компании 
имеют одинаковые средние зарплаты, они должны быть расположены в лексикографическом 
порядке их названий.

Примечание 1. Средняя зарплата компании определяется как отношение суммы всех зарплат 
к их количеству.

Примечание 2. Разделителем в файле salary_data.csv является точка с запятой, при этом 
кавычки не используются.

Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/518491/salary_data.csv
https://stepik.org/media/attachments/lesson/518491/clue_average_salary.txt"""



import csv
from collections import defaultdict


salary_dict = defaultdict(list)
avg_salary = {}
with open('salary_data.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    for row in rows:
        salary_dict[row["company_name"]].append(int(row["salary"]))
for k, v in salary_dict.items():
    avg_salary[k] = sum(v)/ len(v)
    
print(*sorted(avg_salary, key=lambda name: (avg_salary[name], name)), sep = "\n")