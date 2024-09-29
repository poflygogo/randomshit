from sys import stdin


for line in stdin:
    x1, y1, x2, y2, r = map(int, line.rstrip().split())
    if abs(x2 - x1) + abs(y2 - y1) > r:
        print('alive')
    else:
        print('die')
