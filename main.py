# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
print("Задача 1. Введите цифру означающую день недели от 1 до 7:")
day = int(input("Введите цифру означающую день недели от 1 до 7:"))
if 1 <= day <= 5:
    print('нет')
elif 6 <= day <= 7:
    print("да")
else:
    print("Ошибка вывода,попробуйте еще.")

# 2.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (расшифровка этого выражения not (x[0] or x[1] or and  x[2] = not x[0]not x[1] and not x[2]) для всех значений предикат.
print("Задача 2. Введите значения x, y, z:")
x, y, z = int(input()), int(input()), int(input())
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            print(x, 'AND', y, 'OR', z, '=', x and y or z)

# 3Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .
print("Задача 3. Введите координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0:")
x = int(input("Введите координату точки по оси x:"))
y = int(input("Введите координату точки по оси y:"))
if 0 < x and y > 0:
    print('1-я четверть')
elif x < 0 and y > 0:
    print('2-я четверть')
elif x < 0 and y < 0:
    print('3-я четверть')
else:
    print('4-я четверть')
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
print("Задача 4. Введите номер четверти:")
z = int(input("Введите номеру четверти от 1 до 4:"))
if z == 1:
    print('диапазон возможных координа: 0<x и y>0')
elif z == 2:
    print('диапазон возможных координа: 0>x и y>0')
elif z == 3:
    print('диапазон возможных координа: 0>x и y<0')
elif z == 4:
    print('диапазон возможных координа: 0<x и y<0')
else:
    print("Ошибка вывода,попробуйте еще.")

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# print("Задача 5. Введите координаты первой точки:")
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
x = int(input("Введите координату первой точки по оси x:"))
y = int(input("Введите координату первой точки по оси y:"))
print(" Введите координаты второй точки:")
x1 = int(input("Введите координату второй точки по оси x:"))
y1 = int(input("Введите координату второй точки по оси y:"))
print(((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5)
