# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e796. p3. 站牌廣告
# 2019-12 TOI 新手同好會


B = int(input())
P = int(input())

arr = [0] * B
for _ in range(P):
    a, b = sorted(map(int, input().split()))
    for i in range(a - 1, b):
        arr[i] += 1

print(arr.index(min(arr)) + 1, B - arr[::-1].index(max(arr)))

# 笑死，根本土法煉鋼w
