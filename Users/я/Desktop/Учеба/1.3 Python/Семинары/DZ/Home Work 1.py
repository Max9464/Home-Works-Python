# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# week_day = int(input('Input day of week: '))
# if week_day == 1 or 2 or 3 or 4 or 5:
#     print('Рабочий день')
# elif week_day == 6 or 7:
#     print('Выходной')
# else:
#     print('Error, out of range')


# 1. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


# 2.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input("Input x: "))
# y = int(input("Input y: "))
# if x == 0 or y == 0:
#     print('Error X ≠ 0, Y ≠ 0 '+'\n'+'Plese input numbers more then: 0')
# elif x > 0.1 and y > 0.1:
#     print('1')
# elif x < 0 and y > 0.1:
#     print('2')
# elif x < 0 and y < 0:
#     print('3')
# elif x > 0.1 and y < 0:
#     print('4')

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# quarter = int(input('Input qarter: '))
# if quarter == 1:
#     print('X = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10'+ '\n'
#           + 'Y = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10')
# elif quarter == 2:
#     print('X = -1, -2, -3, -4, -5, -6, -7, -8, -9, -10'+ '\n'
#           + 'Y = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10')
# elif quarter == 3:
#     print('X = -1, -2, -3, -4, -5, -6, -7, -8, -9, -10'+ '\n'
#           + 'Y = -1, -2, -3, -4, -5, -6, -7, -8, -9, -10')
# elif quarter == 4:
#     print('X = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10'+ '\n'
#           + 'Y = -1, -2, -3, -4, -5, -6, -7, -8, -9, -10')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
ax = float(input('Введите координаты точки a по оси x:'))
ay = float(input('Введите координаты точки a по оси y:'))
bx = float(input('Введите координаты точки b по оси x:'))
by = float(input('Введите координаты точки b по оси y:'))

import math
distans = math.sqrt((ax-bx)**2+(ay-by)**2)
print(f'Растояние между точкой A до точки B = {distans}' )
