# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge p900. 旅遊計畫 (Travel)
# 2024-12 TOI 練習賽 新手組 第一題


data_a = tuple(map(int, input().split()))
data_b = tuple(map(int, input().split()))

result = min(
    ((i + 1, j + 1, data_a[i] + data_b[j] + 1000 * (j - i)) for i in range(10) for j in range(i, 10)),
    key=lambda x: x[2]
)
print(*result)
