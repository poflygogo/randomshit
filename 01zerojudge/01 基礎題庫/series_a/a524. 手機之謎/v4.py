from sys import stdin, stdout
from itertools import permutations

for line in stdin:
    line = line.strip()
    if not line:
        continue

    data = [str(i) for i in range(1, int(line) + 1)]
    data = sorted(permutations(data), reverse=True)

    for i in data:
        result =''.join(i)
        stdout.write(result + '\n')