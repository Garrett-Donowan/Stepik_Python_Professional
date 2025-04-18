"""В онлайн-школе BEEGEEK каждое лето проходят соревнования по шахматам, во время которых 
ведется статистика побед и поражений. Каждая партия описывается кортежем из двух элементов, 
где первый элемент — имя победившего ученика, второй элемент — имя проигравшего ученика.

Реализуйте функцию wins(), которая принимает один аргумент:

pairs — итерируемый объект, элементами которого являются кортежи, каждый из которых 
представляет собой пару имён победитель-проигравший
Функция должна возвращать словарь, в котором ключом служит имя ученика, а значением — 
множество (тип set) имен учеников, которых он победил.

Примечание 1. Гарантируется, что каждая партия заканчивается победой одного из учеников, 
то есть ничьей быть не может.

Примечание 2. Элементы в возвращаемом функцией словаре могут располагаться в произвольном порядке.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию wins(), но не код, вызывающий ее."""

from collections import defaultdict

def wins(args):
    players = defaultdict(set)
    for k, v in args:
        players[k].add(v)
    return players
