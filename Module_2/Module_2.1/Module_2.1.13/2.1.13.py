"""Реализуйте функцию spell(), которая принимает произвольное количество позиционных 
аргументов-слов и возвращает словарь, ключи которого — первые буквы слов, 
а значения — максимальные длины слов на эту букву.

Примечание 1. Если в функцию не передается ни одного аргумента, функция должна возвращать 
пустой словарь.
Примечание 2. Функция должна игнорировать регистр слов, при этом в результирующий 
словарь должны попасть именно буквы в нижнем регистре.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию, но не код, вызывающий ее."""


def spell(*lst):
    spell_dict = {}
    if lst:
        for el in sorted(lst, key=len, reverse=False):
            spell_dict[el[0].lower()] = len(el)
        return spell_dict
    return {}



    
# INPUT DATA:

# TEST_1:
words = ['Россия', 'Австрия', 'Австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

print(spell(*words))

# TEST_2:
print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))

# TEST_3:
words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))

# TEST_4:
print(spell())

# TEST_5:
words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
print(spell(*words))

# TEST_6:
words = ['aaaaa', 'aaaaa', 'aaaaa', 'aaaaa', 'aaaaa']
print(spell(*words))

# TEST_7:
words = ['a']
print(spell(*words))

# TEST_8:
words = ['a', 'ab', 'abc', 'abcd', 'ба', 'аб', 'абвгдеЁёёЁЁжбБбБввВ', 'ёёё', 'Ёаaа']
print(spell(*words))

