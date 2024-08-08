from sys import stdin

data = stdin.readlines()
data = [line.strip() for line in data][1:]

for line in data:
    a, b, c= map(int, line.split())
    if a == 1:print(b + c)
    elif a == 2:print(b - c)
    elif a == 3:print(b * c)
    else:print(int(b / c))
