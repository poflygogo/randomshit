def gen_tornado_num(arr: list,
                    width: int,
                    direct: int) -> str:
    flag = [[True] * width for _ in range(width)]
    pos_x = width // 2
    pos_y = pos_x
    flag[pos_x][pos_y] = False
    while 0 <= pos_x < width and 0 <= pos_y < width:
        yield str(arr[pos_x][pos_y])
        flag[pos_x][pos_y] = False
        # 左
        if direct == 0:
            pos_y -= 1
            if flag[pos_x - 1][pos_y]:
                direct = 1
        # 上
        elif direct == 1:
            pos_x -= 1
            if flag[pos_x][pos_y + 1]:
                direct = 2
        # 右
        elif direct == 2:
            pos_y += 1
            if flag[pos_x + 1][pos_y]:
                direct = 3
        # 下
        else:
            pos_x += 1
            if flag[pos_x][pos_y - 1]:
                direct = 0


wid = int(input())
dir = int(input())
data = [[int(i) for i in input().split()] for _ in range(wid)]
print(''.join(gen_tornado_num(data, wid, dir)))
