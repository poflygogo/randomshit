# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 3330. Find the Original Typed String I


class Solution:
    def possibleStringCount(self, word: str) -> int:
        cnt = len(word)
        for i in range(1, cnt):
            if word[i] != word[i - 1]:
                cnt -= 1
        return cnt


if __name__ == "__main__":
    test = ["abbcccc", "abcd", "aaaa"]
    s = Solution()
    for i in test:
        print(s.possibleStringCount(i))
