# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n630. 電影院 (Cinema)
# 2024-04 TOI 練習賽 新手組 第一題


n = int(input())
data = [0] * (n + 1)
for i in range(n + 1):
    a, b = map(int, input().split())
    data[i] = a * 60 + b
curr = data.pop() + 20

lft, rgt = 0, n
while lft < rgt:
    mid = (lft + rgt) // 2
    if data[mid] < curr:
        lft = mid + 1
    else:
        rgt = mid

if lft < n:
    s = data[lft]
    print(f'{s // 60:02d} {s % 60:02d}')
else:
    print('Too Late')
