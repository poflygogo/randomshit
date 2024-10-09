from sys import stdin
from functools import reduce


for line in stdin:
    print(reduce(int.__and__, range(*map(int, line.rstrip().split()))))
