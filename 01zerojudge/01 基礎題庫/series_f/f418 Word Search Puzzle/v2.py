from sys import stdin

data = stdin.readlines()
info = tuple(map(int, data.pop(0).split()))

arrow = (info[4]-info[2], info[5]-info[3])
arrow = tuple(map(lambda x: 1 if x > 0 else 0 , arrow))

coordinate = [info[2], info[3]]
while (coordinate[0] <= info[4]) and (coordinate[1] <= info[5]):
    print(data[coordinate[0]-1][coordinate[1]-1], end='')
    coordinate[0] += arrow[0]
    coordinate[1] += arrow[1]