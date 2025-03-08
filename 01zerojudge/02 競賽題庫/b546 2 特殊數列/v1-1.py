# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b546. 2.特殊數列


def operate(start: int, target: int) -> int:
    dp = [0] * target
    dp[0] = start
    for i in range(1, target):
        if dp[i - 1] % i == 0:
            dp[i] = dp[i - 1] // i
        else:
            dp[i] = dp[i - 1] * i
    return dp[-1]


def main():
    while True:
        try:
            a, b = map(int, input().split())
        except EOFError:
            break
        print(operate(a, b))


if __name__ == '__main__':
    main()
