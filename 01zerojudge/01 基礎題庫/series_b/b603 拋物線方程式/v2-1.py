from sys import stdin


class Frac:
    """用來表示分數"""
    def __init__(self, num1: int, num2: int):
        self.numerator = num1       # 分子
        self.denominator = num2     # 分母
        self.simplify()             # 化簡

    def simplify(self):
        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        if self.numerator < 0:
            self.numerator *= -1
            self.denominator *= -1

    @staticmethod
    def _gcd(num1: int, num2: int) -> int:
        while num2:
            num1, num2 = num2, num1 % num2
        return num1


for data in stdin:
    x1, y1, x2, y2 = map(int, data.strip().split())
    a = Frac((x2 - x1) ** 2, y2 - y1)
    print(
        f'{a.numerator}y =',
        f'{a.denominator}x^2',
        f'+ {a.denominator * x1 * (-2)}x',
        f'+ {x1 ** 2 * a.denominator + y1 * a.numerator}'
    )
