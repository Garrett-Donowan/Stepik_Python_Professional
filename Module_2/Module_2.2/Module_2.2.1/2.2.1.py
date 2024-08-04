"""Напишите программу, которая вычисляет минимальное расстояние, которое потребуется пройти
Тимуру, чтобы посетить оба магазина и вернуться домой. Тимур всегда стартует из дома. 
Он должен посетить оба магазина, перемещаясь только по имеющимся трём дорожкам, 
и вернуться назад домой. При этом его совершенно не смутит, если ему придётся посетить один 
и тот же магазин или пройти по одной и той же дорожке более одного раза. Единственная 
его задача — минимизировать суммарное пройденное расстояние.

Формат входных данных
На вход программе подаются 3 натуральных числа  d1, d2, d3 — длины дорожек, каждое на 
отдельной строке:
d1 — длина дорожки, соединяющая дом Тимура и первый магазин
d2 — длина дорожки, соединяющая дом Тимура и второй магазин
d3 — длина дорожки, соединяющая магазины
Формат выходных данных
Программа должна вывести минимальное количество метров, которое придётся пройти Тимуру, 
чтобы посетить оба магазина и вернуться домой."""


def read_input():
    """Read input data from files

    Returns:
        output_data: dict of input data and answers
    """
    with open('Module_2\Module_2.2\Module_2.2.1\input.txt', 'r') as f, open('Module_2\Module_2.2\Module_2.2.1\output.txt', 'r') as o:
        i_data = []
        o_data = []
        raw1 = list(filter(lambda x: ("#" not in x) & (x != []), [i.strip().split() for i in f.readlines()]))
        raw2 = list(filter(lambda x: ("#" not in x) & (x != []), [i.strip().split() for i in o.readlines()]))
        for i in range(0, len(raw1), 3):
            i_data.append((int(*raw1[i]), int(*raw1[i+1]), int(*raw1[i+2])))
        for i in range(len(raw2)):
            o_data.append(int(*raw2[i]))
        output_data = dict(zip(i_data, o_data))
    return output_data


def optimal_route(*data):
    """Calculates optimal route between places

    Returns:
        best_route: minimal distance between places according task
    """
    dist_list = [[data[0]*2 + data[1]*2], [data[0] + data[1] + data[2]], [data[0]*2 + data[2]*2], [data[1]*2 + data[2]*2]]
    return min(dist_list)


for k, v in (read_input()).items():
    if [v] == (optimal_route(*k)):
        print(*optimal_route(*k))
    else:
        print("False", end="")
        print(*optimal_route(*k))



