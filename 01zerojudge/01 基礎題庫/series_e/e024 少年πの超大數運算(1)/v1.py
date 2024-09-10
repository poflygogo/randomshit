from sys import stdin

for line in stdin:
    a, b = map(int, line.split())
    if a == b == 0: break
    print(pow(a, b))