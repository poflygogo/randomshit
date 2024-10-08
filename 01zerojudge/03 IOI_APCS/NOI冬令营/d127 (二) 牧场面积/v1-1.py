from sys import stdin
from math import ceil, floor


for line in stdin:
    line = int(line.rstrip()) / 4
    print(f'{ceil(line) * floor(line):.0f}')
