from sys import stdin
from fractions import Fraction as Frac
from math import sqrt, gcd


for _ in stdin:
    for i in range(int(stdin.readline().rstrip())):
        a, b, c = map(int, stdin.readline().rstrip().split())
        check = b ** 2 - 4 * a * c
        if check < 0:
            print(f'{i + 1}. 無解')

        elif check == 0:
            ans = Frac(-b, 2 * a)
            if ans.is_integer():
                print(f'{i + 1}. {ans:.0f} (重根)')
            else:
                print(f'{i + 1}. 分母{ans.denominator}\n{" " * len(f"{i + 1}. ")}分子{ans.numerator} (重根)')

        else:
            if sqrt(check).is_integer():
                check = int(sqrt(check))
                ans1, ans2 = Frac(-b + check, 2 * a), Frac(-b - check, 2 * a)
                print(f'{i + 1}. {ans1} 或 {ans2}')

            else:
                # 將根號化簡為最簡根式
                sqr_fac = 1
                for j in range(1, int(sqrt(check)) + 1):
                    if check % j ** 2 == 0:
                        sqr_fac = j

                simple = gcd(b, sqr_fac, 2 * a)
                check //= sqr_fac ** 2
                sqr_fac //= simple
                denominator = 2 * a // simple
                if denominator == 1:
                    print(
                        f'{i + 1}. {-b // simple}±{sqr_fac if sqr_fac not in (1, -1) else ""}√{check}'
                    )
                else:
                    print(
                        f'{i + 1}. 分母{denominator}',
                        f'{" " * len(f"{i + 1}. ")}分子{-b//simple}±{sqr_fac if sqr_fac not in (1, -1) else ""}√{check}',
                        sep='\n'
                    )


