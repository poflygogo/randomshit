# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a686. 蝸牛往上爬


from sys import stdin

Fail_MESSAGE = "Poor Snail"
_, *ipt = stdin.readlines()
result = []
for line in ipt:
    x, y, z = map(int, line.split())
    if y >= x:
        result.append('1')
    elif y <= z:
        result.append(Fail_MESSAGE)
    else:
        k = ((x - y) // (y - z)) + ((x - y) % (y - z) != 0) + 1
        result.append(str(k) if k else Fail_MESSAGE)
print('\n'.join(result))
