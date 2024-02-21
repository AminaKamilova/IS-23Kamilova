# В последовательности на n целых чисел найти и вывести:

# 1. Максимальный среди отрицательных

# 2. Элементы кратные двум

# 3. Их сумму

import random
list_1 = []
n = int(input("Введите n: "))
for i in range(n):
    list_1.append(random.randint(-3, 2))
print("Последовательность: ", list_1)
print("Максимальный среди отрицательных: ", max(list(filter(lambda x: x < 0, list_1))))
print("Элементы кратные двум: ", list(filter(lambda x: x % 2 == 0 and x != 0, list_1)))
print("Их сумма: ", sum(list_1))