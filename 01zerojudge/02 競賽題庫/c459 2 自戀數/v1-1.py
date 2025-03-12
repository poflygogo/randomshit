# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c459. 2. 自戀數


base, num = input().split()
decimal = int(num, int(base))
if sum(int(i) ** len(num) for i in num) == decimal:
    print('YES')
else:
    print('NO')
