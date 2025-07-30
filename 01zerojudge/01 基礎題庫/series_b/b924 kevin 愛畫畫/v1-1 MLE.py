# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b924. kevin 愛畫畫


from sys import stdin


scan = stdin.readline

for line in stdin:
    if not line.strip():
        print()
        continue
    n, m = map(int, line.strip().split())
    counter = {}
    for _ in range(m):
        a, b = map(int, scan().strip().split())
        counter[a] = counter.get(a, 0) + 1
        counter[b] = counter.get(b, 0) + 1
    
    odd_cnt = 0
    for i in counter.values():
        if i % 2 != 0:
            odd_cnt += 1
    
    print("YES" if odd_cnt in (0, 2) else "NO")
