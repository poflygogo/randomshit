p, a, b = map(int, input().split())

if p >= a:
    print(p + b * int((p - a) / (a - b) + 1))
else:
    print(p)