from sys import stdin

data = stdin.readlines()
heigh, width, r1, c1, r2, c2 = map(int, data.pop(0).split())

arrow = (r2-r1, c2-c1)
arrow = tuple(map(lambda x: 1 if x > 0 else 0 , arrow))

coordinate = [r1, c1]
while (coordinate[0] <= r2) and (coordinate[1] <= c2):
    print(data[coordinate[0]-1][coordinate[1]-1], end='')
    coordinate[0] += arrow[0]
    coordinate[1] += arrow[1]