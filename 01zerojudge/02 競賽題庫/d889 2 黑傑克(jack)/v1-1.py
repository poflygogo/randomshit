# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d889. 2.黑傑克(jack)
# 99學年度台北市資訊學科能力競賽


def jack(n: int, arr: list):
    if n == 0 or arr[0] > 30:
        return 30
    time = 0
    for i in arr:
        if i - time >= 30:
            break
        elif i > time:
            time = i + 5
        else:
            time += 5
    return time + 30


print(jack(int(input()), list(map(int, input().split()))))
