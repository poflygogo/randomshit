# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e169. 粉絲入坑 - V Live & 飯拍影片


base = 100
n = int(input())
while n:
    arr = map(int, input().split())

    # 統計每個數字對 100 的餘數
    counter = {}
    for i in arr:
        reminder = i % base
        counter[reminder] = counter.get(reminder, 0) + 1

    # 統計總和
    # 先特別處理餘數剛好為 0 或 50 的情況
    cnt = counter.get(0, 0) * (counter.get(0, 0) - 1) // 2
    cnt += counter.get(50, 0) * (counter.get(50, 0) - 1) // 2
    for i in range(1, base // 2):
        cnt += counter.get(i, 0) * counter.get(base - i, 0)
    print(cnt)
    n = int(input())
