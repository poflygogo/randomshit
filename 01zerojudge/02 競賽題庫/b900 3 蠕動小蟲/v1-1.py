# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b900. 3. 蠕動小蟲


def ghost_leg(c: int, r: int = 0) -> int:
    if r == max_row:
        return (c + 1) // 2 + 1
    if c > 0 and graph[r][c - 1] == '-':
        return ghost_leg(c - 2, r + 1)
    if c < max_col - 1 and graph[r][c + 1] == '-':
        return ghost_leg(c + 2, r + 1)
    return ghost_leg(c, r + 1)


w, h = map(int, input().split())
max_row, max_col = h, w * 2 - 1
graph = [input() for _ in range(max_row)]
result = [ghost_leg(i) for i in range(0, max_col, 2)]
print(*result)
