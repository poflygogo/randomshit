# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11728 Alternate Task
# zerojudge e629


class Solution:
    def __init__(self):
        self.result = {self.factors_sum(i):i for i in range(1, 1001)}
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
        if n in self.result:
            return str(self.result[n])
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
