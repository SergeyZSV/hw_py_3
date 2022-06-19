# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

new_list = [1, 2, 3, 5, 1, 5, 3, 10]
print(f'Исходный список: {new_list}')
new_set = set()

for i in new_list:
    new_set.add(i)

result_list = []

for i in new_set:
    result_list.append(i)

print(f'Список неповторяющихся элементов исходного: {result_list}')