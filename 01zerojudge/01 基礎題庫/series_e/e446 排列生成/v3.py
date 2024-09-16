from sys import stdin, stdout
from itertools import permutations

data = [i for i in range(1, int(stdin.readline()) + 1)]

for line in permutations(data):
    result = ' '.join(map(str, line))
    stdout.write(result + '\n')