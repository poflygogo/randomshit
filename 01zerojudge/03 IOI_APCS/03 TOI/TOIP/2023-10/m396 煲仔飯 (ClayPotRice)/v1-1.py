# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m396. 煲仔飯 (ClayPotRice)
# 2023-10 TOI 練習賽 新手組 第一題


t, *times = map(int, input().split())
result = sum(times)
if result > t:
    print(-1)
else:
    print(result)
