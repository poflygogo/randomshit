# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 191. Number of 1 Bits


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
