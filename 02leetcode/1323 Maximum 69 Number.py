# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 1323. Maximum 69 Number


class Solution:
    def maximum69Number(self, num: int) -> int:
        digits = str(num)
        idx = digits.find("6")
        if idx == -1:
            return num
        else:
            digits = list(digits)
            digits[idx] = "9"
            return int("".join(digits))
