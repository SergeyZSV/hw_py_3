# Составить список простых множителей натурального числа N.

print('Введите натуральное число: ', end = '')
n = int(input())
n_temp = n
all_factors = []
simple_factors = []

for i in range(2, n):
    if n % i == 0:
        all_factors.append(i)

i = 0
while i < len(all_factors):
    if n_temp % all_factors[i] == 0:
        simple_factors.append(all_factors[i])
        n_temp = n_temp // all_factors[i]
    else:
        i += 1

print(f'Список простых множителей числа {n}: {simple_factors}')