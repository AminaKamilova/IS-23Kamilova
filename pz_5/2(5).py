# Описать функцию Minmax(X, Y), записывающую в переменную
# Х минимальное из значений Хи У, а в переменную У максимальное
# из этих значений (Х и У вещественные параметры, являющиеся
# одновременно входными и выходными).
# Используя четыре вызова этой функции, найти минимальное и
# максимальное из данных чисел А, В, С, D.
def Minmax(x, y):
    if x > y:
        y, x = x, y
    return x, y


a = input('Введите значение A: ')
while int != type(a):
    try:
        a = int(a)
    except ValueError:
        a = input('Введите значение A: ')
b = input('Введите значение B: ')
while int != type(b):
    try:
        b = int(b)
    except ValueError:
        b = input('Введите значение B: ')
c = input('Введите значение C: ')
while int != type(c):
    try:
        c = int(c)
    except ValueError:
        c = input('Введите значение C: ')
d = input('Введите значение D: ')
while int != type(d):
    try:
        d = int(d)
    except ValueError:
        d = input('Введите значение D: ')
a, b = Minmax(a, b)
c, d = Minmax(c, d)
a, d = Minmax(a, d)
b, c = Minmax(b, c)
print('Максимальное число: ', d, ', минимальное число: ', a)