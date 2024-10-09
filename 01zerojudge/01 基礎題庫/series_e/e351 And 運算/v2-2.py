from sys import stdin


for line in stdin:
    if line.rstrip() == '':
        break
    a, b = map(int, line.rstrip().split())
    if b < a:
        a, b = b, a
    while a < b:
        b &= b - 1
    print(a & b)
