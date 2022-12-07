# Задача №5 
# Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint.

import random 
x = [1, 2, 3, 4, 4, 5 ,6, 7]
print(x)

for i in range(len(x) -1, 0, -1):
    y = random.randint(0, i + 1)
    x[i], x[y] = x[y], x[i]

print(str(x))


