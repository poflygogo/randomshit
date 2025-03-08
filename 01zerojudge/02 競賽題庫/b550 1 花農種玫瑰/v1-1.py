# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b550. 1.花農種玫瑰


def main():
    row, col = map(int, input().split())
    garden = [input() for _ in range(row)]
    result = []
    for r in range(row):
        for c in range(col):
            if (r, c) in ((0, 0), (row - 1, 0), (0, col - 1), (row - 1, col - 1)) or garden[r][c] == 'X':
                continue
            possible_place(row, col, r, c, garden, result)
    result.sort()
    print(str(len(result)) + '\n ',
          '\n '.join('  '.join(f'({i},{j})' for i, j in ans) for ans in result),
          sep='')


def possible_place(max_row: int, max_col: int, r: int, c: int, garden: int, result: list):
    directions = (((1, 0), (0, -1), (0, 1)),    # down
                  ((-1, 0), (0, -1), (0, 1)),   # up
                  ((0, 1), (-1, 0), (1, 0)),    # right
                  ((0, -1), (-1, 0), (1, 0)))   # left

    for d in directions:
        temp = [(c + j, r + i) for i, j in d]   # x, y 軸的數值要反過來
        if all(0 <= i < max_col and 0 <= j < max_row and garden[j][i] == 'O' for i, j in temp):
            temp.append((c, r))
            temp.sort()
            result.append(temp)


if __name__ == '__main__':
    main()
