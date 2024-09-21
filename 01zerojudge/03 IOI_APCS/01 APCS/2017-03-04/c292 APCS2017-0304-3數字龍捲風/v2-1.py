def gen_tornado_num(width: int,
                    direct: int,
                    arr: list) -> str:
    offset = ((0, -1), (-1, 0), (0, 1), (1, 0))
    pos_x = width // 2
    pos_y = pos_x
    vector = ((0, -1), (-1, 0))
    yield str(arr[pos_x][pos_y])
    for i in range(1, width):
        for _ in range(2):
            for _ in range(i):
                pos_x += offset[direct][0]
                pos_y += offset[direct][1]
                yield str(arr[pos_x][pos_y])
            direct = (direct + 1) % 4
    for _ in range(i):
        pos_x += offset[direct][0]
        pos_y += offset[direct][1]
        yield str(arr[pos_x][pos_y])


wid = int(input())
print(''.join(gen_tornado_num(
    wid,
    int(input()),
    [[int(i) for i in input().split()] for _ in range(wid)]))
)
