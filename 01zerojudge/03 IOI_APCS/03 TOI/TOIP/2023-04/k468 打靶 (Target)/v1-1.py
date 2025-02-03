# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k468. 打靶 (Target)
# 2023-04 TOI 練習賽 新手組

# O(n^2)


n, s, f = map(int, input().split())
target = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if target[i] is None:
        continue
    cnt += 1

    temp = target[i]
    s -= (temp == f)

    if s == 0:
        print(cnt)
        break

    target[i] = None
    if temp in target:
        target[target.index(temp)] = None
        s -= (temp == f)    

    if s == 0:
        print(cnt)
        break
