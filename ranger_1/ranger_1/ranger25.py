# 3. Задайте список из n чисел последовательности (1 + 1 / n)**n
#  и выведите на экран их сумму.


N = int(input('Введите число - '))
list_s = [round((1 + 1 / i) ** i, 3) for i in range(1, N + 1)]

print(f'Последовательность : {list_s}\n Сумма : {sum(list_s)})')