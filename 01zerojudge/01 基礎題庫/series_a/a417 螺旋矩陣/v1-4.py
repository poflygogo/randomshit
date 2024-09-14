def spin(n: int, reverse: bool) -> list:
    """
    輸出 n x n 的螺旋矩陣
    :param n: 矩陣邊長
    :param reverse: 旋轉方向，預設為順時針
    :return: n x n 的螺旋矩陣
    """
    x1, x2, y1, y2 = 0, n - 1, 0, n - 1                 # 邊界
    x, y = 0, 0                                         # 指針
    direction = 1                                       # 定義方向
    max_num = n * n
    result = [[0 for _ in range(n)] for _ in range(n)]  # 生成一個內容物為 0 的 n x n 矩陣
    for i in range(1, max_num + 1):
        result[y][x] = i
        if i == max_num: break
        if direction == 1:
            x += 1
            if x == x2:
                direction = 2
                y1 += 1
        elif direction == 2:
            y += 1
            if y == y2:
                direction = 3
                x2 -= 1
        elif direction == 3:
            x -= 1
            if x == x1:
                direction = 4
                y2 -= 1
        else:
            y -= 1
            if y == y1:
                direction = 1
                x1 += 1
    if reverse:
        result = [[result[j][i] for j in range(n)] for i in range(n)]
    return result


for _ in range(int(input())):
    a, b = input().split()
    ans = spin(int(a), b == '2')
    for line in ans:
        for item in line:
            print(f'{item: 5d}', end='')
        print()
