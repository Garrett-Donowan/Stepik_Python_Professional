"""Напишите программу, которая принимает на вход две даты и выводит ту, что меньше.

Формат входных данных
На вход программе подаются две корректные даты в ISO формате (YYYY-MM-DD), каждая на отдельной строке.

Формат выходных данных
Программа должна выбрать из двух введенных дат меньшую и вывести ее в формате DD-MM (YYYY)."""

from datetime import date

def comparator():
    dates = []
    for i in range(2):
        year, month, day= input().split('-')
        dates.append(date(int(year), int(month), int(day)))
    print(min(dates).strftime("%d-%m (%Y)"))


comparator()




""" INPUT DATA:

# TEST_1:
2021-05-12
2021-05-04

# TEST_2:
1999-07-14
1999-07-14

# TEST_3:
2016-05-12
2017-07-04

# TEST_4:
3016-05-12
3016-07-12
"""
