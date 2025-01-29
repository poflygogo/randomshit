# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g797. 洗牌 (Cards)
# 2021-11 TOI 練習賽 新手組


def divide_and_merge(n):
    a, b = list(range(n // 2)), list(range(n // 2, n))
    i = 1
    for j in range(n // 2):
        a.insert(i, b[j])
        i += 2
    return a


n, m = map(int, input().split())
idx_info = divide_and_merge(n)
data = input().split()

for _ in range(m):
    data = [data[i] for i in idx_info]

print(*data)
