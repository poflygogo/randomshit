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
    def _gcd(num1: int, num2: int) -> int:
        while num2:
            num1, num2 = num2, num1 % num2
        return num1

    def __str__(self):
        n = self.numerator / self.denominator
        if n.is_integer():
            return f'{n:.0f}'
        return f'{self.numerator}/{self.denominator}'

    def is_integer(self):
        return (self.numerator / self.denominator).is_integer()

    def greater_than_1(self):
        return self.numerator > self.denominator

    def equal_to_1(self):
        return self.numerator == self.denominator

    def sub_1(self):
        return Frac(self.numerator - self.denominator, self.denominator)

    def div_1(self):
        return Frac(self.denominator, self.numerator)

    def add_1(self):
        return Frac(self.numerator + self.denominator, self.denominator)

    def mul_2(self):
        return Frac(self.numerator * 2, self.denominator)


def get_k(n: Frac) -> Frac:
    if n.equal_to_1():
        return Frac(1, 1)
    if n.greater_than_1():
        return get_k(n.sub_1()).mul_2()
    else:
        return get_k(n.div_1()).add_1()


for line in stdin:
    a, b = map(int, line.split())
    print(get_k(Frac(a, b)))


