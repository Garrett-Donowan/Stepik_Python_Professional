"""В различных социальных сетях существуют системы лайков, которые в зависимости 
от количества людей, оценивших запись, показывают соответствующую информацию.

Реализуйте функцию likes(), которая принимает один аргумент:
names — список имён
Функция должна возвращать строку в соответствии с примерами ниже, содержание 
которой зависит от количества имён в списке names.

Приведенный ниже код:
print(likes([]))
print(likes(['Тимур']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))
должен выводить:
Никто не оценил данную запись
Тимур оценил(а) данную запись
Тимур и Артур оценили данную запись
Тимур, Артур и Руслан оценили данную запись
Тимур, Артур и 2 других оценили данную запись
Тимур, Артур и 3 других оценили данную запись
Тимур, Артур и 6 других оценили данную запись

Примечание 1. Имена в формируемой и возвращаемой функцией строке должны располагаться 
в своем исходном порядке.
Примечание 2. Обратите внимание, что если в передаваемом в функцию списке более трех имен, 
то явно указываются лишь первые два из них. 
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию likes(), но не код, вызывающий ее."""


def likes(names_list):
    if len(names_list) == 0:
        return f"Никто не оценил данную запись"
    if len(names_list) == 1:
        return f"{names_list[0]} оценил(а) данную запись"
    if len(names_list) == 2:
        return f"{names_list[0]} и {names_list[1]} оценили данную запись"
    if len(names_list) == 3:
        return f"{names_list[0]}, {names_list[1]} и {names_list[2]} оценили данную запись"
    if len(names_list) > 3:
        return f"{names_list[0]}, {names_list[1]} и {len(names_list) - 2} других оценили данную запись"

# INPUT DATA:

# TEST_1:
print(likes(['Дима', 'Алиса']))

# TEST_2:
print(likes(['Эндрю', 'Тоби', 'Том']))

# TEST_3:
print(likes([]))

# TEST_4:
print(likes(['Том']))

# TEST_5:
print(likes(['Эндрю', 'Тоби', 'Том', 'Артур']))

# TEST_6:
print(likes(['Эндрю', 'Тоби', 'Том', 'Артур', 'Тимур']))

# TEST_7:
print(likes(['Артур', 'Тимур', 'Руслан', 'Анри', 'Дима', 'Алиса']))

# TEST_8:
names = [str(i) * 3 for i in range(100)]
print(likes(names))