# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a846. C.曹冶的成績處理系統
# 102-1延平資研社練習題


for _ in range(int(input())):
    quest = int(input().split()[1])
    score = list(map(int, input().split()))
    for _ in range(quest):
        k, *stu = map(int, input().split())
        if k == 1:
            print(max(score[stu[0]: stu[1] + 1]))
        elif k == 2:
            print(int(sum(score[stu[0]: stu[1] + 1]) / (stu[1] - stu[0] + 1)))
        elif k == 3:
            print(score[stu[0]])
