# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 869. Reordered Power of 2

import collections
from typing import List

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = self.get_all_digits(n)
        length = sum(digits.values())
        return any(self.perm(digits, length, []))
    
    def get_all_digits(self, n: int):
        res = collections.Counter()
        while n:
            n, digit = divmod(n, 10)
            res[digit] += 1
        return res
    
    def perm(self, digits: collections.Counter, length: int, path: List):
        if len(path) == length:
            num = sum(j * 10 ** i for i, j in enumerate(reversed(path)))
            yield bool(not num & num - 1)
        
        for i in digits:
            if i == 0 and not path:
                continue
            if digits[i] > 0:
                digits[i] -= 1
                path.append(i)
                yield from self.perm(digits, length, path)
                digits[i] += 1
                path.pop()
