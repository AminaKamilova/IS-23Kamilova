# Составить функцию решения задачи: из заданного
# числа вычли сумму его цифр. Из результата вновь
# вычли сумму его цифр и т. д. Через сколько таких
# действий получится пуль?
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))


quantity = 0
n = input("Введите значение N: ")
while int != type(n):
    try:
        n = int(n)
    except ValueError:
        n = input("Введите значение N: ")
while n != 0:
    n = n - sum_of_digits(n)
    quantity = quantity + 1
print("Ноль получится через ", quantity, " действий/действия")