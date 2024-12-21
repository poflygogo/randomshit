# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge h026. 202001_1 猜拳
# 2020-01 APCS


def main():
    f = int(input())
    n = int(input())
    trend = tuple(map(int, input().split()))
    bro, result, end = game_result(f, n, trend)
    print(*bro, ':', result, 'at round', end)


def game_result(f: int, n: int, trend: tuple) -> tuple:
    win = {0: 5, 5: 2, 2: 0}
    result = []
    draw_count = 0
    for i in range(n):
        result.append(f)
        if trend[i] == f:
            draw_count += 1
            if draw_count == 2:
                f = win[trend[i - 1]]
                draw_count = 0
        elif win[trend[i]] == f:
            return result, 'Won', i + 1
        else:
            return result, 'Lost', i + 1
    return result, 'Drew', n


main()
