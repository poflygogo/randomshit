# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f373. 週年慶 Anniversary
# 2020-10 TOI 練習賽 新手組


n = int(input())
print(*min((n - n // 2000 * 200, 0), (n - n // 1000 * 100, 1), key=lambda x: x[0]))
