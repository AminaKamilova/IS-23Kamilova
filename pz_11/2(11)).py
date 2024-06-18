# Из предложенного текстового файла (text18-10.txt) вывести на экран его содержимое,
# количество букв в верхнем регистре. Сформировать новый файл, в который поместить
# текст в стихотворной форме предварительно поставив после последней строки автора
# и название произведения

uppercase_count = 0
with open("text18-10.txt", "r", encoding="utf-16") as file:
    text = file.read()
    for char in text:
        if char.isupper():
            uppercase_count += 1
print("Содержимое файла:")
print(text)
print("Количество букв в верхнем регистре:", uppercase_count)

with open("text18-10.txt", "r", encoding="utf-16") as file:
    poem_lines = file.readlines()
formatted_poem = '\n'.join(poem_lines)
author = "М.Ю.Лермонтов"
title = "Бородино"
formatted_poem += "\n\nАвтор: "
formatted_poem += author
formatted_poem += "\nНазвание стихотворения: "
formatted_poem += title
with open("formatted_poem.txt", "w", encoding="utf-16") as file:
    file.write(formatted_poem)
print("Готово! Можете заглянуть в файл")