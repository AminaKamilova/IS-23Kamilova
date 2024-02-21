# Из заданной строки отобразить только цифры.
# Использовать библиотеку string. Строка -
# TheGreat Pyramidof KhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand 481 feet (147 metres) high.

from string import digits

string1 = 'TheGreat Pyramidof KhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand 481 feet (147 metres) high.'
string_new = [i for i in string1 if i in digits]
print("Результат:", string_new)