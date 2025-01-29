# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g498. 兔子跳躍 (Rabbit)
# 2021-10 TOI 練習賽 新手組


n, m, d = map(int, input().split())
print(
    'YES' if any((d - n * i) % m == 0 for i in range(d // n + 1)) else 'NO'
)
