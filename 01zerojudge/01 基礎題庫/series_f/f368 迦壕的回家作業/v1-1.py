from sys import stdin
from re import findall


for line in stdin:
    print(f'1/{2 ** len(findall(r"RED|GREEN", line))}')
