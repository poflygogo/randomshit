# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 258. Add Digits


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9
