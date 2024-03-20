# 1. В матрице элементы третьей строки заменить элементами
# из одномерного динамического массива соответствующей размерности.
matrix = [[i*j for j in range(2, 5)] for i in range(1, 4)]
print("Матрица №1: ")
[print(i) for i in matrix]
new_row = [i for i in range(3)]
matrix[2] = [new_row[i] for i in range(len(new_row))]
print("Матрица №2: ")
[print(i) for i in matrix]