from sys import stdin, stdout


for line in stdin:
    x1, y1, x2, y2, r = map(int, line.rstrip().split())
    if abs(x2 - x1) + abs(y2 - y1) > r:
        stdout.write('alive\n')
    else:
        stdout.write('die\n')
