# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 412. Fizz Buzz


from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [
            'Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or str(i)
            for i in range(1, n + 1)
        ]
