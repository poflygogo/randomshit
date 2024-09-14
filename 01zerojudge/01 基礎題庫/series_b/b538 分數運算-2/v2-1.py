from sys import stdin


class Frac:
    def __init__(self, a: int, b: int):
        self.numerator = a
        self.denominator = b
        self.simplify()

    def simplify(self):
        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    @staticmethod
    def _gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Frac(numerator, denominator)

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Frac(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Frac(numerator, denominator)

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Frac(numerator, denominator)

    def __str__(self):
        n = self.numerator / self.denominator
        if n.is_integer():
            return f'{n:.0f}'
        return f'{self.numerator}/{self.denominator}'

    def is_integer(self):
        return (self.numerator / self.denominator).is_integer()


operate = {
    '+': Frac.__add__,
    '-': Frac.__sub__,
    '*': Frac.__mul__,
    '/': Frac.__truediv__
}
for line in stdin:
    a1, a2, b1, b2, op = line.strip().split()
    print(
        operate[op](
            Frac(int(a1), int(a2)),
            Frac(int(b1), int(b2))
        )
    )

