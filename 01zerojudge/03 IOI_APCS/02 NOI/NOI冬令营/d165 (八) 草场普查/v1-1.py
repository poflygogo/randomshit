# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d165. 八、草场普查
# NOI 冬令營


def gress(max_row, max_col, data):
    def bfs():
        queue = [(row, col)]
        result = data[row][col]
        seen.add((row, col))
        while queue:
            r, c = queue.pop(0)
            for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (i, j) not in seen and 0 <= i < max_row and 0 <= j < max_col and data[i][j] != 0:
                    result += data[i][j]
                    seen.add((i, j))
                    queue.append((i, j))
        return result

    cnt = 0
    max_size = 0
    seen = set()
    for row in range(max_row):
        for col in range(max_col):
            if (row, col) not in seen and data[row][col] != 0:
                max_size = max(max_size, bfs())
                cnt += 1
    return cnt, max_size


def main():
    while True:
        try:
            row, col = map(int, input().split())
            data = [tuple(map(int, input().split())) for _ in range(row)]
            print(*gress(row, col, data), sep='\n')
        except EOFError:
            break


if __name__ == '__main__':
    main()
