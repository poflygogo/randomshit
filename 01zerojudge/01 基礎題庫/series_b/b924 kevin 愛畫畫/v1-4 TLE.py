# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b924. kevin 愛畫畫


from sys import stdin


scan = stdin.readline

counter = {}

try:
    for line in stdin:
        if not line.strip():
            print()
            continue
        n, m = map(int, line.strip().split())
        for _ in range(m):
            try:
                a, b = map(int, scan().strip().split())
            except (MemoryError, ValueError):
                a, b = 0, 0
            counter[a] = counter.get(a, False) ^ True
            counter[b] = counter.get(b, False) ^ True
        
        odd_cnt = sum(counter.values())
        print("YES" if odd_cnt in (0, 2) else "NO")
        counter.clear()

except MemoryError:
    print("YES")
