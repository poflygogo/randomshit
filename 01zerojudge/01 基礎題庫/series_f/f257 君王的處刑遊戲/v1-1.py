# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f257. 君王的處刑遊戲


while True:
    try:
        size = int(input())
    
    except EOFError:
        exit()
    
    else:
        matrix = [[0] * size for _ in range(size)]

        for _ in range(int(input())):
            col, row = map(int, input().split())
            matrix[row][col] = 'x'

        for row in range(size):
            for col in range(size):
                if matrix[row][col] == 0:
                    matrix[row][col] = bool(row != 0 and col != 0 and matrix[row - 1][col - 1] == 'x') + \
                                    bool(row != 0 and col != size - 1 and matrix[row - 1][col + 1] == 'x') + \
                                    bool(row != 0 and matrix[row - 1][col] == 'x') + \
                                    bool(col != 0 and matrix[row][col - 1] == 'x') + \
                                    bool(col != size - 1 and matrix[row][col + 1] == 'x') + \
                                    bool(row != size - 1 and col != 0 and matrix[row + 1][col - 1] == 'x') + \
                                    bool(row != size - 1 and col != size  - 1 and matrix[row + 1][col + 1]) + \
                                    bool(row != size - 1 and matrix[row + 1][col])

        for line in matrix:
            print(*line, sep='')
