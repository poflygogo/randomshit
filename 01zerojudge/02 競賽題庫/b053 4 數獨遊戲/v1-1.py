# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b053. 4. 數獨遊戲
# 96學年度高雄市資訊學科能力競賽

# ---------------------------------

import sys
import io
Q = """
3
0 6 0 1 0 4 0 5 0
0 0 8 3 0 5 6 0 0
2 0 0 0 0 0 0 0 1
8 0 0 4 0 7 0 0 6
0 0 6 0 0 0 3 0 0
7 0 0 9 0 1 0 0 4
5 0 0 0 0 0 0 0 2
0 0 7 2 0 6 9 0 0
0 4 0 5 0 8 0 7 0
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------

def sudoku(n: int, graph: list):
    def solve(i: int = 0):
        if i >= len(empty):
            return True
        r, c = empty[i]
        for num in range(1, 10):
            if is_valid(num, r, c):
                graph[r][c] = num
                if solve(i + 1):
                    return True
            graph[r][c] = 0
        return False
    
    def is_valid(target: int, row: int, col: int):
        box_r = row // n * n
        box_c = col // n * n
        if (any(graph[row][c] == target for c in range(SIZE) if c != col) or
            any(graph[r][col] == target for r in range(SIZE) if r != col) or
            any(graph[r][c] == target for r in range(box_r, box_r + n) for c in range(box_c, box_c + n) if (row, col) != (r, c))):
            return False
        return True

    SIZE = n ** 2
    empty = [(i, j) for i in range(SIZE) for j in range(SIZE) if graph[i][j] == 0]
    if solve():
        return '\n'.join(' '.join(map(str, i)) for i in graph)
    else:
        return 'NO SOLUTION'


def main():
    while True:
        try:
            n = int(input())
        except EOFError:
            break
        graph = [list(map(int, input().split())) for _ in range(n ** 2)]
        print(sudoku(n, graph))


if __name__ == '__main__':
    main()
