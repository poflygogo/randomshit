def mine_small(a:int, b:int):
    """標記小地雷的小十字危險區"""
    danger[a][b] += 1
    if a != 0:
        danger[a - 1][b] += 1
    if a != (num_row - 1):
        danger[a + 1][b] += 1
    if b != 0:
        danger[a][b - 1] += 1
    if b != (num_column - 1):
        danger[a][b + 1] += 1

def mine_big(a:int, b:int):
    """標記大地雷的大十字危險區"""
    danger[a] = [i + 1 for i in danger[a]]
    for i in range(num_row):
        danger[i][b] += 1
    danger[a][b] -= 1


num_row, num_column = map(int, input().split())
danger = [[0 for _ in range(num_column)] for _ in range(num_row)]

for row in range(num_row):
    for column, item in enumerate(map(int, input().split())):
        if item != 0:
            if item == 1:
                mine_small(row, column)
            else:
                mine_big(row, column)

for line in danger:
    print(*line)