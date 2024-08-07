"""Назовем набор различных натуральных чисел группой. Например: 
(13,4,22,40). Тогда длиной группы будем считать количество чисел в группе.
Например, длина группы (13,4,22,40) равна 4.

Дана последовательность натуральных чисел от 1 до n включительно. 
Напишите программу, которая группирует все числа данной последовательности 
по сумме их цифр и определяет длину группы, содержащей наибольшее 
количество чисел.

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна сгруппировать все числа из натуральной последовательности 
от 1 до n по сумме их цифр и определить длину группы, 
содержащей наибольшее количество чисел.

Примечание 1. Рассмотрим третий тест, в котором n=20. Запишем 
последовательность чисел от 1 до 20:
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
Сгруппируем полученные числа по сумме их цифр:
(1,10),(2,11,20),(3,12),(4,13),(5,14),(6,15),(7,16),(8,17),(9,18),(19)

Итак, длина группы с наибольшим количеством чисел равна 3."""

def read_input():
    """Read input data from files

    Returns:
        output_data: dict of input data and answers
    """
    with open('Module_2\Module_2.2\Module_2.2.5\input.txt', 'r') as f, open('Module_2\Module_2.2\Module_2.2.5\output.txt', 'r') as o:
        i_data = []
        o_data = []
        raw1 = list(filter(lambda x: ("#" not in x) & (x != []) & (x != ""), [i.strip().split() for i in f.readlines()]))
        raw2 = list(filter(lambda x: ("#" not in x) & (x != []) & (x != ""), [i.strip().split() for i in o.readlines()]))
        for el in raw1:
            i_data.append(int(*el))
        for el in raw2:
            o_data.append(int(*el))
        output_data = dict(zip(i_data, o_data))
    return output_data


def sum_nums(x):
    generated_sum = [sum(map(int, list(str(i)))) for i in range(1, x+1)]
    generated_list = [int(i) for i in range(1, x+1)]
    len_group = {}
    max = 0
    for i in range(len(generated_list)):
        len_group[generated_sum[i]] = len_group.get(generated_sum[i], []) + [generated_list[i]]
    for k, v in len_group.items():
        if max < len(v):
            max = len(v)
    return max
    

for k, v in (read_input()).items():
    if v == (sum_nums(k)):
        print(sum_nums(k))
    else:
        print("False", end="")
        print(sum_nums(k),"//", v)


