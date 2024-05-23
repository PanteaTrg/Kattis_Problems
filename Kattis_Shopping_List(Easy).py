# Solution 1
number_of_list, number_of_items = map(int, input().split())

list_items = []
for i in range(number_of_list):
    list_items.append(input().split())

items = list_items[0]
for i in range(1, len(list_items)):
    items = set(items) & set(list_items[i])

list(items).sort()
print(len(items))
for item in items:
    print(item)


# Solution 2
n, m = map(int, input().split())
items = input()
itemsList = items.split(' ')
countList = [1] * m

for i in range(n - 1):
    newItems = input()
    newItemList = newItems.split(' ')
    for j in range(m):
        if itemsList[j] in newItemList:
            countList[j] += 1

printedList = []
for i in range(len(countList)):
    if countList[i] == n:
        printedList.append(itemsList[i])

print(len(printedList))
printedList.sort()
for i in printedList:
    print(i)

# Solution 3
# Read input values
number_of_list, number_of_items = map(int, input().split())

# Read all the list items and store them as sets
list_items = [set(input().split()) for _ in range(number_of_list)]

# Find the common items by taking the intersection of all sets
common_items = set.intersection(*list_items)

# Convert the result to a sorted list
common_items = sorted(common_items)

# Output the result
print(len(common_items))
for item in common_items:
    print(item)