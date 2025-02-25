# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11777 Automate the Grades
# ZeroJudge j055


for t in range(1, int(input()) + 1):
    score = list(map(int, input().split()))
    score_total = sum(score[:-3]) + (sum(score[-3:]) - min(score[-3:])) / 2
    if score_total >= 90:
        result = 'A'
    elif score_total >= 80:
        result = 'B'
    elif score_total >= 70:
        result = 'C'
    elif score_total >= 60:
        result = 'D'
    else:
        result = 'F'
    print(f'Case {t}: {result}')
