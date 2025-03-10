"""Реализуйте функцию get_min_max(), которая принимает один аргумент:

dates — список дат (тип date)
Функция должна возвращать кортеж, первым элементом которого является 
минимальная дата из списка dates, вторым — максимальная дата из списка dates. 
Если список dates пуст, функция должна вернуть пустой кортеж.

Примечание 1. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию get_min_max(), но не код, вызывающий ее."""


from datetime import date

def get_min_max(dates):
    if dates:
        return (min(dates), max(dates))
    else:
        return ()

# TEST_1:
dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
print(get_min_max(dates))

# TEST_2:
print(get_min_max([]))

# TEST_3:
dates = [date(2021, 10, 5), date(2021, 10, 5), date(2021, 10, 5), date(2021, 10, 5)]

print(get_min_max(dates))

# TEST_4:
dates = [date(1999, 9, 9)]

print(get_min_max(dates))

# TEST_5:
print(get_min_max([date(5091, 6, 23), date(9881, 1, 21), date(1860, 1, 16), date(8365, 3, 6), date(5425, 1, 3), date(1017, 5, 9), date(892, 2, 22), date(499, 4, 15), date(596, 2, 28), date(714, 7, 1), date(3770, 7, 8), date(6604, 1, 5), date(2303, 5, 8), date(2527, 12, 12), date(6408, 1, 3), date(1569, 3, 16), date(4845, 5, 17), date(6148, 7, 9), date(6235, 10, 23), date(2370, 4, 3), date(7291, 12, 17), date(8224, 9, 15), date(5205, 4, 9), date(6948, 12, 7), date(2016, 10, 18), date(5930, 4, 20), date(8934, 5, 2), date(619, 5, 10), date(4837, 11, 15), date(6969, 6, 28), date(1456, 4, 18), date(3887, 4, 21), date(8908, 4, 26), date(9198, 11, 19), date(5366, 12, 24), date(5366, 8, 18), date(248, 10, 23), date(529, 4, 16), date(6133, 10, 13), date(3517, 2, 1), date(85, 3, 10), date(4929, 7, 1), date(2175, 12, 10), date(1056, 5, 25), date(4698, 9, 2), date(6168, 6, 8), date(2632, 11, 12), date(3323, 9, 12), date(8390, 1, 20), date(461, 3, 26)]))

# TEST_6:
print(get_min_max([date(5580, 4, 2), date(1353, 3, 24), date(1896, 9, 24), date(2709, 6, 13), date(5144, 11, 24), date(885, 10, 24), date(5841, 6, 5), date(3432, 4, 26), date(8540, 12, 5), date(1674, 1, 25), date(7766, 4, 11), date(6852, 12, 4), date(4165, 7, 25), date(3012, 4, 19), date(2601, 9, 18), date(6503, 10, 14), date(7807, 2, 19), date(7834, 4, 21), date(9663, 5, 13), date(2298, 7, 24), date(4556, 6, 27), date(3871, 3, 2), date(5433, 2, 20), date(5103, 9, 13), date(930, 8, 23)]))

# TEST_7:
print(get_min_max([date(1, 1, 1), date(1, 1, 1), date(1, 1, 1), date(1, 1, 1), date(1, 1, 1), date(1, 1, 1), date(1, 1, 1), date(1, 1, 1), date(1, 1, 1), date(1, 1, 1), date(1, 1, 1)]))
