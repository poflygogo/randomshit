# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a753. 一、最大面積


def find_max_area(max_row: int, max_col: int, graph: list):
    def dfs(r: int, c: int, target: str):
        if not (0 <= r < max_row) or not (0 <= c < max_col) or graph[r][c] != target:
            return
        nonlocal size
        size += 1
        graph[r][c] = None
        dfs(r - 1, c, target)
        dfs(r + 1, c, target)
        dfs(r, c - 1, target)
        dfs(r, c + 1, target)

    max_area = {}
    for row in range(max_row):
        for col in range(max_col):
            if graph[row][col]:
                key = graph[row][col]
                size = 0
                dfs(row, col, key)
                if size > 2:
                    max_area[key] = max(size, max_area.get(key, 0))
    return max_area


def main():
    max_row, max_col = map(int, input().split())
    graph = [input().split() for _ in range(max_row)]
    result = find_max_area(max_row, max_col, graph)
    print('\n'.join(str(result.get(input(), 0)) for _ in range(int(input()))))


if __name__ == '__main__':
    main()
