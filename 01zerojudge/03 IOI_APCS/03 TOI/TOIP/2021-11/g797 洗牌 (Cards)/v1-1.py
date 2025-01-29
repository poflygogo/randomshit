# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g797. 洗牌 (Cards)
# 2021-11 TOI 練習賽 新手組


n, m = map(int, input().split())
data = input().split()

for _ in range(m):
    # divide
    data, temp = data[:n // 2], data[n // 2:]

    # merge
    i = 1
    for j in range(n // 2):
        data.insert(i, temp[j])
        i += 2

print(*data)
