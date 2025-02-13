# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e971. 2. 梗圖著色 (Coloring)
# 2019-04 TOI 練習賽 新手組


def coloring(max_row, max_col, graph: list) -> list:
    """ 只需要填滿橫的，直的不用填滿
    """
    queue = []
    for row in range(max_row):
        for col in range(max_col):
            if graph[row][col] != '1':
                continue
            if queue:
                graph[row][queue[0][1]: col + 1] = ['1'] * (col - queue[0][1] + 1)
                queue.clear()
            else:
                queue.append((row, col))
        queue.clear()
    return graph


def main():
    m, n = map(int, input().split())
    graph = [input().split() for _ in range(m)]
    print('\n'.join(' '.join(row) for row in coloring(m, n, graph)))


if __name__ == '__main__':
    main()
