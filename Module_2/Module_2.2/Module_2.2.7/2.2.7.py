"""Напишите программу, которая находит все схожие слова для заданного слова. 
Слова называются схожими, если имеют одинаковое количество и расположение гласных букв. 
При этом сами гласные могут различаться.

Формат входных данных
На вход программе подается одно слово, записанное в первой строке, 
затем натуральное число n — количество слов для сравнения и n строк со словами.

Формат выходных данных
Программа должна вывести все схожие слова для заданного слова, сохранив их 
исходный порядок следования.

Примечание 1. После последней гласной в начальном и проверяемом слове может 
быть любое количество согласных.

Примечание 2. В русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е) и 
21 согласная буква (б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ)."""

def similar(word, *words):
    vowels = 'а, у, о, ы, и, э, я, ю, ё, е'
    sample_similar = [i for i, ltr in enumerate(word) if ltr in vowels]
    output_data = []
    for el in words:
        w_list = [i for i, ltr in enumerate(el) if ltr in vowels]
        if (w_list == sample_similar):
            output_data.append(el)
    return output_data



print(similar(input(), *[input() for i in range(int(input()))]))