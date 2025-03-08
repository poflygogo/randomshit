# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b563. 3.魔法學校交換生問題


from collections import defaultdict

data: dict[str, dict[str, int]]

while True:
    try:
        n = int(input())
    except EOFError:
        break

    data = defaultdict(dict)       # {原始學校: {目標學校: 人數}}
    for _ in range(n):
        a, b = input().strip().split()
        data[a][b] = data[a].get(b, 0) + 1
    result = sum(data[i][j] * (i in data[j]) for i in data for j in data[i]) // 2
    print(result)
