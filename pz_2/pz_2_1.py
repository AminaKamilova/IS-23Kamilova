
# Даны целые положительные числа А и В (А > В).
# На отрезке длины А размещено максимально возможное
# количество отрезков длины В (без наложений).
# Используя операцию взятия остатка от деления нацело,
# найти длину незанятой части отрезка А.

a = int(input('Введите значение А: '))
if a <= 0:
    print('Значение A должно быть больше нуля!')
    a = int(input('Введите значение А: '))
b = int(input('Введите значение B: '))
if b <= 0:
    print('Значение B должно быть больше нуля!')
    b = int(input('Введите значение B: '))
remainder = a % b
print('Длина незанятой части отрезка А:', remainder)
