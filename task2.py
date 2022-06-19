# Вычислить число Пи c заданной точностью d.
# Пример: при d = 0.001,  c= 3.141.
import math

print('Введите число для определения точности числа Пи: ', end = '')
d = input()

pi = str(math.pi)
length = len(d)
pi_short = ''

for i in range(0, length):
    pi_short += pi[i]

pi_short = float(pi_short)
print(f'Число Пи с точностью {d} = {pi_short}')