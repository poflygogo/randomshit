# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k721. 肥余歷險記---(數學城2)


from sys import stdin


def can_afford(a, b):
    return "能" if (a <= b) or (a <= 0) else "不能"


print("\n".join(can_afford(*map(int, i.split())) for i in stdin.read().splitlines()))
