from sys import stdin


for n in stdin:
    n = int(n)
    if not n: continue
    print(0 if n % 17 else 1)
