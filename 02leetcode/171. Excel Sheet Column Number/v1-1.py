# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 171. Excel Sheet Column Number


from typing import List


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in columnTitle:
            result *= 26
            result += ord(i) - 64
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.titleToNumber('AA'))
