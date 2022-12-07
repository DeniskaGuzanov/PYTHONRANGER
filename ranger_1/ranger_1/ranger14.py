#4 Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint
max_v=100
k = int(input('Введите натуральную степень k:'))

rad=[randint(0,max_v) for i in range(k)]+[randint(1,max_v)]
m ='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(rad) if j][::-1])

m = m.replace('x^1+', 'x+')
m = m.replace('x^0', '')
m +=('','1')[m[-1]=='+']
m =(m, m[:-2])[m[-2:]=='^1']
print(m)