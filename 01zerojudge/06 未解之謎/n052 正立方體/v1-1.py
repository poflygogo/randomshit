# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n052. 正立方體
# 林口高中練習題


# ---------------------------------------------------

import sys
import io
Q = """
1
13 14 10 11 12 8
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------

def main():
    for _ in range(int(input())):
        block_info = list(map(int, input().rstrip().split()))
        if is_possible_cube_net(block_info):
            print('yes')
        else:
            print('no')


def is_possible_cube_net(squares: list, size: int=4) -> bool:
    """ 判斷是否是正方體的展開圖(忽視33型展開圖)
    """
    # 把方格資訊轉換成座標的形式(row, col)
    for i in range(len(squares)):
        squares[i] = divmod(squares[i] - 1, size)
    squares.sort()

    if not is_connected(squares):
        return False
    squares = standardize(squares)
    return is_type_4_1_1(squares) or is_type_3_2_1(squares) or is_type_2_2_2(squares)


def is_connected(squares: list) -> bool:
    """ 判斷所有格子是否互相連通(bfs)
    """
    squares_set = set(squares)
    queue = [squares[0]]
    seen = set(queue)
    while queue:
        x, y = queue.pop(0)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            neighbor = (x + dx, y + dy)
            if neighbor in squares_set and neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return len(seen) == 6
    

# TOFIX: (4, 1, 1) 型, (3, 2, 1) 型上下翻轉的條件有問題
def standardize(squares: list, size: int=4):
    """ 標準化，透過平移、翻轉(鏡像)、旋轉座標資訊，以利後續判斷
    """
    # 平移，保證圖盡可能往原點(0, 0)靠近
    min_x = min(i[0] for i in squares)
    if min_x != 0:
        for i in range(len(squares)):
            squares[i] = squares[i][0] - min_x, squares[i][1]
    min_y = min(i[1] for i in squares)
    if min_y != 0:
        for i in range(len(squares)):
            squares[i] = squares[i][0], squares[i][1] - min_y

    # 90度旋轉, 保證圖是橫著擺的
    if max(i[0] for i in squares) == size - 1:
        for i in range(len(squares)):
            squares[i] = squares[i][1], -squares[i][0]
        min_x = min(i[0] for i in squares)
        min_y = min(i[1] for i in squares)
        for i in range(len(squares)):
            squares[i] = squares[i][0] - min_x, squares[i][1] - min_y

    # 左右翻轉, 保證圖是從左上開始
    if max(i[1] for i in squares if i[0] == 0) >= size // 2:
        for i in range(len(squares)):
            squares[i] = squares[i][0], -squares[i][1] + size - 1
    
    # 上下翻轉，確保圖的方向符合規格
    if sum(i[0] == 1 for i in squares) >= 3 and (2, 0) in squares:
        for i in range(len(squares)):
            if squares[i][0] == 0:
                squares[i] = 2, squares[i][1]
            elif squares[i][0] == 2:
                squares[i] = 0, squares[i][1]

    squares.sort()
    return tuple(squares)


def is_type_4_1_1(squares: list) -> bool:
    """ 
    □ ■ □ □     ■ □ □ □     ■ □ □ □     ■ □ □ □     ■ □ □ □     □ ■ □ □
    ■ ■ ■ ■     ■ ■ ■ ■     ■ ■ ■ ■     ■ ■ ■ ■     ■ ■ ■ ■     ■ ■ ■ ■
    □ ■ □ □     ■ □ □ □     □ ■ □ □     □ □ ■ □     □ □ □ ■     □ □ ■ □
    """
    condition = {((0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1)),
                 ((0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0)),
                 ((0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1)),
                 ((0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2)),
                 ((0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3)),
                 ((0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2))}
    return squares in condition


def is_type_3_2_1(squares: list) -> bool:
    """
    ■ ■ □ □     ■ ■ □ □     ■ ■ □ □
    □ ■ ■ ■     □ ■ ■ ■     □ ■ ■ ■
    □ ■ □ □     □ □ ■ □     □ □ □ ■
    """
    condition = {((0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 1)),
                 ((0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 2)),
                 ((0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 3))}
    return squares in condition


def is_type_2_2_2(squares: list) -> bool:
    """
    ■ ■ □ □
    □ ■ ■ □
    □ □ ■ ■
    """
    condition = {((0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3))}
    return squares in condition


if __name__ == '__main__':
    main()
