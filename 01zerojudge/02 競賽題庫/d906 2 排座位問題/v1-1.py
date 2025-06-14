# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d906. 2. 排座位問題
# 99學年度北基區資訊學科能力競賽


mon = int(input())
start = int(input())
student = [input().split() for _ in range(6)]

if mon % 2:
    student.sort(key=lambda x: int(x[1]))
else:
    student.sort(key=lambda x: (int(x[2]), int(x[1])))

print(student[(8 - start) % 6][0])
