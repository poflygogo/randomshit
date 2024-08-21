from sys import stdin
from itertools import accumulate

stdin.readline()
print(*tuple(accumulate(map(int, stdin.readline().split()))))