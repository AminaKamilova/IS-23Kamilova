# 2. В матрице найти среднее арифметическое положительных элементов.
matrix = [[1, -2, 3], [4, 5, -6], [7, -8, -9]]
positive = [num for i in matrix for num in i if num > 0]
average = sum(positive) / len(positive) if positive else "???"
print("Матрица: ")
[print(i) for i in matrix]
print("Среднее арифметическое положительных элементов в матрице:", average)
