# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f707. 幸運 7 (Lucky Seven)
# 2021-03 TOI 練習賽 新手組


def rule(n: int):
    if n % 7 == 0:
        return True, n % 70
    else:
        return False, -(n % 77)


nums = list(map(int, input().split()))
nums.pop()
print(max(nums, key=rule))
