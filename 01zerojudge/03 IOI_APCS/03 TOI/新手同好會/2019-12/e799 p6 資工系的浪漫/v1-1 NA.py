# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e799. p6. 資工系的浪漫
# 2019-12 TOI 新手同好會


import math


class Solution:
    def __init__(self):
        self.POWER_of_2 = self.create_power_of_2_list()
        self.row, self.col = map(int, input().split())
        self.token = input()
        self.code = [int(input()) for _ in range(self.row)]

    def main(self):
        decode = [self.decode(i) for i in self.code]
        self.print_pic(decode)


    def create_power_of_2_list(self, max_limit=62):
        result = [0] * (max_limit + 1)
        result[0] = 1
        for i in range(1, max_limit + 1):
            result[i] = result[i - 1] * 2
        return result

    def decode(self, n: int):
        def backtrack(remain: int, path: list, exponent: int):
           nonlocal result
           if remain == 0:
               result = path.copy()
               return
           if remain < 0:
               return
           for i in range(exponent, -1, -1):
               path.append(i)
               backtrack(remain - self.POWER_of_2[i], path, i - 1)
               path.pop()

        if n == 0:
            return []
        result = None
        backtrack(n, [], math.floor(math.log(n, 2)))
        return result
    
    def print_pic(self, decode):
        result = [['.'] * self.col for _ in range(self.row)]
        for r in range(self.row):
            for c in decode[r]:
                result[r][c] = self.token
        print('\n'.join(' '.join(row) for row in result))


if __name__ == '__main__':
    s = Solution()
    s.main()
