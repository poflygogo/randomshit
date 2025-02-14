# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m582. 書房 (Study)
# 2023-11 TOI 練習賽 新手組 第二題


n, m = map(int, input().split())
data = list(map(int, input().split()))

result = [(data[i], i + 1) for i in range(n) if data[i] != 0]
result.sort()
print(' '.join(str(i[1]) for i in result))
