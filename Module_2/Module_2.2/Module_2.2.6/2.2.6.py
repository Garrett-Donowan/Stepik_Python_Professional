"""Зачастую переводить сериалы, не теряя изначальный смысл, невозможно, особенно за счет игр слов. 
Сумасшедший режиссер хочет снять сериал, в котором бы в целях эксперимента задействовал 
как можно больше языков, чтобы пользоваться красотой каждого из них. Тем не менее если 
задействовать слишком много языков, то сериал станет непонятен абсолютно всем, поэтому 
режиссер достает случайных людей на улице и спрашивает их, какие языки они знают, таким 
образом он будет использовать языки которые знают все из них.

Напишите программу, которая определяет, какие языки будут использоваться в сериале.

Формат входных данных
На вход программе в первой строке подается число n — количество людей, которых донимает режиссер. 
В каждой из следующих n строк через запятую и пробел указывается список языков, 
которые знает человек.

Формат выходных данных
Программа должна вывести список языков для сериала в лексикографическом порядке.
Если такой список составить нельзя, необходимо вывести текст: 
Сериал снять не удастся"""


def read_input():s
    """Read input data from files

    Returns:
        output_data: dict of input data and answers
    """
    with open('Module_2\Module_2.2\Module_2.2.6\input.txt', 'r') as f, open('Module_2\Module_2.2\Module_2.2.6\output.txt', 'r') as o:
        i_data = []
        o_data = []
        raw1 = list(filter(lambda x: ("#" not in x) & (x != []) & (x != ""), [i.strip().replace(",", "").split() for i in f.readlines()]))
        raw2 = list(filter(lambda x: ("#" not in x) & (x != []) & (x != ""), [i.strip().replace(",", "").split() for i in o.readlines()]))
        for i in range(len(raw1)):
            if (raw1[i][0]).isdigit():
                test_data = []
                for z in range(1, int(raw1[i][0])+1):
                    cumulative = []
                    for j in range(len((raw1[z+i]))):
                        cumulative.append(raw1[i+z][j])
                    test_data.append(tuple(cumulative))
                i_data.append(tuple(test_data)) 
        for el in raw2:
            o_data.append((el))
        output_data = dict(zip(i_data, o_data))
    return output_data


def languages(*x):
    lang = {}
    output = []
    for el in x:
        for i in range(len(el)):
            lang[el[i]] = lang.get(el[i], 0) + 1
    for k, v in lang.items():
        if v == len(x):
            output.append(k)
    return sorted(output)
    

for k, v in (read_input()).items():
    if v == (languages(*k)) != []:
        print(*languages(*k), sep = ", ")
    elif (languages(*k)) == []:
        print("Сериал снять не удастся")
    else:
        print("False", end="")
        print(*languages(*k),"//", v)


