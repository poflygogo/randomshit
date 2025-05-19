# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 224. Basic Calculator


class Solution:
    operate = {'+': int.__add__,
               '-': int.__rsub__}
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('(', ' ( ').replace(')', ' ) ').strip().split()
        num = []
        operator = []
        sign = False
        for i in s:
            match i:
                case '+':
                    while operator and operator[-1] != '(':
                        num.append(self.operate[operator.pop()](num.pop(), num.pop()))
                    operator.append(i)
                case '-':
                    if not num or (operator and operator[-1] == '('):
                        sign = True
                    else:
                        operator.append(i)
                case '(':
                    operator.append(i)
                case ')':
                    while operator and operator[-1] != '(':
                        num.append(self.operate[operator.pop()](num.pop(), num.pop()))
                    operator.pop()
                case _:
                    num.append(int(i))
                    if sign:
                        num[-1] *= -1
                        sign = False
        while operator:
            num.append(self.operate[operator.pop()](num.pop(), num.pop()))
        return num.pop()


# testing
if __name__ == '__main__':
    a = Solution()
    print(a.calculate('(1+(4+5+2)-3)+(6+8)'))
