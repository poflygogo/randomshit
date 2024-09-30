"""
zerojudge 的 python 沒有 math.lcm
"""

from math import lcm


while True:
    if input() == '0':
        break

    print(lcm(*map(int, input().split())))
