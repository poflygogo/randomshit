# n是矩陣大小, m是測資數量
n, m = map(int, input("矩陣大小與測資數量: ").split())

# 接收矩陣資料
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input(f"第{_}行矩陣: ").split())))

# 接收、處理數據後輸出
for _ in range(m):
    x1, y1, x2, y2 = map(int, input("輸入範圍: ").split())

    total = 0
    for index, line in enumerate(matrix):
        if index < x2:
            if index >= (x1 - 1):
                total += sum(line[y1-1:y2])
        else:
            break
    
    print(f"答案： {total}")
