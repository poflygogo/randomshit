# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 3330. Find the Original Typed String I


from itertools import groupby


class Solution:
    def possibleStringCount(self, word: str) -> int:
        cnt = 1
        for _, j in groupby(word):
            if (length := len(list(j))) > 1:
                cnt += length - 1
        return cnt


if __name__ == "__main__":
    test = ["abbcccc", "abcd", "aaaa"]
    s = Solution()
    for i in test:
        print(s.possibleStringCount(i))
