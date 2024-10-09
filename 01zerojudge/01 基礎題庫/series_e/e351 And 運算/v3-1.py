from sys import stdin


for line in stdin:
    if line.rstrip():
        a, b = map(int, line.rstrip().split())
        if a > b:
            a, b = b, a
        shift = 0
        while a != b:
            a >>= 1
            b >>= 1
            shift += 1
        print(a << shift)
