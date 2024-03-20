# 2. В матрице найти среднее арифметическое положительных элементов.
matrix = [[i*j for j in range(-1, 2)] for i in range(1, 4)]
positive = [num for i in matrix for num in i if num > 0]
average = sum(positive) / len(positive) if positive else "???"
print("Матрица: ")
[print(i) for i in matrix]
print("Среднее арифметическое положительных элементов в матрице:", average)
