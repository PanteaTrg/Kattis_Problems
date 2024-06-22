num_of_digits = int(input())
slot_list = [map(int, input().split()) for _ in range(3)]

count_of_seven = 0
for _ in range(len(slot_list)):
    if 7 in slot_list[_]:
        count_of_seven += 1

if count_of_seven == 3:
    print('777')
else:
    print(0)
