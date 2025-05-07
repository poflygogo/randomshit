from sys import stdin


for n in stdin:
    n = int(n.rstrip())
    if n < 0:
        print(-1)
        break
    print(f'{n:o}')
