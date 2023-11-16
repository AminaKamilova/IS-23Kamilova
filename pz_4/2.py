n = input('Введите значение N(N>0): ')
result = 0
while int != type(n):
    try:
        n = int(n)
    except ValueError:
        n = input('Введите значение N(N>0): ')