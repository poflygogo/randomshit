from sys import stdin, stdout
from itertools import permutations

for line in stdin:
    line = int(line.strip())
    data = [str(i) for i in range(1, line + 1)]
    data = sorted(permutations(data), reverse=True)

    for i in data:
        stdout.write(f"''.join(i)" + '\n')