"""
方程式可以寫成 f(x) = y = a(x - x1)^2 + y1
y2 = a(x2 - x1)^2 + y1
a = (y2 - y1) / (x2 - x1)^2, a 不保證一定是整數，應表達成分數的形式，因為浮點數有誤差
最後輸出 {(x2 - x1)^2}y = {(y2 - y1)}x^2 + {(y2 - y1) * x1 * (-2)}x + {(x1)^2 * (y2 - y1) + y1 * (x2 - x1)^2}
"""
from sys import stdin


def gcd(num1: int, num2: int) -> int:
    return num1 if num2 == 0 else gcd(num2, num1 % num2)


for data in stdin:
    x1, y1, x2, y2 = map(int, data.strip().split())
    a = (x2 - x1) ** 2
    b = y2 - y1
    g = gcd(a, b)
    a //= g
    b //= g
    print(
        f'{a}y =',
        f'{b}x^2',
        f'+ {b * x1 * (-2)}x',
        f'+ {x1 ** 2 * b + y1 * a}'
    )
