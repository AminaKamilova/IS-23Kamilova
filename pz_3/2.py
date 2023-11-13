# Дан номер месяца - целое число в диапазоне 1-12
# (1 - январь, 2 - февраль и т. д.).
# Определить количество дней в этом месяце для невисокосного года.
month = input('Введите номер месяца: ')
while type(month) != int:
    try:
        month = int(month)
    except ValueError:
        month = input('Введите номер месяца: ')
while month <= 0 or month > 12:
    print('Номер месяца должен быть от 1 до 12')
    month = int(input('Введите номер месяца: '))
if month == 2:
    days = 28
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
else:
    days = 31
print("В этом месяце", days, "день/дней")