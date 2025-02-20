# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11094 Continents
# ZeroJudge e584


from collections import deque
from sys import stdin


def continent(max_row: int, max_col: int, graph: list, x: int, y: int) -> int:
    def bfs(r, c):
        queue.append((r, c))
        temp = set(queue)
        while queue:
            r, c = queue.popleft()
            for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if j < 0 or j == max_col:
                    j %= max_col
                if 0 <= i < max_row and (i, j) not in temp and graph[i][j] == ground:
                    temp.add((i, j))
                    queue.append((i, j))
        seen.update(temp)
        return len(temp)

    ground = graph[x][y]
    queue = deque()
    seen = set()
    result = [0]
    bfs(x, y)
    for row in range(max_row):
        for col in range(max_col):
            if (row, col) not in seen and graph[row][col] == ground:
                result.append(bfs(row, col))
    return max(result)


def main():
    for line in stdin:
        line = line.rstrip()
        if not line:
            continue
        r, c = map(int, line.split())
        graph = [stdin.readline() for _ in range(r)]
        x, y = map(int, stdin.readline().rstrip().split())
        print(continent(r, c, graph, x, y))


if __name__ == '__main__':
    main()
