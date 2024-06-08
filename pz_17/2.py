# Разработать программу с применением пакета tk,
# взяв в качестве условия одну любую задачу из ПЗ №2-9

# УСЛОВИЕ(3(1)):

# Даны два целых числа: А, В. Проверить истинность
# высказывания: «Ровно одно из чисел А и В нечетное».
import tkinter as tk

def check_numbers():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())

        if (a % 2 != 0 and b % 2 == 0) or (a % 2 == 0 and b % 2 != 0):
            result_label.config(text="Истина! Ровно одно из чисел А и В нечетное")
        else:
            result_label.config(text="Ложь... не выполняется условие")

    except ValueError:
        result_label.config(text="Некорректный ввод!" "\n" "Попробуйте ещё раз")

window = tk.Tk()
window.title("Проверка истинности высказывания")

label_a = tk.Label(window, text="Введите число A:")
label_a.grid(row=0, column=0)

entry_a = tk.Entry(window)
entry_a.grid(row=0, column=1)

label_b = tk.Label(window, text="Введите число B:")
label_b.grid(row=1, column=0)

entry_b = tk.Entry(window)
entry_b.grid(row=1, column=1)

button_check = tk.Button(window, text="Проверить истинность", command=check_numbers)
button_check.grid(row=2, column=0, columnspan=2)

result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2)

window.mainloop()
