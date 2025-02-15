"""Дана последовательность дат. Напишите программу, 
которая выводит количество дней между максимальной и 
минимальной датами данной последовательности.

Формат входных данных
На вход программе подается произвольное количество строк, в 
каждой строке записана дата в ISO формате (YYYY-MM-DD).

Формат выходных данных
Программа должна вывести единственное число — количество дней 
между максимальной и минимальной датами введенной последовательности."""

import sys, datetime
from datetime import datetime, timedelta

dates = [datetime.strptime(i.strip(), '%Y-%m-%d') for i in sys.stdin]
print((sorted(dates)[-1] - sorted(dates)[0]).days)




"""Sample Input 1:

2022-06-15
2022-06-12
2022-06-16
2022-06-30
Sample Output 1:

18
Sample Input 2:

2077-01-01
2077-01-01
2077-01-01
Sample Output 2:

0"""