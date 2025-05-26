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


# TOFIX: 需要修正判斷的方式
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
    transfer(squares)

    if not is_all_connected(squares):
        return False
    
    h = squares[-1][0] - squares[0][0]
    w = max(i[1] for i in squares) - min(i[1] for i in squares)
    if h + w != 5:
        return False
    
    if h == 4:
        rotate(squares)
        h, w = w, h
    
    k = sum(i[0] == 1 for i in squares)
    if k == 2:
        pass
    
    elif k == 3:
        if sum(i[0] == 0 for i in squares) == 1:
            flip(squares, mode=True)
    
    elif k == 4:
        return True
    
    else:
        return False


def is_all_connected(squares: list) -> bool:
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
    

def transfer(squares: list):
    """ 平移, 使圖形盡可能貼近原點(0, 0)
    """
    min_x = min(i[0] for i in squares)
    min_y = min(i[1] for i in squares)
    for i in range(len(squares)):
        squares[i] = squares[i][0] - min_x, squares[i][1] - min_y
    squares.sort()


def rotate(squares: list, mode: bool=False):
    """ 旋轉圖形，預設為逆時針旋轉，若 mode 為 True 則改為順時針
    """
    if mode:
        for i in range(len(squares)):
            squares[i] = -squares[i][1], squares[i][0]
    else:
        for i in range(len(squares)):
            squares[i] = squares[i][1], -squares[i][0]
    transfer(squares)


def flip(squares: list, mode: bool=False):
    """ 鏡像翻轉圖形，預設為左右翻轉，若 mode 為 True 則改為上下翻轉
    """
    if mode:
        for i in range(len(squares)):
            squares[i] = squares[i][0], -squares[i][1]
    else:
        for i in range(len(squares)):
            squares[i] = -squares[i][0], squares[i][1]
    transfer(squares)


if __name__ == '__main__':
    main()
