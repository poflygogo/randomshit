# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q896. 快樂學幾何4


# 我不知道，我也推不出來這結果
# 只能背答案
from sys import stdin

print("\n".join(f"{i / 2:.1f}" for i in map(int, stdin.read().splitlines())))
