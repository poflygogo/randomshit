# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 869. Reordered Power of 2

import itertools

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = str(n)
        for i in itertools.permutations(digits):
            if i[0] == '0':
                continue
            num = int(''.join(i))
            if not (num & (num - 1)):
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.reorderedPowerOf2(4802))
