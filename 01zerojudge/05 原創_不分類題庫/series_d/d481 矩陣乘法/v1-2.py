# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d481. 矩陣乘法


def matrix_multiply(a: list, b: list, row: int, col: int) -> list:
    result = [[0] * row for _ in range(row)]
    for i in range(row):
        for j in range(row):
            result[i][j] = sum([a[i][k] * b[k][j] for k in range(col)])
    return result


def main():
    while True:
        try:
            size = tuple(map(int, input().split()))
            if size and all(i > 0 for i in size) and size[0] == size[3] and size[1] == size[2]:
                a = [list(map(int, input().split())) for _ in range(size[0])]
                b = [list(map(int, input().split())) for _ in range(size[2])]
            else:
                print('Error')
                continue
        except EOFError:
            break
        result = matrix_multiply(a, b, size[0], size[2])
        for row in result:
            print(' '.join(map(str, row)))


if __name__ == '__main__':
    main()
