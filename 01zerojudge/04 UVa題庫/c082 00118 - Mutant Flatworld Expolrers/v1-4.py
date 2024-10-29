from sys import stdin


max_x, max_y = map(int, stdin.readline().rstrip().split())  # 紀錄最遠的點
gap = set()                                                 # 紀錄踩過的坑
for line in stdin:
    line = line.rstrip().split()

    # 將方位資訊轉換成數字，方便計算，才不需要一直 if
    x, y, direction = int(line[0]), int(line[1]), {'N': 0, 'E': 1, 'S': 2, 'W': 3}[line[2]]

    for d in next(stdin).rstrip():
        if d == 'R':
            direction += 1
        elif d == 'L':
            direction -= 1
        else:
            if not (0 <= direction <= 3):
                direction = (0, 1, 2, 3)[direction % 4]

            x += (0, 1, 0, -1)[direction]
            y += (1, 0, -1, 0)[direction]

            if not ((0 <= x <= max_x) and (0 <= y <= max_y)):
                x -= (0, 1, 0, -1)[direction]
                y -= (1, 0, -1, 0)[direction]

                if (x, y) not in gap:
                    print(x, y, 'NESW'[direction], 'LOST')
                    gap.add((x, y))
                    break

    else:
        direction = (0, 1, 2, 3)[direction % 4]
        print(x, y, 'NESW'[direction])
