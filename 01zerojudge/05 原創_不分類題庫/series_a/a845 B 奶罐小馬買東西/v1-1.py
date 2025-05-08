# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a845. B.奶罐小馬買東西
# 102-1 延平資研社練習題


input()
price = list(map(int, input().split()))
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(price[a] + price[b])
