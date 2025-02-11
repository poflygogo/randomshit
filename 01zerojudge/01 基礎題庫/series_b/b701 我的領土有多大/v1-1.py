# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b701. 我的領土有多大


def get_island_info(row: int, col: int) -> tuple:
    """ 返回島嶼的大小，與極西、極北、極東、極南四個位置的座標
    """
    # bfs
    queue = [(row, col)]
    seen.add((row, col))
    w = e = col     # 極西、極東
    n = s = row     # 極北、極南
    size = 1        # 島嶼大小

    while queue:
        r, c = queue.pop()
        for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if (i, j) in seen:
                continue
            if 0 <= i < rows and 0 <= j < cols and graph[i][j] == '1':
                queue.append((i, j))
                seen.add((i, j))
                w = min(w, j)
                e = max(e, j)
                n = min(n, i)
                s = max(s, i)
                size += 1

    return w, n, e, s, size


rows, cols = map(int, input().split())
graph = [input().split() for _ in range(rows)]
result = []
seen = set()
for row in range(rows):
    for col in range(cols):
        if graph[row][col] == '1' and (row, col) not in seen:
            result.append(get_island_info(row, col))    # 其實好像不用存，直接 print 就可以了

print('\n'.join(' '.join(map(str, r)) for r in result))
