"""Реализуйте функцию choose_plural(), которая принимает два аргумента в следующем порядке:

    amount — натуральное число, количество
    declensions — кортеж из трех вариантов склонения существительного
Функция должна возвращать строку, полученную путем объединения подходящего существительного 
из кортежа declensions и количества amount, в следующем формате:
    <количество> <существительное>
Примечание 1. Передаваемый в функцию кортеж легко составить по мнемоническому правилу: 
один, два, пять. Например:
    для слова «арбуз»: арбуз, арбуза, арбузов
    для слова «рубль»: рубль, рубля, рублей
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию choose_plural(), но не код, вызывающий ее."""

def choose_plural(amount, declensions):
        if (amount == 11) or (amount % 100 == 11) or (amount == 12) or (amount % 100 == 12) or (amount == 13) or (amount % 100 == 13) or (amount == 14) or (amount % 100 == 14):
            return f"{amount} {declensions[2]}"
        elif (amount == 1) or (amount % 10 == 1):
            return f"{amount} {declensions[0]}"
        elif (amount == 2) or (amount % 10 == 2) or (amount == 3) or (amount % 10 == 3) or (amount == 4) or (amount % 10 == 4):
            return f"{amount} {declensions[1]}"
        else: 
            return f"{amount} {declensions[2]}"




# INPUT DATA:

# TEST_1:
print(choose_plural(21, ('пример', 'примера', 'примеров')))

# TEST_2:
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))

# TEST_3:
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))

# TEST_4:
print(choose_plural(111223, ('копейка', 'копейки', 'копеек')))

# TEST_5:
print(choose_plural(763434, ('рубль', 'рубля', 'рублей')))

# TEST_6:
print(choose_plural(512312, ('цент', 'цента', 'центов')))

# TEST_7:
print(choose_plural(59, ('помидор', 'помидора', 'помидоров')))

# TEST_8:
print(choose_plural(23424157, ('огурец', 'огурца', 'огурцов')))

# TEST_9:
print(choose_plural(240, ('курица', 'курицы', 'куриц')))

# TEST_10:
print(choose_plural(49324, ('плюмбус', 'плюмбуса', 'плюмбусов')))

# TEST_11:
print(choose_plural(505, ('утка', 'утки', 'уток')))

# TEST_12:
print(choose_plural(666, ('шкаф', 'шкафа', 'шкафов')))

# TEST_13:
print(choose_plural(11, ('стул', 'стула', 'стульев')))

# TEST_14:
print(choose_plural(3458438435812, ('доллар', 'доллара', 'долларов')))

# TEST_15:
print(choose_plural(2, ('пример', 'примера', 'примеров')))

# TEST_16:
print(choose_plural(111, ('пример', 'примера', 'примеров')))

# TEST_17:
print(choose_plural(1223123111, ('пример', 'примера', 'примеров')))

