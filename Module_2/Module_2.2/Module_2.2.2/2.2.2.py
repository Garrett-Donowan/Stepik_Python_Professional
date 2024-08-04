"""В русском и английском языках есть буквы, которые выглядят одинаково. 
Вот список английских букв "AaBCcEeHKMOoPpTXxy", а вот их русские аналоги "АаВСсЕеНКМОоРрТХху". 
Напишите программу, которая для трёх букв из данных списков букв определяет, русские они, 
английские или и те и другие (смесь русских и английских букв).

Формат входных данных.На вход программе подаются три буквы из указанных в условии наборов букв, 
каждая на отдельной строке.

Формат выходных данных.Программа должна вывести

ru, если все три буквы русские
 en, если все три буквы английские
 mix, если среди букв есть как русские, так и английские
Примечание 1. Гарантируется, что введенные три буквы находятся в наборе 
"AaBCcEeHKMOoPpTXxy" + "АаВСсЕеНКМОоРрТХху" (английские + русские буквы)."""

def read_input():
    """Read input data from files

    Returns:
        output_data: dict of input data and answers
    """
    with open('Module_2\Module_2.2\Module_2.2.2\input.txt', 'r') as f, open('Module_2\Module_2.2\Module_2.2.2\output.txt', 'r') as o:
        i_data = []
        o_data = []
        raw1 = list(filter(lambda x: ("#" not in x) & (x != []), [i.strip().split() for i in f.readlines()]))
        raw2 = list(filter(lambda x: ("#" not in x) & (x != []), [i.strip().split() for i in o.readlines()]))
        for i in range(0, len(raw1), 3):
            i_data.append((*raw1[i], *raw1[i+1], *raw1[i+2]))
        for i in range(len(raw2)):
            o_data.append(*raw2[i])
        output_data = dict(zip(i_data, o_data))
    return output_data


def letters(*data):
    """detect to which language letters are belong

    Returns:
        str: locale of letters
    """
    en = 'AaBCcEeHKMOoPpTXxy'
    if all(map(lambda x: x in en, data)):
        return "en"
    elif any(map(lambda x: x in en, data)):
        return "mix"
    else:
        return "ru"

for k, v in (read_input()).items():
    if v == (letters(*k)):
        print(letters(*k))
    else:
        print("False", end="")
        print(letters(*k))
