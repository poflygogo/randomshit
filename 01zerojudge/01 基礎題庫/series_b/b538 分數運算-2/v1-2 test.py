from fractions import Fraction
# from sys import stdin


operate = {
    '+': Fraction.__add__,
    '-': Fraction.__sub__,
    '*': Fraction.__mul__,
    '/': Fraction.__floordiv__
}
stdin = open('test.txt', 'r', encoding='utf-8')
for line in stdin:
    a1, a2, b1, b2, op = line.strip().split()
    print(
        operate[op](Fraction(int(a1), int(a2)),
                    Fraction(int(b1), int(b2))
                    )
    )
