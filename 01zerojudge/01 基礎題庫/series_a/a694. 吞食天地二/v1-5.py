while True:
    try:
        # n是矩陣大小, m是測資數量
        n, m = map(int, input().split())

        # 接收矩陣資料, 並處理成前綴和
        matrix = [[0] * (n + 1)]

        for _ in range(n):
            row = list(map(int, input().split()))   # 接收數據

            row_prefix_sum = [0]
            for i, num in enumerate(row):
                row_prefix_sum.append(
                    num + row_prefix_sum[-1] + matrix[-1][i+1] - matrix[-1][i]
                )

            matrix.append(row_prefix_sum)

        # 接收、處理數據後輸出
        for _ in range(m):
            x1, y1, x2, y2 = map(int, input().split())

            print(
                matrix[x2][y2] - matrix[x1-1][y2] - matrix[x2][y1-1] + matrix[x1-1][y1-1]
            )
    except EOFError:
        break
