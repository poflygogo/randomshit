# -*- encoding: utf-8 -*-
# python 3.12
# 2021-10 TOI 新手同好會

# 沒有 zerojudge 編號，因為沒人上傳到 zerojudge


import time


def checkers(n: int, matrix: list[list[str]], x: int, y: int, direction: str) -> list[list[str]] | str:
    delta_x, delta_y = ((1, 0), (1, 1), (0, 1))[int(direction)]
    x -= 1
    y -= 1
    if x + delta_x < n and y + delta_y < n and matrix[x + delta_x][y + delta_y] == '0':
        matrix[x][y], matrix[x + delta_x][y + delta_y] = matrix[x + delta_x][y + delta_y], matrix[x][y]
        return matrix
    else:
        end_x, end_y = x, y
        while (end_x + delta_x * 2 < n and
               end_y + delta_y * 2 < n and
               matrix[end_x + delta_x][end_y + delta_y] != '0' and
               matrix[end_x + delta_x * 2][end_y + delta_y * 2] == '0'):
            end_x += 2 * delta_x
            end_y += 2 * delta_y
        if (x, y) != (end_x, end_y):
            matrix[x][y], matrix[end_x][end_y] = matrix[end_x][end_y], matrix[x][y]
            return matrix
        return 'Impossible'


def main():
    n = int(input())
    matrix = [input().split() for _ in range(n)]
    row, col = map(int, input().split())
    direction = input()
    result = checkers(n, matrix, row, col, direction)
    if type(result) is str:
        print(result)
    else:
        print('\n'.join(' '.join(map(str, r)) for r in result))


def custom_judge(file_id: int = 1):
    file_path_test = f'./testcase/testcase{file_id}_test.txt'
    file_path_ans = f'./testcase/testcase{file_id}_ans.txt'
    with open(file_path_test, encoding='utf-8') as f:
        scan = f.readline
        n = int(scan().strip())
        matrix = [scan().strip().split() for _ in range(n)]
        row, col = map(int, scan().strip().split())
        direction = scan().strip()
    result = checkers(n, matrix, row, col, direction)
    if type(result) is str:
        ans = result
    else:
        ans = '\n'.join(' '.join(map(str, r)) for r in result)

    # judge
    with open(file_path_ans, encoding='utf-8') as f:
        if f.read().strip() == ans:
            print('AC')
        else:
            print('WA')
    print(ans)


if __name__ == '__main__':
    # main()
    for i in range(1, 6):
        s = time.time_ns()
        custom_judge(i)
        print(f'Execute Time: {(time.time_ns() - s) * (1e-6):.8f} ms', end='\n\n')
