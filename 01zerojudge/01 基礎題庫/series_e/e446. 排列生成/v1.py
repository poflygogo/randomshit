from sys import stdin
from itertools import permutations

data = [i for i in range(1, int(stdin.readline()) + 1)]
for i in permutations(data):
    print(*i)