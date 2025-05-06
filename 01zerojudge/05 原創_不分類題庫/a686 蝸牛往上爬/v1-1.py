# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a686. 蝸牛往上爬


Fail_MESSAGE = "Poor Snail"
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    if y >= x:
        print(1)
    elif y <= z:
        print(Fail_MESSAGE)
    else:
        result = ((x - y) // (y - z)) + ((x - y) % (y - z) != 0) + 1
        print(result if result else Fail_MESSAGE)
