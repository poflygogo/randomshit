# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge i793. pC. WAKUWAKU 尋找興奮源 (⌓‿⌓)


max_row, max_col, r, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(max_row)]


def find_wakuwaku(r, c):
    def next_node(x, y):
        yield x + 1, y
        yield x - 1, y
        yield x, y + 1
        yield x, y - 1

    def is_available(r, c):
        return (
            0 <= r < max_row
            and 0 <= c < max_col
            and (r, c) not in seen
            and graph[r][c] != 1
        )

    def is_wakuwaku(r, c):
        return graph[r][c] == 2

    if is_wakuwaku(r, c):
        return 0

    queue = [(r, c, 0)]
    seen = {(r, c)}
    while queue:
        row, col, step = queue.pop(0)
        step += 1
        for r, c in next_node(row, col):
            if is_available(r, c):
                if is_wakuwaku(r, c):
                    return step
                queue.append((r, c, step))
                seen.add((r, c))
    return "WAKUWAKU"


print(find_wakuwaku(r, c))
