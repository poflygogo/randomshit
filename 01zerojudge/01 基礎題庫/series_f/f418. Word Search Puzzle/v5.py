from sys import stdin

data = stdin.readlines()
heigh, width, r1, c1, r2, c2 = map(int, data.pop(0).split())

if r1 == r2:
    print(data[r1-1][c1-1:c2])

elif c1 == c2:
    x = r1-1
    y = c1 -1
    while x < r2:
        print(data[x][y], end='')
        x += 1
        
else:
    x, y = r1-1, c1-1
    while x < r2:
        print(data[x][y], end='')
        x += 1
        y += 1