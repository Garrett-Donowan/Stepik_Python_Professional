"""Напишите программу, которая принимает на вход описание одного объекта в формате JSON 
и выводит все пары ключ-значение этого объекта.

Формат входных данных
На вход программе подается корректное описание одного объекта в формате JSON.

Формат выходных данных
Программа должна вывести все пары ключ-значение введенного объекта, разделяя ключ 
и значение двоеточием, каждую на отдельной строке. Если значением ключа является список, 
то все его элементы должны быть выведены через запятую.

Примечание 1. Пары ключ-значение при выводе должны располагаться в своем исходном порядке.

Примечание 2. Для считывания произвольного числа строк используйте потоковый ввод sys.stdin."""

import json, sys

data = json.loads(sys.stdin.read())
for k, v in data.items():
    if isinstance(v, list):
        v = ", ".join(map(str,v))
    print(f"{k}: {v}")
