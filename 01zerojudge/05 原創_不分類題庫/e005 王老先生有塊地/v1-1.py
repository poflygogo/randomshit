# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e005. 王老先生有塊地


def total_stakes(x1, y1, x2, y2, x3, y3) -> int:
    return sum([
        gcd(abs(x2 - x1), abs(y2 - y1)),
        gcd(abs(x3 - x2), abs(y3 - y2)),
        gcd(abs(x1 - x3), abs(y1 - y3))
    ])


def gcd(a, b) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    while True:
        x1, y1, x2, y2, x3, y3 = map(int, input().split())
        if x1 == x2 == x3 == y1 == y2 == y3 == 0:
            break
        print(total_stakes(x1, y1, x2, y2, x3, y3))


if __name__ == "__main__":
    main()
