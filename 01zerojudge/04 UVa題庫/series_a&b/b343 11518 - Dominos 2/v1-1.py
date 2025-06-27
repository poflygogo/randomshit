# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11518 Dominos 2
# ZeroJudge b343


from collections import defaultdict

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    links = defaultdict(set)
    for _ in range(m):
        a, b = map(int, input().split())
        links[a].add(b)

    seen = set()
    stack = []
    for _ in range(k):
        stack.append(int(input()))
        while stack:
            i = stack.pop()
            if i not in seen:
                seen.add(i)
                stack.extend(links[i])
    print(len(seen))
