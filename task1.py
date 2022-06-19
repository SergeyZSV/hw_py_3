# Найти наименьшее общее кратное двух чисел.

print('Введите первое число: ', end = '')
first_number = int(input())
print('Введите второе число: ', end = '')
second_number = int(input())

max = first_number * second_number

for i in range(1, max):
    if (i % first_number == 0) and (i % second_number == 0):
        nok = i
        break

print(f'Наименьшее общее кратное чисел {first_number} и {second_number} = {nok}')