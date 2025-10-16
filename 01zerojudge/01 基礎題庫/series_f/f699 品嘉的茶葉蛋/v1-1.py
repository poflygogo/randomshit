from typing import NamedTuple


class StepInfo(NamedTuple):
    r: int
    c: int
    step: int


def next_step(curr: StepInfo):
    yield curr.r + 1, curr.c
    yield curr.r - 1, curr.c
    yield curr.r, curr.c + 1
    yield curr.r, curr.c - 1


row_limit, col_limit = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row_limit)]

flag = True
seen = {(0, 0)}
queue = [StepInfo(0, 0, 0)]
while queue:
    curr = queue.pop(0)
    if graph[curr.r][curr.c] == 1:
        print(curr.step)
        flag = False
    for nr, nc in next_step(curr):
        if 0 <= nr < row_limit and 0 <= nc < col_limit and (nr, nc) not in seen and graph[nr][nc] != 2:
            seen.add((nr, nc))
            queue.append(StepInfo(nr, nc, curr.step + 1))

if flag:
    print("嘉油！")
