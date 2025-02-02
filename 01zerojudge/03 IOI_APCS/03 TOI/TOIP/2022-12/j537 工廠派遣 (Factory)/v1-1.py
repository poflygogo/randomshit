# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge j537. 工廠派遣 (Factory)
# 2022-12 TOI 練習賽 新手組


n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
data.sort(key=lambda x: (-x[0]))
total_employee = int(input())

cnt = 0
for i, j in data:
    if total_employee <= 0:
        print(cnt)
        break
    cnt += 1
    total_employee -= j
else:
    print(n)
