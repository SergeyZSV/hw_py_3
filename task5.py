# Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.

all_nums = []
odd_nums = []
with open('text_file_task5.txt', 'r') as read_file:
    for number in read_file:
        all_nums.append(int(number))

for i in range(0, len(all_nums)):
    if all_nums[i] % 2 != 0:
        odd_nums.append(all_nums[i])


with open('text_file_task5.txt', 'w') as result_file:
    for k in odd_nums:
        result_file.write(str(k) + '\n')