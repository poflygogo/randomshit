# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 9. Palindrome Number


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        reverse_num = 0
        temp = x
        while temp > 0:
            reverse_num = reverse_num * 10 + temp % 10
            temp //= 10
        return x == reverse_num


if __name__ == '__main__':   
    s = Solution()
    print(s.isPalindrome(121))
