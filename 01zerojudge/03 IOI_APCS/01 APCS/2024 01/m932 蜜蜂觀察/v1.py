rows, cols, steps = map(int, input().split())
data = [input() for _ in range(rows)]
path = tuple(map(int, input().split()))

result = ''
curr_row, curr_col = rows - 1, 0
for step in path:
    if step == 0:
        dir_row, dir_col = -1,  0
    elif step == 1:
        dir_row, dir_col =  0,  1
    elif step == 2:
        dir_row, dir_col =  1,  1
    elif step == 3:
        dir_row, dir_col =  1,  0
    elif step == 4:
        dir_row, dir_col =  0, -1
    else:
        dir_row, dir_col = -1, -1
    
    if 0 <= curr_row + dir_row < rows and 0 <= curr_col + dir_col < cols:
        curr_row += dir_row
        curr_col += dir_col

    result += data[curr_row][curr_col]

print(result, len(set(result)), sep='\n')