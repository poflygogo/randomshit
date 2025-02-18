# # -*- encoding: utf-8 -*-
# # python 3.12
# # ZeroJudge f680. 色塊數量


def operate(n: int, graph: list, cnt: int = 0):
    def dfs(r, c, target):
        if 0 <= r < n and 0 <= c < n and graph[r][c] == target:
            graph[r][c] = 0
            dfs(r - 1, c, target)
            dfs(r + 1, c, target)
            dfs(r, c + 1, target)
            dfs(r, c - 1, target)

    for r in range(n):
        for c in range(n):
            if graph[r][c] != 0:
                cnt += 1
                dfs(r, c, graph[r][c])
    return cnt


def main():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    print(operate(n, graph))


if __name__ == '__main__':
    main()
