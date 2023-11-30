# Дан список А размера N и целое число К(1<K<N).
# Вывести элементы списка, кратные К: AK, A2K, A3K... .
# Условный оператор не использовать
import random
list = []
n = input("Введите значение N: ")
while int != type(n):
    try:
        n = int(n)
    except ValueError:
        n = input("Введите значение N: ")
for i in range(n):
    list.append(random.randint(1, 5))