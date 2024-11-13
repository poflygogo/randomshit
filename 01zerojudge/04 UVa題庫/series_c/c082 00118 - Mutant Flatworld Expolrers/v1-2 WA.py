from sys import stdin


max_x, max_y = map(int, stdin.readline().rstrip().split())
gap = set()
for line in stdin:
    line = line.rstrip().split()
    x, y, direction = int(line[0]), int(line[1]), {'N': 0, 'E': 1, 'S': 2, 'W': 3}[line[2]]

    for d in next(stdin).rstrip():
        if d == 'R':
            direction += 1
        elif d == 'L':
            direction -= 1
        else:
            if not (0 <= direction <= 3):
                direction = (0, 1, 2, 3)[direction % 4]

            if (x, y, direction) not in gap:
                x += (0, 1, 0, -1)[direction]
                y += (1, 0, -1, 0)[direction]

                if not ((0 <= x <= max_x) and (0 <= y <= max_y)):
                    x -= (0, 1, 0, -1)[direction]
                    y -= (1, 0, -1, 0)[direction]
                    print(x, y, 'NESW'[direction], 'LOST')
                    gap.add((x, y, direction))
                    break

    else:
        direction = (0, 1, 2, 3)[direction % 4]
        print(x, y, 'NESW'[direction])
