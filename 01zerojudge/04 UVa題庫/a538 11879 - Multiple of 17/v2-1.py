from sys import stdin


for n in stdin:
    n = int(n)
    if not n: continue

    if n < 17:
        print(0)
        continue

    if abs(n // 10 - n % 10 * 5) % 17 == 0:
        print(1)
    else:
        print(0)
