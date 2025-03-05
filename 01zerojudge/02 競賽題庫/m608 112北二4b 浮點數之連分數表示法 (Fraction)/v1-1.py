# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m608. 112北二4b.浮點數之連分數表示法 (Fraction)


from math import gcd


def simple_continued_fraction(num: str) -> str:
    if '.' not in num:
        return num
    
    digit, decimal = num.split('.')
    decimal = decimal.rstrip('0')
    if not decimal:
        return digit
    
    numerator, dominator = int(decimal), 10 ** len(decimal)
    numerator, dominator = simplify(numerator, dominator)

    result = []
    while numerator > 0:
        n, numerator, dominator = *divmod(dominator, numerator), numerator
        result.append(n)
    return f'{digit};' + ','.join(map(str, result))


def simplify(a: int, b: int) -> tuple:
    g = gcd(a, b)
    return a // g, b // g


def main():
    while True:
        try:
            n = input()
        except EOFError:
            break
        print(simple_continued_fraction(n))


if __name__ == '__main__':
    main()
