# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q082. 小明的次方和(簡單版)

# 直接硬算，不套公式了......

def main():
    n = int(input())
    a, b = map(int, input().split())
    print(pow_sum(a, b, n))


def pow_sum(a, b, n):
    if n % 2 == 0:
        return '不能'
    return f'能\n{a ** n + b ** n}'


if __name__ == '__main__':
    main()
