"""Дана последовательность неотрицательных целых чисел. Напишите программу, которая 
выводит те числа, которые встречаются в данной последовательности более одного раза.

Формат входных данных
На вход программе подается строка, содержащая целые неотрицательные числа, разделенные пробелом.

Формат выходных данных
Программа должна вывести те числа, которые встречаются в данной строке более одного раза, 
разделяя их пробелом. Числа должны быть расположены в порядке возрастания и не должны повторяться.

Примечание 1. 
Если повторяющихся чисел в исходной строке нет, программа ничего не должна выводить."""


def read_input():
    """Read input data from files

    Returns:
        output_data: dict of input data and answers
    """
    with open('Module_2\Module_2.2\Module_2.2.4\input.txt', 'r') as f, open('Module_2\Module_2.2\Module_2.2.4\output.txt', 'r') as o:
        i_data = []
        o_data = []
        flag = True
        raw1 = list(filter(lambda x: ("#" not in x) & (x != []), [i.strip().split() for i in f.readlines()]))
        raw2 = list(filter(lambda x: ("#" not in x) & (x != []), [i.strip() for i in o.readlines()]))
        for el in raw1:
            i_data.append(tuple([int(x) for x in el]))
        for i in range(1, len(raw2)):
            if (raw2[i] != "") & (raw2[i-1] == ""):
                o_data.append([int(x) for x in raw2[i].split()])
                flag = False
            elif (raw2[i] == "") & (raw2[i-1] == "") & (not flag):
                o_data.append([int(x) for x in raw2[i].split()])
                flag = True
            else:
                pass   
        output_data = dict(zip(i_data, o_data))
    return output_data

def more(data):
    return sorted(filter(lambda i: data.count(i) > 1, set(data)))


for k, v in (read_input()).items():
    if v == (more(k)):
        print(*more(k))
    else:
        print("False", end="")
        print(more(k),"//", v)
