# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b563. 3.魔法學校交換生問題


from collections import defaultdict

# data: dict[str, dict[str, int]]

while True:
    try:
        n = int(input())
    except EOFError:
        break

    result = 0
    data = defaultdict(dict)       # {原始學校: {目標學校: 人數}}
    for _ in range(n):
        a, b = input().strip().split()
        if data.get(b, {}).get(a, 0) > 0:
            result += 1
            data[b][a] -= 1
        else:
            data[a][b] = data[a].get(b, 0) + 1

    print(result)
