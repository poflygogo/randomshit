from sys import stdin


for line in stdin:
    a, b = map(int, line.rstrip().split())
    while a < b:
        b &= b - 1
    print(a & b)
