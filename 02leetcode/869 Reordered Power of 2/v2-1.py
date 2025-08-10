# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 869. Reordered Power of 2


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digits(x):
            return ''.join(sorted(str(x)))

        target = count_digits(n)
        
        for i in range(31):
            if count_digits(1 << i) == target:
                return True
        return False
    