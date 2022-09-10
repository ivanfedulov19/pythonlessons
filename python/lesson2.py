# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 0,56 -> 11

number = (input('Введите дробное число c разделителем \'точка\': '))
result = number.split('.')

is_int = int(result[0])
is_fl = int(result[1])

sum = 0

while (is_int != 0):
    sum = sum + (is_int % 10)
    is_int = is_int // 10
while (is_fl != 0):
    sum = sum + (is_fl % 10)
    is_fl = is_fl // 10
print(f'Сумма цифр равна: {sum}')

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)

n = int(input('Введите любое число: '))
print(factorial(n))
    
# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

list = []

for i in range(1,6):
    i = (1 + (1/i))**i
    list.append(i)

print(sum(list))


# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

n = int(input('Введите число N: '))
list = []

for i in range(-n, n+1):
    list.append(i)

elements = (input('Введите позиции элементов, которые хотите перемножить: '))
list2 = (elements.split(' '))

for i in range(len(list2)):
    list2[i] = int(list2[i])

multi = 1

for i in range(len(list2)):
    multi = multi * list[list2[i]]

print(multi)

# Реализуйте алгоритм перемешивания списка.

import random

list = [4, 7, 2 , 45, 231, 65]

random.shuffle(list) # сам не додумался, как можно реализовать перемешивание
random.shuffle(list)
random.shuffle(list)

print(list)