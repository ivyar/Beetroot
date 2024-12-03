import random

#Task 1
numbers = []
while len(numbers) != 10:
    numbers.append(random.randint(0, 20))
print(max(numbers))

#Task 2
list1 = []
list2 = []
while len(list1) != 10:
    list1.append(random.randint(1, 10))
    list2.append(random.randint(1, 10))
set1 = set(list1)
set2 = set(list2)
list3 = list(set1 & set2)
print(list3)

#Task3
list100 = list(range(1, 101))
other_list = []
i = 0
while i != len(list100):
    if (list100[i] % 7 == 0) and (list100[i] % 5 != 0):
        other_list.append(list100[i])
    i += 1
print(other_list)