from sys import stdin
from re import findall


class BlueFlame:
    def __init__(self, init: list) -> None:
        self.x = int(init[0])
        self.y = int(init[1])
        self.prex = self.x
        self.prey = self.y
        self.direction = (
            0 if case[2] == 'N'
            else 45 if case[2] == 'NE'
            else 90 if case[2] == 'E'
            else 135 if case[2] == 'SE'
            else 180 if case[2] == 'S'
            else 225 if case[2] == 'SW'
            else 270 if case[2] == 'W'
            else 315
        )
    
    def turn(self, clockwise: str, degree: str):
        if clockwise == 'R':
            self.direction += int(degree)
        else:
            self.direction += 360 - int(degree)
        self.direction %= 360
    
    def move(self):
        self.prex = self.x
        self.prey = self.y
        if self.direction == 0:
            self.x -= 1
        elif self.direction == 45:
            self.x -= 1
            self.y += 1
        elif self.direction == 90:
            self.y += 1
        elif self.direction == 135:
            self.x += 1
            self.y += 1
        elif self.direction == 180:
            self.x += 1
        elif self.direction == 225:
            self.x += 1
            self.y -= 1
        elif self.direction == 270:
            self.y -= 1
        else:
            self.x -= 1
            self.y -= 1

    def move_back(self):
        self.x = self.prex
        self.y = self.prey
        

row, col = map(int, stdin.readline().strip().split())
mapdata = [stdin.readline().strip() for _ in range(row)]
_ = stdin.readline()
fail = []

flag = False
for case in stdin:
    if flag:
        print("I think I don't need to move anymore.")
        _ = stdin.readline()
        continue

    case = case.strip().split()
    bf = BlueFlame(case)
    actions = findall(r'\D|\d+', stdin.readline().strip())

    for i in range(len(actions)):
        if actions[i].isdigit():
            continue

        if actions[i] == 'M':
            bf.move()
        else:
            bf.turn(actions[i], actions[i + 1])

        if not ((0 < bf.x <= row) and (0 < bf.y <= col)):
            if (bf.x, bf.y, bf.direction) in fail:
                bf.move_back()

            else:
                fail.append((bf.x, bf.y, bf.direction))
                print(
                    bf.prey,
                    bf.prex,
                    ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')[bf.direction // 45],
                    'BAD PLAN!'
                )
                break
        
        elif mapdata[bf.x - 1][bf.y - 1] == 'T':
            print(bf.y, bf.x, 'FINISHED!')
            flag = True
            break
    
    else:
        print(
            bf.y,
            bf.x,
            ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')[bf.direction // 45]
        )
