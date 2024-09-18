from sys import stdin, stdout
from itertools import permutations

for line in stdin:
    line = line.strip()
    if not line:
        continue

    for i in sorted(
            permutations([str(i) for i in range(1, int(line) + 1)]),
            reverse=True):
        result = ''.join(i)
        stdout.write(result + '\n')