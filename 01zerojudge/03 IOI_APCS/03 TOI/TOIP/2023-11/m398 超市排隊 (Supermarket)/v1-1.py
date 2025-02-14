# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m398. 超市排隊 (Supermarket)
# 2023-11 TOI 練習賽 新手組 第三題


arr = tuple(map(int, input().split()))
data = [tuple(map(int, input().split())) for _ in range(3)]
result = [(i + 1, sum(data[i]) * 3 + (arr[i] - 1) * 2) for i in range(3)]
print(*min(result, key=lambda x: x[1]))
