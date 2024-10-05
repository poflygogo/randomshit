rows, cols = map(int, input().split())
matrix = [['.'] * cols for _ in range(rows)]
steps = [int(i) for i in input()]

curr_row, curr_col = 0, 0
matrix[0][0] = '*'
for i in range(len(steps)):
    if i % 4 == 0:      # 右
        for _ in range(steps[i]):
            if curr_col < cols - 1:
                curr_col += 1
                matrix[curr_row][curr_col] = '*'
            else:
                break

    elif i % 4 == 1:    # 下
        for _ in range(steps[i]):
            if curr_row < rows - 1:
                curr_row += 1
                matrix[curr_row][curr_col] = '*'
            else:
                break

    elif i % 4 == 2:    # 左
        for _ in range(steps[i]):
            if curr_col > 0:
                curr_col -= 1
                matrix[curr_row][curr_col] = '*'
            else:
                break

    else:               # 上
        for _ in range(steps[i]):
            if curr_row > 0:
                curr_row -= 1
                matrix[curr_row][curr_col] = '*'
            else:
                break

for row in matrix:
    print(*row, sep='')
