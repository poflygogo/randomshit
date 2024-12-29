# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m685. 三角形計數器


def gcd(a, b) -> int:
    while b != 0:
        a, b = b, a % b
    return a


data = set()
for _ in range(int(input())):
    a, b, c = sorted(map(int, input().split()))
    gcd_abc = gcd(gcd(a, b), c)
    a, b, c = map(lambda x: x // gcd_abc, (a, b, c))
    data.add((a, b, c))

print(len(data))
