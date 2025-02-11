# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d165. 八、草场普查
# NOI 冬令營


def gress(max_row, max_col, data):
    def dfs(r, c):
        nonlocal size
        if (not 0 <= r < max_row) or (not 0 <= c < max_col) or (data[r][c] == 0):
            return
        seen.add((r, c))
        size += data[r][c]
        data[r][c] = 0
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    cnt = 0
    max_size = 0
    seen = set()
    for row in range(max_row):
        for col in range(max_col):
            if (row, col) not in seen and data[row][col] != 0:
                size = 0
                dfs(row, col)
                max_size = max(max_size, size)
                cnt += 1
    return cnt, max_size


def main():
    while True:
        try:
            row, col = map(int, input().split())
            data = [list(map(int, input().split())) for _ in range(row)]
            print(*gress(row, col, data), sep='\n')
        except EOFError:
            break


if __name__ == '__main__':
    main()
