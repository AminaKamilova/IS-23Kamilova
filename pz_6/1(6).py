# Дан список А размера N и целое число К(1<K<N).
# Вывести элементы списка, кратные К: AK, A2K, A3K... .
# Условный оператор не использовать
import random
a = []
n = input("Введите значение N: ")
while int != type(n):
    try:
        n = int(n)
    except ValueError:
        n = input("Введите значение N: ")
for i in range(n):
    a.append(random.randint(1, 5))
k = input('Введите значение K(1<K<N): ')
while True:
    try:
        k = int(k)
        if 1 < k < n:
            break
        else:
            k = int(input('Введите значение K (1<K<N): '))
    except ValueError:
        k = input('Введите значение K (1<K<N): ')


# Вывод элементов списка, кратных K
elements = a[k-1::k]
print("Список: ", a)
print('элементы списка, кратные К: ', elements)
