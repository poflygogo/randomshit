# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e664. 108 p2. 空氣盒子
# 108新北市資訊學科能力複賽


# ---------------------------------------------------

import sys
import io
Q = """48 52 47 46 44 42 43 44 47 49 44 43 39 40 40 36 31 36 36 37 42 51 59 62 62 67 75 70 66 69 70"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------



def air_box(info: list):
    result = []
    last_idx = 0
    for i in range(1, len(info) - 1):
        if info[last_idx] < info[i] > info[i + 1]:
            if last_idx + 1 == i:
                result.append((i + 1, info[i]))
            else:
                result.append((last_idx + 2, i + 1, info[i]))
        elif info[i] == info[i + 1]:
            continue
        last_idx = i

    if result:
        return result
    else:
        return [(0, 0)]


result = air_box(list(map(int, input().split())))
print('\n'.join(' '.join(map(str, i)) for i in result))
