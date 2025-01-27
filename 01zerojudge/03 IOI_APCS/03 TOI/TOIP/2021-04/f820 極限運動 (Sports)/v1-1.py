# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f820. 極限運動 (Sports)
# 2021-04 TOI 練習賽 新手組


n = int(input())
data = tuple(map(int, input().split()))
idx = int(input()) - 1

offset = 1 if idx < n - 2 and data[idx + 1] < data[idx - 1] else -1
while 0 <= idx < n and data[idx + offset] <= data[idx]:
    idx += offset

print(idx + 1)

# 原則上這個應該要吃 WA
# 若測資為下面的狀況:
# 
# 6
# 4 2 1 3 5 1
# 1
# 
# 這段程式碼的結果會輸出 0
# 但實際上應該要輸出 3
# 因為在決定方向的邏輯錯了，當起點在第一格時，程式會檢查 第2格和「最後一格」的大小，這是不應該發生的
