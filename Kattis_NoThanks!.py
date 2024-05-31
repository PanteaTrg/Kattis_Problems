# -------------------------------
#        First Attempt
# -------------------------------

number_cnt = int(input())
sample_list = list(map(int, input().split()))
sample_list.sort()


sum_total = sample_list[0]
current_item = sample_list[0]
j = 1

for i in range(1, len(sample_list)):
    if sample_list[i] == current_item + j:
        j += 1
        continue
    else:
        sum_total += sample_list[i]
        current_item = sample_list[i]
        j = 1

print(sum_total)

# -------------------------------
#        Second Attempt
# -------------------------------

# Read the number of elements
number_cnt = int(input())

# Read the list of numbers and convert them to integers
sample_list = list(map(int, input().split()))

# Sort the list of numbers
sample_list.sort()

# Initialize the sum with the first element
sum_total = sample_list[0]
current_item = sample_list[0]

# Loop through the rest of the sorted list
for i in range(1, len(sample_list)):
    if sample_list[i] != current_item + 1:
        sum_total += sample_list[i]
        current_item = sample_list[i]

print(sum_total)
