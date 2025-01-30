# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge i070. 比對卡片 (Match)
# 2022-04 TOI 練習賽 新手組


n = int(input())
teacher = list(map(int, input().split()))
student = tuple(map(int, input().split()))

for i in range(n):
    if teacher[i] not in student:
        teacher[i] = -1
    else:
        j = 0
        while teacher[i] not in (
            student[i - j] if i - j >= 0 else None,
            student[i + j] if i + j < n else None):
            j += 1
        teacher[i] = j

print(*teacher)
