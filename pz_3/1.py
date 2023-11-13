# Даны два целых числа: А, В. Проверить истинность
# высказывания: «Ровно одно из чисел А и В нечетное».
a = input('Введите значение A: ')
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        a = input('Введите значение A: ')
b = input('Введите значение B: ')
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        b = input('Введите значение B: ')

if (a % 2 == 0) and (b % 2 != 0):
    print(True)
elif (b % 2 == 0) and (a % 2 != 0):
    print(True)
else:
    print(False)