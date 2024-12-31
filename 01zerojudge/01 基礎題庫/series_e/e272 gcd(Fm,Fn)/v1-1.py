# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e272. gcd(Fm,Fn)


def main():
    fib = create_fib_list()
    while True:
        try:
            m, n = map(int, input().split())
        except EOFError:
            break

        print(fib[gcd(m, n) - 1])


def create_fib_list(max_limit=93) -> list:
    # 題目表明最終答案不會超過 unsigned long long int 的範圍
    # 也就是答案會小於 2^64
    # 故只需生成到第 93 個即可
    fib = [0] * max_limit
    fib[0] = fib[1] = 1
    for i in range(2, max_limit):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    main()
