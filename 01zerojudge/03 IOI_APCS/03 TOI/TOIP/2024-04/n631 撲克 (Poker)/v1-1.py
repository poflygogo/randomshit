# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n630. 電影院 (Cinema)
# 2024-04 TOI 練習賽 新手組 第二題


n = int(input())
data = list(map(int, input().split()))
counter = [data.count(i) for i in range(1, 53)]
min_num, max_num = min(counter), max(counter)
print(
    min_num,
    (max_num - min_num) * 52 - (n - min_num * 52)
)
