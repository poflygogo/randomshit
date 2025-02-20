# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00532 Dungeon Master
# ZeroJudge c124


from collections import deque


def dungeon_master(layer, row, col, graph):
    sz, sx, sy = find_s(layer, row, col, graph)
    queue = deque([(sz, sx, sy, 0)])
    seen = {(sz, sx, sy)}
    while queue:
        z, x, y, steps = queue.popleft()
        steps += 1
        for k, i, j in ((z + 1, x, y), (z - 1, x, y), (z, x + 1, y), (z, x - 1, y), (z, x, y + 1), (z, x, y - 1)):
            if (0 <= k < layer and 0 <= i < row and 0 <= j < col and (k, i, j) not in seen and graph[k][i][j] != '#'):
                if graph[k][i][j] == 'E':
                    return steps
                seen.add((k, i, j))
                queue.append((k, i, j, steps))
    return False


def find_s(layer, row, col, graph):
    for i in range(layer):
        for j in range(row):
            for k in range(col):
                if graph[i][j][k] == 'S':
                    return i, j, k


def main():
    while True:
        layer, row, col = map(int, input().split())
        if layer == row == col == 0:
            break
        graph = [[''] * row for _ in range(layer)]
        for i in range(layer):
            for j in range(row):
                graph[i][j] = input()
            input()
        result = dungeon_master(layer, row, col, graph)
        print(
            f'Escaped in {result} minute(s).' if result else
            'Trapped!'
        )


if __name__ == '__main__':
    main()
