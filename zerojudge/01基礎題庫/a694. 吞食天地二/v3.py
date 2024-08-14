from itertools import accumulate
# n是矩陣大小, m是測資數量
n, m = map(int, input().split())

# 接收矩陣資料, 並處理成前綴和
matrix = []
for _ in range(n):
    matrix.append([0] + list(accumulate(map(int, input().split()))))

# 接收、處理數據後輸出
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    total = 0
    for index, line in enumerate(matrix):
        if index < x2:
            if index >= (x1 - 1):
                total += (line[y2] - line[y1-1])
        else:
            break
    
    print(total)
