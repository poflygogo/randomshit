# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 43. Multiply Strings


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return "0"
    
        num1_list = [ord(i) - 48 for i in reversed(num1)]
        result = [0] * (len(num1) + len(num2))
        for idx, i in enumerate(reversed(num2)):
            curr = idx
            for j in num1_list:
                result[curr] += (ord(i) - 48) * j
                k, result[curr] = divmod(result[curr], 10)
                result[curr + 1] += k
                curr += 1
        return ''.join(chr(i + 48) for i in reversed(result)).lstrip('0')


if __name__ == '__main__':
    s = Solution()
    print(s.multiply('12', '13'))
