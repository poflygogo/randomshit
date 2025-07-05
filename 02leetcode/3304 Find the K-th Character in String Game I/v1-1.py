# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 3304. Find the K-th Character in String Game I


import math


class Solution:
    def kthCharacter(self, k: int) -> str:
        times = math.ceil(math.log2(k))
        text = [0]
        for _ in range(times):
            text.extend([(i + 1) % 26 for i in text])
        print(text)
        return chr(text[k - 1] + ord("a"))


if __name__ == "__main__":
    test = [5, 10]
    s = Solution()
    for i in test:
        print(s.kthCharacter(i))
