from sys import stdin, stdout
from itertools import permutations

data = [i for i in range(1, int(stdin.readline()) + 1)]
result = permutations(data)

result = '\n'.join(' '.join(map(str, line)) for line in result)

stdout.write(result)