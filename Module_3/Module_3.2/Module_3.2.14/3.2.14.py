"""Тимур считает дату «интересной», если её год совпадает с годом его рождения, 
а сумма номера месяца и номера дня равна его возрасту. Год рождения Тимура — 
1992, возраст — 29 лет.

Реализуйте функцию print_good_dates(), которая принимает один аргумент:

dates — список дат (тип date)
Функция должна выводить «интересные» даты в порядке возрастания, каждую на отдельной строке, 
в формате  month_name DD, YYYY, где month_name — полное название месяца на английском. 

Примечание 1. Если в функцию передается пустой список или список без интересных дат, функция ничего не должна выводить.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию print_good_dates(), но не код, вызывающий ее.

"""

from datetime import date



def print_good_dates(dates):
    for el in sorted(dates):
        if (el.year == 1992) & (el.month+ el.day == 29):
            print(el.strftime("%B %d, %Y"))
    pass



# INPUT DATA:

# TEST_1:
dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)

# TEST_2:
dates = [date(1993, 9, 15), date(2021, 11, 2), date(2000, 7, 7)]
print_good_dates(dates)

# TEST_3:
print_good_dates([])

# TEST_4:
dates = [date(1992, 5, 24), date(1000, 1, 1), date(2000, 2, 2), date(3000, 3, 3)]
print_good_dates(dates)

# TEST_5:
dates = [date(1257, 8, 22), date(1765, 8, 23), date(1999, 9, 9), date(1992, 6, 23), date(1993, 1, 28)]
print_good_dates(dates)

# TEST_6:
dates = [date(1992, 9, 20), date(1992, 8, 21), date(1992, 7, 22), date(1992, 10, 19)]
print_good_dates(dates)

# TEST_7:
dates = [date(1257, 12, 12), date(1992, 6, 23), date(1284, 11, 2), date(1992, 1, 1)]
print_good_dates(dates)

# TEST_8:
print(print_good_dates([]))

