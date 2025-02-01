"""Напишите программу, которая принимает на вход время и выводит целое количество секунд, 
прошедшее с начала суток.

Формат входных данных
На вход программе подается время в формате HH:MM:SS.

Формат выходных данных
Программа должна вывести целое количество секунд, прошедшее с начала суток.

Примечание 1. Началом суток считается момент времени, соответствующий 00:00:00."""

from datetime import time, datetime, timedelta

input_time = datetime.strptime(input(), "%H:%M:%S")

print(input_time.hour*3600 + input_time.minute*60 + input_time.second)

"""Sample Input 1:

00:01:01
Sample Output 1:

61
Sample Input 2:

00:00:00
Sample Output 2:

0
Sample Input 3:

12:12:12
Sample Output 3:

43932"""