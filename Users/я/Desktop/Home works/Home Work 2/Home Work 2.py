# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# num = input('Введите число: ')
# sum = 0
# for a in num:
#     if a.isdigit():
#         sum += int(a)
#
# print(f"Сумма {num} равна: ", sum)

# 2.Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# n=int(input('Input n: '))
# any_lists = [round((1+1/i)**i, 3) for i in range(1, 1+n)]
# print(f'Последовательность чисел: {any_lists} \nСумма: {round(sum(any_lists), 3)}')



# 3.Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

import random
list = [0,1,2,3,4,5,6,7,8,9]
print ("Начальный список: " + str(list))
for i in range(len(list)-1, 0, -1):
    j = random.randint(0, i + 1)
    list[i], list[j] = list[j], list[i]
print ("Перемешанный список: " +  str(list))


