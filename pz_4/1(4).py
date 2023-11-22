# Дано целое число N (N > 0).
# Найти сумму N² + (N + 1)² + (N + 2)² + ... + (2N)²
n = input('Введите значение N(N>0): ')
result = 0
while int != type(n):
    try:
        n = int(n)
    except ValueError:
        n = input('Введите значение N(N>0): ')
while n <= 0:
    n = input('Введите значение N(N>0): ')
    while int != type(n):
        try:
            n = int(n)
        except ValueError:
            n = input('Введите значение N(N>0): ')
for n in range(n, 2*n + 1):
    result = result + n**2
print('Сумма: ', result)