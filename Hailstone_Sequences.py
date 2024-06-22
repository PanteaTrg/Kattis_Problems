# -------------------------------
#        First Approach
# -------------------------------
number = int(input())
sequence_list = [number]

while number > 1:
    if number % 2 == 0:
        number = number // 2
        sequence_list.append(number)
    else:
        number = number * 3 + 1
        sequence_list.append(number)

print(len(sequence_list))


# -------------------------------
#        Second Approach
# -------------------------------
def collatz_length(number):
    length = 1
    while number > 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        length += 1
    return length


number = int(input())
print(collatz_length(number))
