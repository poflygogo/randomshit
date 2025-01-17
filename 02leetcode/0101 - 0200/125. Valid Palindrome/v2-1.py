# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 125. Valid Palindrome


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_temp: list[str] = [i.lower() for i in s if i.isalnum()]
        return all(s_temp[i] == s_temp[-i - 1] for i in range(len(s_temp) // 2))
