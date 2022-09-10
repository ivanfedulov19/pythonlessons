# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

list = [2, 3, 5, 9, 3]
sum = 0
for item in range(len(list)):
    if item % 2 == 1:
        sum += list[item]
print(sum)
    

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


list = [2, 3, 4, 5, 6]
half = len(list)//2
list3 = []
if len(list) % 2 == 0:
    list1 = list[:half]
    list2 = list[half:]
    list2.reverse()
    for i in range(len(list1)):
        list3.append(list1[i] * list2[i])
    print(list3)

elif len(list) % 2 == 1:
    list1 = list[:half]
    list2 = list[half + 1:]
    list2.reverse()
    for i in range(len(list1)):
        list3.append(list1[i] * list2[i])
    list3.append(list[half]**2)
    print(list3)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 10.01]
list2 = []
for i in range(len(list)):
    list2.append(round((list[i] - (list[i]//1)), 2))
print(list2)
print(max(list2) - min(list2))


# Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = 45
list = []

while number != 0:
    list.append(number % 2)
    number = number // 2
list.reverse()
for i in range(len(list)):
    list[i] = str(list[i])

result = ''.join(list)
print(result)


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число k: '))

lst = []
def fibonachi(x):
    if x < 2:
        return 1
    else:
        return fibonachi(x - 1) + fibonachi(x - 2)
        
for i in range(0,k):
    lst.append(fibonachi(i))

list2 = tuple(lst)
list2 = list(list2)
for i in range(len(list2)):
    if i % 2 == 1:
        list2[i] *= -1

list2.reverse()
list2.append(0)
list2.extend(lst)
print(list2)
