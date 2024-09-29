from sys import stdin


for _ in stdin:
    print(*sorted(map(int, next(stdin).rstrip().split())))
