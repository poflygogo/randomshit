# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b924. kevin 愛畫畫


from sys import stdin

scan = stdin.readline

elements = set()
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
                print("YES" if m % 2 else "NO")
                exit()
            if a in elements:
                elements.remove(a)
            else:
                elements.add(a)
            if b in elements:
                elements.remove(b)
            else:
                elements.add(b)
        
        print("YES" if len(elements) in (0, 2) else "NO")
        elements.clear()

except MemoryError:
    print("YES")
