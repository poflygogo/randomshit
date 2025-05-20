# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m606. 112北二1b.開場列隊 (Line up)
# 112北二區桃竹苗資訊學科能力複賽


# ---------------------------------------------------

import sys
import io
Q = """5
0 0
0 1
0 2
1 0
1 1"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


from collections import Counter


def line_up(arr: list, t: int=0, team: str='BA'):
    slope = [safe_slope(arr[i][0] - arr[t][0], arr[i][1] - arr[t][1]) if i != t else None 
             for i in range(len(arr))]
    slope_counter = Counter(slope)
    if slope_counter.most_common(1)[0][1] > 1:
        target = slope_counter.most_common(1)[0][0]
        return [team[i in (None, target)] for i in slope]
    if t == 0:
        result = line_up(arr, 1, 'AB')
        if result:
            return result
        else:
            result = ['B'] * len(arr)
            result[0] = result[1] = 'A'
            return result
    else:
        return False


def safe_slope(dx: int, dy: int) -> float:
    if dx == 0:
        return float('inf')
    else:
        return dy / dx


def main():
    arr = [tuple(map(int, input().split())) for _ in range(int(input()))]
    result = line_up(arr)
    print(*result, sep='\n')


if __name__ == '__main__':
    main()
