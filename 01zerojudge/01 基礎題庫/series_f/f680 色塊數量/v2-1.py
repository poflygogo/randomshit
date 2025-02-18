# # -*- encoding: utf-8 -*-
# # python 3.12
# # ZeroJudge f680. 色塊數量


def operate(n: int, graph: list, cnt: int = 0):
    def bfs(row, col):
        queue = [(row, col)]
        while queue:
            r, c = queue.pop(0)
            for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (i, j) not in seen and 0 <= i < n and 0 <= j < n and graph[i][j] == graph[row][col]:
                    queue.append((i, j))
                    seen.add((i, j))


    seen = set()
    for r in range(n):
        for c in range(n):
            if (r, c) not in seen and graph[r][c] != 0:
                cnt += 1
                seen.add((r, c))
                bfs(r, c)
    return cnt


def main():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    print(operate(n, graph))


if __name__ == '__main__':
    main()
