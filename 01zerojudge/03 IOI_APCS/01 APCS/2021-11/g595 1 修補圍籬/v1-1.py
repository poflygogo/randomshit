# -*- encoding: utf-8 -*-
# python 3.12
# 2021-11 APCS
# ZeroJudge f595


n = int(input()) - 1
fence = tuple(map(int, input().split()))

result = []
for i in range(n + 1):
    if fence[i] != 0:
        continue
    result.append(
        fence[i + 1] if i == 0 else
        fence[i - 1] if i == n else
        min(fence[i - 1], fence[i + 1])
    )

print(sum(result))
