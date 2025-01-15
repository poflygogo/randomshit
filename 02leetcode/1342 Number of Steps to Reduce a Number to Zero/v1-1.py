# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 1342. Number of Steps to Reduce a Number to Zero


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            steps += 1
        return steps
