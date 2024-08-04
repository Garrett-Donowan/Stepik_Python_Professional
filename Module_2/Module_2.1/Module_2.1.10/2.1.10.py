"""Анаграммы — это слова, которые состоят из одинаковых букв. Например:

адаптер — петарда
адресочек — середочка
азбука — базука
аистенок — осетинка
Реализуйте функцию filter_anagrams(), которая принимает два аргумента в следующем порядке:

word — слово в нижнем регистре
words — список слов в нижнем регистре
Функция должна возвращать список, элементами которого являются слова из списка words, 
которые представляют анаграмму слова word. Если список words пуст или не содержит анаграмм, 
функция должна вернуть пустой список.

Примечание 1. Слова в возвращаемом функцией списке должны располагаться в 
своем исходном порядке. 
Примечание 2. Считайте, что слово является анаграммой самого себя.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую
функцию filter_anagrams(), но не код, вызывающий ее."""


def filter_anagrams(s, sargs):
    return list(filter(lambda x: sorted(list(x)) == sorted(list(s)), sargs))




# INPUT DATA:

# TEST_1:
word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']

print(filter_anagrams(word, anagrams))

# TEST_2:
print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))

# TEST_3:
print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))

# TEST_4:
print(filter_anagrams('стекло', []))

# TEST_5:
print(filter_anagrams('крона', ['кротко', 'укроп', 'норка']))

# TEST_6:
print(filter_anagrams('чулки', ['лучик', 'чутко', 'кочка']))

# TEST_7:
print(filter_anagrams('клоун', ['колдун', 'кулон', 'уклон', 'кол']))

# TEST_8:
word = 'abba'
anagrams = ['aaab', 'dbcd', 'bdaa', 'badb']
print(filter_anagrams(word, anagrams))

