# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o580. 因數計算 (Factor)
# 2024-09 TOI 練習賽 新手組 第三題


def factor(n: int):
    temp = {1, n}
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            temp.update({i, n // i})
    return len(temp)


a, b = map(int, input().split())
arr = [(i, factor(i)) for i in range(a, b + 1)]
print(*max(arr, key=lambda x: (x[1], -x[0])))
