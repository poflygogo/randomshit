# 須測試多筆資料，故需要無限循環
while True:

    # 當檢測到EOF錯誤時，就停止循環
    try:
        # 創建一個空列表，用來存放矩陣資料
        matrix = list()

        # 獲取矩陣的長度和寬度
        a, b = (map(int,input().split()))

        # 將矩陣資料逐步放進列表中
        for row in range(a):
            matrix.append(tuple(map(int,input().split())))
            
        # 用指針取得數據資料，並輸出
        for column in range(b):
            output = []
            for row in range(a):
                output.append(matrix[row][column])
            print(*output)
    except EOFError:
        break
