# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o067. 柯尼斯堡七橋問題

n, m = map(int, input().split())
counter = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    counter[a] += 1
    counter[b] += 1

is_odd = sum(1 for i in counter if i % 2 != 0)
if is_odd > 3:
    print('NO')
else:
    print('YES')
