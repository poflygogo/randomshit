# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10189 Minesweeper
# ZeroJudge e605


cases = 0
while True:
    rows, cols = map(int, input().split())
    if rows == cols == 0:
        break
    cases += 1
    data = [list(input()) for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if data[row][col] == '*':
                for r in range(row - 1 if row > 0 else row, row + 2 if row + 1 < rows else row + 1):
                    for c in range(col - 1 if col > 0 else col, col + 2 if col + 1 < cols else col + 1):
                        if type(data[r][c]) is int:
                            data[r][c] += 1
                        elif data[r][c] == '.':
                            data[r][c] = 1
            
            elif data[row][col] == '.':
                data[row][col] = 0
    
    print(
        f'Field #{cases}:',
        *[''.join(str(i) for i in row) for row in data],
        sep='\n',
        end='\n\n'
    )
