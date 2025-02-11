# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e287. 機器人的路徑
# 2019-06 APCS


def test():
    path = f'./test_case/e287_'
    for i in range(3):
        with open(path + f'{i:02d}' + '.in') as f:
            row, col = map(int, f.readline().rstrip().split())
            data = [list(map(int, f.readline().rstrip().split())) for _ in range(row)]
            result = robot(row, col, data)
        with open(path + f'{i:02d}' + '.out') as f:
            ans = int(f.readline().rstrip())
            if ans == result:
                print(f'{i:02d} AC', end='\n\n')
            else:
                print(f'{i:02d} WA',
                      f'bad  ans: {result}',
                      f'good ans: {ans}',
                      sep='\n',
                      end='\n\n')


def robot(max_row, max_col, data):
    # find start coordinate
    x = y = 0
    for i in range(max_row):
        for j in range(max_col):
            x, y = min((x, y), (i, j), key=lambda item: data[item[0]][item[1]])

    result = data[x][y]
    data[x][y] = None
    possible = [(i, j)
                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
                if 0 <= i < max_row and 0 <= j < max_col and data[i][j] is not None]
    while possible:
        x, y = min(possible, key=lambda item: data[item[0]][item[1]])
        result += data[x][y]
        data[x][y] = None
        possible = [(i, j)
                    for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
                    if 0 <= i < max_row and 0 <= j < max_col and data[i][j] is not None]
    return result


def main():
    row, col = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(row)]
    print(robot(row, col, data))


if __name__ == '__main__':
    test()
