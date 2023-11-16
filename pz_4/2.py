# Дано целое число N (> 1).
# Найти наибольшее целое число К, при котором выполняется
# неравенство 3^k < N.
n = input('Введите значение N(N>1): ')
while int != type(n):
    try:
        n = int(n)
    except ValueError:
        n = input('Введите значение N(N>1): ')
while n <= 1:
    n = input('Введите значение N(N>1): ')
    while int != type(n):
        try:
            n = int(n)
        except ValueError:
            n = input('Введите значение N(N>1): ')
k = 0
degree = 3**k
while degree < n:
    k = k + 1
    degree = 3**k
k = k - 1
print("Наибольшее целое число К = ", k)