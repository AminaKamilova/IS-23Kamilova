# 1. В матрице элементы третьей строки заменить элементами
# из одномерного динамического массива соответствующей размерности.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Матрица №1: ")
[print(i) for i in matrix]
new_row = [10, 11, 12]
matrix[2] = [new_row[i] for i in range(len(new_row))]
print("Матрица №2: ")
[print(i) for i in matrix]