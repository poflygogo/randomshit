# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n052. 正立方體
# 林口高中練習題


# ---------------------------------------------------

import sys
import io
Q = """
10
1 5 6 7 8 9
2 5 6 7 8 10
2 5 6 7 8 9
3 5 6 7 8 9
4 5 6 7 8 9
3 5 6 7 8 10
2 6 7 8 9 10
3 6 7 8 9 10
4 6 7 8 9 10
3 4 6 7 9 10
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
    """ 判斷是否是正方體的展開圖

    忽視33型展開圖, 因為33型展開圖的最大寬度為5格, 放不進 4x4 的空間內

    (3, 3) 型展開圖為下面這種形式
    ■ ■ ■ □ □
    □ □ ■ ■ ■
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
    

def standardize(squares: list, size: int=4):
    """ 標準化，透過平移、翻轉(鏡像)、旋轉座標資訊，以利後續判斷
    """
    variant = []
    for _ in range(4):              # 旋轉 4 次
        # 旋轉
        for i in range(len(squares)):
            squares[i] = squares[i][1], -squares[i][0]

        for flip in (False, True):  # 是否翻轉(左右翻轉即可)
            # 翻轉
            if flip:
                for i in range(len(squares)):
                    squares[i] = -squares[i][0], squares[i][1]
            
            # 平移, 確保圖形貼近原點(0, 0)
            min_x = min(i[0] for i in squares)
            min_y = min(i[1] for i in squares)
            for i in range(len(squares)):
                squares[i] = squares[i][0] - min_x, squares[i][1] - min_y
            squares.sort()
            variant.append(tuple(squares))
    return min(variant)


def is_type_4_1_1(squares: list) -> bool:
    """ (4, 1, 1) 型展開圖
    □ ■ □ □     ■ □ □ □     ■ □ □ □     ■ □ □ □     ■ □ □ □     □ ■ □ □
    ■ ■ ■ ■     ■ ■ ■ ■     ■ ■ ■ ■     ■ ■ ■ ■     ■ ■ ■ ■     ■ ■ ■ ■
    □ ■ □ □     ■ □ □ □     □ ■ □ □     □ □ ■ □     □ □ □ ■     □ □ ■ □
    """
    condition = {((0, 0), (0, 1), (0, 2), (1, 1), (2, 1), (3, 1)),
                 ((0, 0), (0, 1), (1, 1), (1, 2), (2, 1), (3, 1)),
                 ((0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 1)),
                 ((0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2)),
                 ((0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2)),
                 ((0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1))}
    return squares in condition


def is_type_3_2_1(squares: list) -> bool:
    """ (3, 2, 1) 型展開圖
    ■ ■ □ □     ■ ■ □ □     ■ ■ □ □
    □ ■ ■ ■     □ ■ ■ ■     □ ■ ■ ■
    □ ■ □ □     □ □ ■ □     □ □ □ ■
    """
    condition = {((0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 1)),
                 ((0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 2)),
                 ((0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 3))}
    return squares in condition


def is_type_2_2_2(squares: list) -> bool:
    """ (2, 2, 2) 型展開圖
    ■ ■ □ □
    □ ■ ■ □
    □ □ ■ ■
    """
    condition = {((0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3))}
    return squares in condition


if __name__ == '__main__':
    main()
