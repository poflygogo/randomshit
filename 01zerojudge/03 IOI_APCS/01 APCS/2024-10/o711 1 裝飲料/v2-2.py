# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o711. 1. 裝飲料
# 2024-10 APCS


n = int(input())
w1, w2, h1, h2 = map(int, input().split())
liquid = tuple(map(int, input().split()))

w1 **= 2
w2 **= 2

result = []
for i in liquid:
    if h1:
        rise = min(i // w1, h1)
        h1 -= rise
        if h1 == 0:
            rise2 = min((i - w1 * rise) // w2, h2)
            rise += rise2
            h2 -= rise2
    elif h2:
        rise = min(i // w2, h2)
        h2 -= rise
    else:
        break
    result.append(rise)

print(max(result))
