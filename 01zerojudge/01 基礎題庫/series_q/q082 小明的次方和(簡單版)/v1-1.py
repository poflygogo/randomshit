# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q082. 小明的次方和(簡單版)

# 有三個正整數 a, b, n
# 當 n 為奇數時，a^n + b^n 可以分解成
# (a + b)(a^(n-1) - a^(n-2)b + a^(n-3)b^2 ... + b^(n-1)) 
# 例如 a^3 + b^3 = (a + b)(a^2 - ab + b^2)

def main():
    n = int(input())
    a, b = map(int, input().split())
    print(pow_sum(a, b, n))


def pow_sum(a, b, n):
    if n % 2 == 0:
        return '不能'

    factor1 = a + b
    factor2 = sum(
        a ** ((n - 1) - i) * b ** i - a ** ((n - 1) - (i + 1)) * b ** (i + 1)
        for i in range(0, n - 1, 2)
    )
    factor2 += b ** (n - 1)
    return f'能\n{factor1 * factor2}'


if __name__ == '__main__':
    main()
