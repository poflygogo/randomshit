from sys import stdin, stdout
from itertools import permutations

for line in stdin:
    data = sorted(permutations([str(i) for i in range(1, int(line.strip()) + 1)]), reverse=True)

    for i in data:
        result = ''.join(i)
        stdout.write(result + '\n')