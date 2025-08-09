# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 231. Power of Two


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return bool(n and not (n & n - 1))
