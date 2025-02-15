"""Дан блок кода на языке Python. Напишите программу, которая удаляет все строки 
в данном коде, которые содержат в себе только комментарии. 
Если в строке помимо комментария имеется что-то еще, то такую строку учитывать не нужно.

Формат входных данных
На вход программе подается произвольное количество строк, 
в совокупности представляющих блок кода на языке Python.

Формат выходных данных
Программа должна вывести введенный блок кода, предварительно удалив 
из него все строки которые содержат в себе только комментарии.

Примечание 1. Порядок вывода строк кода должен совпадать с порядком их ввода."""

import sys

raw_data = [line for line in sys.stdin]

for el in raw_data:
    if not el.strip().startswith("#"):
        print(el, end = "")







"""Sample Input:

digit = int(input())
s = input()
for i in s:
    #комментирую потому что прикольно

    if 97 > ord(i) - digit:
        temp = ord(i) - digit + 26
        print(chr(temp), end='')   #вывод
    else:
        #ахаха
        temp = ord(i) - digit
        print(chr(temp), end='')
Sample Output:

digit = int(input())
s = input()
for i in s:

    if 97 > ord(i) - digit:
        temp = ord(i) - digit + 26
        print(chr(temp), end='')   #вывод
    else:
        temp = ord(i) - digit
        print(chr(temp), end='')"""