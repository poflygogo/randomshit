# python 3.12
# ZeroJudge r488. 1. 彗星撞擊
# APCS 2025-10

from typing import List, Dict, Tuple


def main():
    rows, cols, deep = map(int, input().split())
    graph: List[List[int]] = [[deep] * cols for _ in range(rows)]
    
    dinosaur: Dict[Tuple[int, int], int] = {}
    for _ in range(int(input())):
        a, b = map(int, input().split())
        dinosaur[(a, b)] = dinosaur.get((a, b), 0) + 1

    for _ in range(int(input())):
        r, c, s, d = map(int, input().split())
        flag = False  # 標記是否有恐龍被砸
        for i in range(max(0, r - s // 2), min(rows, r + s // 2 + 1)):
            for j in range(max(0, c - s // 2), min(cols, c + s // 2 + 1)):
                if dinosaur.get((i, j), 0) > 0:
                    dinosaur[(i, j)] = 0
                    flag = True

        if flag:
            continue
        for i in range(max(0, r - s // 2), min(rows, r + s // 2 + 1)):
            for j in range(max(0, c - s // 2), min(cols, c + s // 2 + 1)):
                graph[i][j] -= d

    print(
        max(max(i) for i in graph),  # 最高地面高度
        min(min(i) for i in graph),  # 最低地面高度
        sum(dinosaur.values()),      # 清醒恐龍數量
    )


main()
