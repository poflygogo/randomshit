# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e838 P5 炸彈超人(Bombs)
# 2019-08 TOI 新手同好會


def bombs(n: int, data: list) -> list:
    result = [['0'] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if data[row][col] == '*':
                for r in range(n):
                    result[r][col] = '*'
                for c in range(n):
                    result[row][c] = '*'
    return result


if __name__ == '__main__':
    n = int(input())
    data = [input() for _ in range(n)]
    for row in bombs(n, data):
        print(''.join(row))
