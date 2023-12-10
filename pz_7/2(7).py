# Дана строка, содержащая полное имя файла.
# Выделить из этой строки название последнего каталога
# (без символов «/»).
# Если файл содержится в корневом каталоге, то вывести символ «\»
file_path = input('Введите полное имя файла: ')
index = file_path.rfind('\\')
if index == -1:
    directory_name = '\\'
else:
    index_prev = file_path.rfind('\\', 0, index)
    if index_prev == -1:
        directory_name = '\\'
    else:
        directory_name = file_path[index_prev+1:index]
print("Вывод: ", directory_name)
