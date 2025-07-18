# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge p907. 學測 (Examination)
# TOI練習賽202504新手組第2題


LEVEL_STR = 'ABCDE'

def judge(score: int, level: list):
    if score == 0:
        return 'X'
    for i in range(len(level)):
        if score >= level[i]:
            return LEVEL_STR[i]
    return 'F'

scores = map(int, input().split())
for i in scores:
    print(judge(i, list(map(int, input().split()))))
