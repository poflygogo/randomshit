# -*- encoding: utf-8 -*-
# python 3.6.8
# UVa 12970 Alcoholic Pilots
# ZeroJudge h385


from fractions import Fraction


class Frac(Fraction):
    def is_integer(self):
        return self.denominator == 1


v1, d1, v2, d2 = map(int, input().split())
test_case = 1
beer = ('No beer for the captain.', 'You owe me a beer!')
while any((v1, d1, v2, d2)):
    a, b = Frac(d1, v1), Frac(d2, v2)
    winner = beer[bool(a < b)]
    avg = Frac(a + b, 2)
    if avg.is_integer():
        avg = str(avg.numerator)
    else:
        avg = f'{avg.numerator}/{avg.denominator}'

    print(f'Case #{test_case}: {winner}\nAvg. arrival time: {avg}')
    test_case += 1
    v1, d1, v2, d2 = map(int, input().split())
