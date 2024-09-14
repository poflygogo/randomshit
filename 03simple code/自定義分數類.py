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

    def __floordiv__(self, other):
        self.__truediv__(self, other)

    def __str__(self):
        n = self.numerator / self.denominator
        if n.is_integer():
            return f'{n:.0f}'
        return f'{self.numerator}/{self.denominator}'

    def is_integer(self):
        return (self.numerator / self.denominator).is_integer()

    def __eq__(self, other):
        return (self.numerator == other.numerator) and (self.denominator == other.denominator)


if __name__ == '__main__':
    while True:
        a1, a2 = map(int, input().split())
        b1, b2 = map(int, input().split())
        num1, num2 = Frac(a1, a2), Frac(b1, b2)
        print(
            f'num1 is integer? {num1.is_integer()}',
            f'num2 if integer? {num2.is_integer()}',
            f'num1 == num2? {num1 == num2}',
            f'num1 + num 2 = {num1 + num2}',
            f'num1 - num 2 = {num1 - num2}',
            f'num1 * num 2 = {num1 * num2}',
            f'num1 / num 2 = {num1 / num2}',
            sep='\n'
        )
