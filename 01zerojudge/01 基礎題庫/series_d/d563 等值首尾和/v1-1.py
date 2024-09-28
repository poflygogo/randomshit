from itertools import accumulate


data = [int(i) for i in input().split()]
del data[0]
a = set(accumulate(data))
print(len(a.intersection(set(accumulate(data[::-1])))))
