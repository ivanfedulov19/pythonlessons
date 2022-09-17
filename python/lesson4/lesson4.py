# 1. Вычислить число c заданной точностью *d*
#     *Пример:* 
#     - при $d = 0.001, π = 3.141

import math
d = input('Введите число d: ')

list = d.split('.')
count = len(list[1])

result = round(math.pi,count)
print(result)

    
# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

import math

n = int(input('Введите натуральное число: '))
for i in range(2, int(math.sqrt(n)) + 1):
    while (n % i == 0):
        print(i)
        n //= i
if (n != 1): 
    print (n)
if (n == 1): 
    print (n)


# 3. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

lst = [1, 1, 2, 3, 4, 5, 5]
list2 = [i for i in lst if lst.count(i) == 1]
print(list2)


# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#     *Пример:* 
#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from sympy import *
from random import randint

def polycan(k,a,b,c):
    return f'{a} * x**{k} + {b} * x**{k-1} + {c} * x**{k-2}'

a = randint(0,101)
b = randint(0,101)
c = randint(0,101)
result = sympify(polycan(2,a,b,c))
print(result)

with open('task4.txt', 'w') as file:
    file.write(str(result))

# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# смог сделать реализацию только для многочленов с одинаковым количестом членов

from sympy import *

def delete_space(lst):
    for i in range(len(lst)):
        lst[i] = lst[i].strip()

def get_coeffs(lst1,lst2):
    for i in range(len(lst1)):
        lst2.append(lst1[i].split('*')[0])

def el_to_int(lst):
    for i in range(len(lst)):
        lst[i] = int(lst[i])

with open ('task5_1.txt','r') as file1:
    p1 = file1.read()

with open ('task5_2.txt','r') as file2:
    p2 = file2.read()

lst1 = p1.split('+')
lst2 = p2.split('+')

delete_space(lst1)
delete_space(lst2)

lst3 = []
lst4 = []

get_coeffs(lst1,lst3)
get_coeffs(lst2,lst4)

el_to_int(lst3)
el_to_int(lst4)

lst5 = []

for i in range(len(lst3)):
    lst5.append(lst3[i] + lst4[i])

result = f'{lst5[0]}*x**2 + {lst5[1]}*x + {lst5[i]}'
result = simplify(result)
print(result)