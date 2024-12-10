# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11728 Alternate Task
# zerojudge e629


import math

class Solution:
    def __init__(self):
        self.cases = 0
        self.mainloop()

    def mainloop(self):
        while True:
            num = int(input())
            if num == 0:
                break
            self.cases += 1
            print(f'Case {self.cases}: {self.judge(num)}')
    
    def judge(self, n: int) -> str:
        if n == 1:
            return 1
        for i in range(n - 1, math.floor(math.sqrt(n)) - 1, -1):
            result = self.factors_sum(i)
            if result == n:
                return str(i)
        return '-1'

    @staticmethod
    def factors_sum(n: int) -> int:
        """integer n 的因數和"""
        temp = {1, n}
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                temp.update({i, n // i})
        return sum(temp)


if __name__ == '__main__':
    Solution()
