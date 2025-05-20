# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m602. 112北二2a.教練 (Coach)
# 112北二區桃竹苗資訊學科能力複賽


def coach():
    slope = [safe_slope(data[i][1] - data[0][1], data[i][0] - data[0][0]) for i in range(1, n)]
    if all(slope[i] != slope[i - 1] for i in range(1, n - 1)):
        return data[0]
    
    counter = {}
    for i in slope:
        counter[i] = counter.get(i, 0) + 1
        if len(counter) == 2 and sum(counter.values()) > 2:
            r = [j for j in counter if counter[j] == 1][0]
            return data[slope.index(r) + 1]
    return -1, -1


def safe_slope(dy, dx):
    if dx == 0:
        return float('inf')
    else:
        return dy / dx


if __name__ == '__main__':
    n = int(input())
    data = [tuple(map(int, input().split())) for _ in range(n)]
    data.sort()
    print(*coach())
