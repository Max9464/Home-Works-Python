
#  Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# # Пример:
# # [2, 3, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# my_list = [5, 3, 6, 8, 3, 1]
# odd_sum = 0
# for i in my_list:
#     if i % 2 != 0:
#         odd_sum += i
#
# print(odd_sum)

# новое решение
my_list = [5, 3, 6, 8, 3, 1]
print(sum(i for i in my_list if i % 2 != 0))

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


#
# list = [5,3,4,4,5]
# j = len(list)
# list_result = []
# print(list)
# for i in range(len(list)):
#     while i < len(list)/2 and j > len(list)/2:
#         j -= 1
#         a = list[i] * list[j]
#         list_result.append(a)
#         i += 1
# print(list_result)

#новое решение

# list = [5,3,4,4,5]
# list_result = []
# for i in range(len(list) // 2):
#     a = list[i] * list[len(list) - i - 1]
#     list_result.append(a)
# print(list_result)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
#

# a = int(input('Введите число '))
# b = ''
# while a > 0:
#     b = str(a % 2) + b
#     a = a // 2
# print(b)

#новое решение
# a = int(input('Enter a number: '))
# print(bin(a)[2:])




