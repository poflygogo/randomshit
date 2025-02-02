# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k254. 拍七 (Seven)
# 2023-03 TOI 練習賽 新手組


start, end, base, k = map(int, input().split())

for i in range(start, end + 1):
    if i % base == 0 or str(base) in str(i):
        k -= 1

    if k == 0:
        print(i)
        break
else:
    print(-1)
