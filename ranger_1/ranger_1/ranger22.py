#  Напишите программу вычисления арифметического выражения 
# заданного строкой. Используйте операции +,-,/,*.
#  приоритет операций стандартный.
# Добавьте возможность использования скобок,
#  меняющих приоритет операций.
# *Пример:*           1+2*3 => 7;            (1+2)*3 => 9;

from operator import mul

number = '(3 + 3) x 3'
number_1 = '2 + 2 x 5'



result = number.replace('+', '+').replace('x', '*')
result_1 = number_1.replace('+', '+').replace('x', '*')
res = eval(result)
res_1 = eval(result_1)
print(f'{number} Арифметическое выпажение заданной строки ==> ' + str(res))
print(f'{number_1} Арифметическое выпажение заданной строки ==> ' + str(res_1))