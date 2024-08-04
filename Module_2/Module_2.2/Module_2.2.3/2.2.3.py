"""Дана последовательность натуральных чисел от 1 до n включительно. 
Напишите программу, которая сначала располагает в обратном порядке часть элементов 
этой последовательности от элемента с номером X до элемента с номером Y, а затем от 
элемента с номером A до элемента с номером B.

Формат входных данных.На вход программе подаются 5 натуральных чисел, разделенных пробелом: 
n,X, Y,A,B (X<Y,A<B,  1≤X,Y,A,B≤ n).

Формат выходных данных
Программа должна сформировать последовательность чисел, согласно условию задачи, и вывести их, 
разделяя пробелом.

Примечание 1. Нумерация членов последовательности начинается с единицы.
Примечание 2. Рассмотрим первый тест, в котором n=9,X=2,Y=5,A=6,B=9. 
Запишем последовательность от 1,2,3,4,5,6,7,8,9

Перевернем в этой последовательности сначала элементы со 2 по 5 (2,3,4,5), 
затем с 6 по 9 (6,7,8,9). Получим искомую последовательность:1,5,4,3,2,9,8,7,6 """

def read_input():
    """Read input data from files

    Returns:
        output_data: dict of input data and answers
    """
    with open('Module_2\Module_2.2\Module_2.2.3\input.txt', 'r') as f, open('Module_2\Module_2.2\Module_2.2.3\output.txt', 'r') as o:
        i_data = []
        o_data = []
        raw1 = list(filter(lambda x: ("#" not in x) & (x != []), [i.strip().split() for i in f.readlines()]))
        raw2 = list(filter(lambda x: ("#" not in x) & (x != []), [i.strip().split() for i in o.readlines()]))
        for el in raw1:
            i_data.append(tuple([int(x) for x in el]))
        for el in raw2:
            o_data.append([int(x) for x in el])
        output_data = dict(zip(i_data, o_data))
    return output_data

def rewerse(data):
    """rewerse  pointed positions of sequence

    Args:
        data (tuple): num of numbers, positions in list

    Returns:
        subsequence: list with rewersed positions
    """
    subsequence = [int(i+1) for i in range(data[0])]
    subsequence[data[1]-1:data[2]] = subsequence[data[1]-1:data[2]][::-1]
    subsequence[data[3]-1:data[4]] = subsequence[data[3]-1:data[4]][::-1]
    return subsequence

for k, v in (read_input()).items():
    if v == (rewerse(k)):
        print(rewerse(k))
    else:
        print("False", end="")
        print(rewerse(k), "//", v)
