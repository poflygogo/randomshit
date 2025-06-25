# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 258. Add Digits


class Solution:
    def addDigits(self, num: int) -> int:
        return num if num < 10 else self.addDigits(sum(map(int, str(num))))
