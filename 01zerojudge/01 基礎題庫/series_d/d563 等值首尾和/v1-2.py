from itertools import accumulate


data = [int(i) for i in input().split()]
del data[0]
a = set(accumulate(data))
b = set(accumulate(data[::-1]))
print(len(a & b))
