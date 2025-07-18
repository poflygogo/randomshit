# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge p906. 食譜換算 (Recipe)
# TOI練習賽202504新手組第1題


n, a = map(int, input().split())
arr = list(map(int, input().split()))
b = arr.pop()

def calc(num):
    num *= b
    num, reminder = divmod(num, a)
    if reminder:
        return str(num + 1)
    else:
        return str(num)

print(' '.join(map(calc, arr)))
