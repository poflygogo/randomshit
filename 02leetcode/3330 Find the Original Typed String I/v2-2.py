# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 3330. Find the Original Typed String I


class Solution:
    def possibleStringCount(self, word: str) -> int:
        return len(word) - sum(word[i] == word[i + 1] for i in range(len(word) - 1))


if __name__ == "__main__":
    test = ["abbcccc", "abcd", "aaaa"]
    s = Solution()
    for i in test:
        print(s.possibleStringCount(i))
