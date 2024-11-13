from sys import stdin

for line in stdin:
    B, P, M = map(int, line.split())
    print(pow(B, P, M))