# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 43. Multiply Strings


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_int = self.str_to_int(num1)
        num2_int = self.str_to_int(num2)
        return self.int_to_str(num1_int * num2_int)

    def str_to_int(self, num: str) -> int:
        arr = [ord(i) - 48 for i in num]
        return sum(j * 10 ** i for i, j in enumerate(reversed(arr)))

    def int_to_str(self, num: int) -> str:
        if num == 0:
            return chr(48)
        arr = []
        while num:
            num, b = divmod(num, 10)
            arr.append(b)
        return ''.join(chr(i + 48) for i in reversed(arr))
