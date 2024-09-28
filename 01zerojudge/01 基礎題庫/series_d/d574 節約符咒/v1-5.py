from sys import stdin
from itertools import groupby


for length1 in stdin:
    length1 = length1.rstrip()
    if length1.isdigit():
        length1 = int(length1)
        data = stdin.readline().rstrip()
    else:
        length1, data = length1.split()
        length1 = int(length1)

    result = []
    for key, val in groupby(data):
        length2 = len(tuple(val))
        result.extend([str(length2), str(key)])
    
    if length1 <= len(result):
        print(data)
    else:
        print(*result, sep='')
