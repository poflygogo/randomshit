# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d481. 矩陣乘法


def matrix_multiply(a: list, b: list, a_rows: int, a_cols: int, b_rows: int, b_cols: int) -> list:
    result = [[0 for j in range(b_cols)] for i in range(a_rows)]
    for i in range(a_rows):
        for j in range(b_cols):
            result[i][j] = sum([a[i][k] * b[k][j] for k in range(a_cols)])
    return result


def main():
    while True:
        try:
            a_rows, a_cols, b_rows, b_cols = map(int, input().split())
            if a_cols != b_rows or any(x <= 0 for x in [a_rows, a_cols, b_rows, b_cols]):
                print('Error')
                continue
            a = [[int(x) for x in input().split()] for i in range(a_rows)]
            b = [[int(x) for x in input().split()] for i in range(b_rows)]
            result = matrix_multiply(a, b, a_rows, a_cols, b_rows, b_cols)
            for row in result:
                print(' '.join(map(str, row)))
        except EOFError:
            break


if __name__ == '__main__':
    main()
