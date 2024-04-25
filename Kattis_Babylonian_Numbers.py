# -------------------------------
#        First Attempt
# -------------------------------

number_of_testcases = int(input())
final_list = []

for i in range(number_of_testcases):
    list_of_testcases = input().split(',')
    new_list = [x if x != '' else '0' for x in list_of_testcases]
    integer_list = [int(item) for item in new_list]

    item_sum = 0
    for j in range(len(integer_list)):
        item_sum = item_sum + integer_list[j] * (60 ** (len(integer_list) - j - 1))
    final_list.append(item_sum)

    list_of_testcases.clear()
    new_list.clear()
    integer_list.clear()


for item in final_list:
    print(item)


# -------------------------------
#        Second Attempt
# -------------------------------
number_of_testcases = int(input())

results = []

for _ in range(number_of_testcases):
    test_input = input().split(',')
    integer_list = [int(item) if item != '' else 0 for item in test_input]

    item_sum = sum(integer_list[j] * (60 ** (len(integer_list) - j - 1)) for j in range(len(integer_list)))
    results.append(item_sum)

for result in results:
    print(result)

