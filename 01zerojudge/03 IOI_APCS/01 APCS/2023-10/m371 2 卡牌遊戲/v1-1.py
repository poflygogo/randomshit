# python 3.12
# ZeroJudge m371. 2. 卡牌遊戲
# APCS 2023-10

# 可讀性好差啊...

from typing import List, Optional


DIRECTIONS = (0, 1), (1, 0)


def main():
    max_row, max_col = map(int, input().split())
    graph: List[List[Optional[int]]] = [
        list(map(int, input().split())) for _ in range(max_row)
    ]

    sum_of_pair = 0
    while True:
        changed = False
        for r in range(max_row):
            for c in range(max_col):
                if graph[r][c] is None:
                    continue

                for dr, dc in DIRECTIONS:
                    r2 = r + dr
                    c2 = c + dc

                    while r2 < max_row and c2 < max_col and graph[r2][c2] is None:
                        r2 += dr
                        c2 += dc

                    if r2 < max_row and c2 < max_col and graph[r][c] == graph[r2][c2]:
                        changed = True
                        sum_of_pair += graph[r][c]
                        graph[r][c] = None
                        graph[r2][c2] = None
                        break
        if not changed:
            break

    print(sum_of_pair)


main()
