# Дан словарь с произвольным количеством элементов.
# Выяснить имеется ли в нем элемент с ключом «фрукт  = яблоко» и
# если он отсутствует, то добавить его в словарь.
# Вывести на экран первоначальный словарь и измененный
dictionary = dict(ноутбук="honor", марк="инженер", солнце="Монако")
print("первоначальный словарь", dictionary)
dictionary.setdefault("фрукт", "яблоко")
print("измененный словарь", dictionary)