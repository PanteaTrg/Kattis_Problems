array_size, subarray_size = input().split()
numbers_list = input().split()

i = 0
j = 0
even_cnt_total = 0
while i <= len(numbers_list) - int(subarray_size):
    even_count_list = 0
    for j in range(i, i + int(subarray_size)):
        if int(numbers_list[j]) % 2 == 0:
            even_count_list += 1
    if even_count_list >= 2:
        even_cnt_total += 1
    i += 1

print(even_cnt_total)
