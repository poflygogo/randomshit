# -*- encoding: utf-8 -*-
# UVa 11172 Relational Operators
# ZeroJudge d143

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(
        '<' if a < b else
        '>' if a > b else
        '='
    )
