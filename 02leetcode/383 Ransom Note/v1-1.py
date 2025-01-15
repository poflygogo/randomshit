# -*- encoding: utf-8 -*-
# Python 3.12
# LeetCode 383. Ransom Note


import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_freq = collections.Counter(ransomNote)
        magazine_freq = collections.Counter(magazine)
        for char, freq in ransomNote_freq.items():
            if magazine_freq[char] < freq:
                return False
        return True
