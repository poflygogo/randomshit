def gen_tornado_num(width: int,
                    direct: int,
                    arr: list) -> str:
    flag = [[True] * width for _ in range(width)]
    pos_x = width // 2
    pos_y = pos_x
    while 0 <= pos_x < width and 0 <= pos_y < width:
        yield str(arr[pos_x][pos_y])
        flag[pos_x][pos_y] = False
        # 左
        if direct == 0:
            pos_y -= 1
            if pos_y >= 0 and flag[pos_x - 1][pos_y]:
                direct = 1
        # 上
        elif direct == 1:
            pos_x -= 1
            if pos_x >= 0 and flag[pos_x][pos_y + 1]:
                direct = 2
        # 右
        elif direct == 2:
            pos_y += 1
            if pos_y < width and flag[pos_x + 1][pos_y]:
                direct = 3
        # 下
        else:
            pos_x += 1
            if pos_x < width and flag[pos_x][pos_y - 1]:
                direct = 0


stdin = open('test3.txt')
wid = int(stdin.readline())
print(''.join(gen_tornado_num(
    wid,
    int(stdin.readline()),
    [[int(i) for i in stdin.readline().split()] for _ in range(wid)]))
)
