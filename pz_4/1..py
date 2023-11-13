# Дано целое число N (0).
# Найти сумму ² (N + 1)² + (N2) + ... + (2N)²
n = input('Введите значение N(N>0): ')
result = 0
while int != type(n):
    try:
        n = int(n)
    except ValueError:
        n = input('Введите значение N(N>0): ')
for i in range(n, 2*n + 1):
    result = result + i**2
print(result)