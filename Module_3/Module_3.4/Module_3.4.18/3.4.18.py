"""Реализуйте функцию num_of_sundays(), которая принимает на вход один аргумент:

year — натуральное число, год
Функция должна возвращать количество воскресений в году year.

Примечание 1. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию num_of_sundays(), но не код, вызывающий ее."""

from datetime import datetime

def  num_of_sundays(num_year):
    d = datetime(num_year, 12, 31)
    return d.strftime("%U")



print(num_of_sundays(int(input())))



"""Sample Input 1:

print(num_of_sundays(2021))
Sample Output 1:

52
Sample Input 2:

year = 2000
print(num_of_sundays(year))
Sample Output 2:

53
Sample Input 3:

print(num_of_sundays(768))
Sample Output 3:

52"""