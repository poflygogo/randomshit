from sys import stdin
from itertools import groupby


for _ in stdin:
    result = []
    for key, val in groupby(stdin.readline().rstrip()):
        length = len(tuple(val))
        result.append(f'{"" if length == 1 else length}{key}')
    print(*result, sep='')
