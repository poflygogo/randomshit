# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o337. YTPizza


input()
arr = input().split()
seen = set()

result = []
for i in arr:
    if i not in seen:
        result.append(i)
        seen.add(i)

print(' '.join(result))
