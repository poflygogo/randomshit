from sys import stdin
from itertools import permutations

for line in stdin:
    if line == '0\n': break
    
    items = [chr(i) for i in range(97, 97 + int(line))]
    result = permutations(items)

    for i in result:
        print(*i, sep='')