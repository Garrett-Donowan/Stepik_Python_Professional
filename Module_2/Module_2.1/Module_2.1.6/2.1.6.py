"""Реализуйте функцию same_parity(), которая принимает один аргумент:

numbers — список целых чисел
Функция должна возвращать новый список, элементами которого являются числа из списка numbers, 
имеющие ту же четность, что и первый элемент этого списка.
Примечание 1. Числа в возвращаемом функцией списке должны располагаться в своем исходном порядке. 
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию same_parity(), но не код, вызывающий ее."""

def same_parity(numbers):
    return list(filter(lambda x: x % 2 == numbers[0] % 2, numbers))



# INPUT DATA:

# TEST_1:
print(same_parity([]))

# TEST_2:
print(same_parity([6, 0, 67, -7, 10, -20]))

# TEST_3:
print(same_parity([-7, 0, 67, -9, 70, -29, 90]))

# TEST_4:
print(same_parity([2]))

# TEST_5:
print(same_parity([2, 2, 2, 2, 3, 0, 2, 3]))

# TEST_6:
print(same_parity([-1, 1248234832443, 8]))

# TEST_7:
print(same_parity([1, 2, 4, 6, 8]))

# TEST_8:
print(same_parity([1, 3, 5, 7, 9]))
