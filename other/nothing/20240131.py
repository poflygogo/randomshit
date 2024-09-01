list1 = [1, 2, 3]
list2 = [10, 100, 1000]

list3 = [i*j for i, j in zip(list1, list2)]

print(list1)
print(list2)
print(list3)