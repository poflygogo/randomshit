# -*- encoding: utf-8 -*-
# Python 3.12
# LeetCode 383. Ransom Note


import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
