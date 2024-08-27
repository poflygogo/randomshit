

matrix = [[1, 1, 0], [1, 1, 1], [1, 1, 0]]

count = 0
row, col = 0, 0
while row < 3 and col < 3:
    if matrix[row][col] == 0:
        if col < 2:
            col += 1
        else:
            row += 1
            col = 0
        continue

    count += 1
    matrix[row][col] == 0

    if row != 2 and col != 2:
        if matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1] == 1:
            matrix[row][col + 1] = 0
            matrix[row + 1][col] = 0
            matrix[row + 1][col + 1] = 0

            if row != 1 and col != 1:
                curr_row = [i for i in matrix[row + 2]]
                curr_col = [matrix[i][col] for i in range(col + 1)]
                if (sum(curr_row) + sum(curr_col)) == (len(curr_row) + len(curr_col)):
                    break
    
    if col < 2:
        col += 1
    else:
        row += 1
        col = 0
    continue

print(count)