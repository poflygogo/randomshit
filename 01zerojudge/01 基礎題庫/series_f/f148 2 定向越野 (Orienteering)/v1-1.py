# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f148. 2. 定向越野 (Orienteering)
# TOI 2020-06 練習賽 新手組


rows, cols = map(int, input().split())  # 接受行列資料
request = int(input())                  # 接受需要尋找的目標數量

# 紀錄字母出現的位置
data = {}
for row in range(rows):
    for col, item in enumerate(input().split()):
        if item != '0':
            data[item] = (row, col)

# 若被記錄到的字母比 request 少，則輸出 Mission fail
if len(data) < request:
    print('Mission fail.')

# 反之則按字典序輸出前 request 個結果
else:
    for _, ans in zip(range(request), sorted(data)):
        print(*data[ans])
