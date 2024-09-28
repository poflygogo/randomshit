from itertools import accumulate


data = [int(i) for i in input().split()]
del data[0]
a = tuple(accumulate(data))
count = 0
for i in accumulate(data[::-1]):
    if i in a:
        count += 1
print(count)
